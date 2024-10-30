import heapq
from flask import request, jsonify
from collections import deque
from models.ModelPedido import ModelPedido
from decimal import Decimal

class PedidosController:
    def __init__(self):
        self.pedidos_cola = deque()
        self.pedidos_heap = []
        
    def agregar_pedido_con_prioridad(self, pedido_id, prioridad):
        heapq.heappush(self.pedidos_heap, (-prioridad, pedido_id))
    
    def obtener_pedido_con_mayor_prioridad(self):
        if self.pedidos_heap:
            prioridad, pedido_id = self.pedidos_heap[0]
            return {
                "pedido_id": pedido_id,
                "prioridad": -prioridad 
            }
        else:
            return {"message": "No hay pedidos en el heap"}

    def mostrar_todos_los_pedidos_priorizados(self):
        pedidos_priorizados = sorted(
            [(-prioridad, pedido_id) for prioridad, pedido_id in self.pedidos_heap],
            reverse=True
        )
        return [{"pedido_id": pid, "prioridad": prioridad} for prioridad, pid in pedidos_priorizados]

    def extraer_pedido_con_mayor_prioridad(self):
        if self.pedidos_heap:
            prioridad, pedido_id = heapq.heappop(self.pedidos_heap)
            return {
                "pedido_id": pedido_id,
                "prioridad": -prioridad  
            }
        else:
            return {"message": "No hay pedidos en el heap"}
      
    def cargar_todos_pedidos_desde_db(self):
        self.pedidos_cola.clear()
        pedidos, status_code = ModelPedido().obtener_todos_pedidos()
        
        if status_code == 200:
            for pedido in pedidos:
                pedido_dict = {
                    "pedido_id": pedido["id"],
                    "usuario_id": pedido["usuario_id"],
                    "fecha": str(pedido["fecha"]),  
                    "total": float(pedido["total"]) if isinstance(pedido["total"], Decimal) else pedido["total"],  # Convertir Decimal a float
                    "estado": pedido["estado"]
                }
                if not any(p["pedido_id"] == pedido_dict["pedido_id"] for p in self.pedidos_cola):
                    self.pedidos_cola.append(pedido_dict)
                        
    def cargar_pedidos_desde_db(self):

        pedidos, status_code = ModelPedido().obtener_pedidos_pendientes()
        
        if status_code == 200:
            for pedido in pedidos:
                
                pedido_dict = {
                    "pedido_id": pedido["id"],
                    "usuario_id": pedido["usuario_id"],
                    "fecha": str(pedido["fecha"]),  
                    "total": float(pedido["total"]) if isinstance(pedido["total"], Decimal) else pedido["total"],  # Convertir Decimal a float
                    "estado": pedido["estado"]
                }
                
                if not any(p["pedido_id"] == pedido_dict["pedido_id"] for p in self.pedidos_cola):
                    self.pedidos_cola.append(pedido_dict)
                        
    def agregar_pedido(self):
        usuario_id = request.json.get('usuario_id')
        total = request.json.get('total')
        estado = request.json.get('estado', 'pendiente')
        detalles = request.json.get('detalles', [])

        resultado, status_code = ModelPedido().agregar_pedidoDB(usuario_id, total, estado, detalles)
        if status_code == 201:
            
            pedido = {
                "pedido_id": resultado['data']['pedido_id'],
                "usuario_id": usuario_id,
                "total": total,
                "estado": estado,
                "detalles": detalles
            }
            self.pedidos_cola.append(pedido)
        return jsonify(resultado), status_code

    def procesar_pedido(self):
        
        if self.pedidos_cola:
            pedido = self.pedidos_cola.popleft()
            pedido_id = pedido.get("pedido_id")

            resultado, status_code = ModelPedido().actualizar_pedidoDB(
                pedido_id,
                pedido['total'],
                'procesado'
            )
            if status_code == 200:
                return jsonify({"message": "Pedido procesado", "pedido": pedido}), status_code
            else:
                self.pedidos_cola.appendleft(pedido)
                return jsonify(resultado), status_code
        else:
            return jsonify({"message": "No hay pedidos para procesar"}), 404

    def ver_siguiente_pedido(self):
        if self.pedidos_cola:
            siguiente_pedido = self.pedidos_cola[0]  
            return jsonify({"message": "Siguiente pedido en la cola", "pedido": siguiente_pedido}), 200
        else:
            return jsonify({"message": "No hay pedidos en la cola"}), 404

    def cancelar_pedido(self, pedido_id):
        for pedido in self.pedidos_cola:
            if pedido.get("pedido_id") == pedido_id:
                self.pedidos_cola.remove(pedido) 
                ModelPedido().actualizar_pedidoDB(pedido_id, pedido['total'], 'cancelado')
                return jsonify({"message": "Pedido cancelado", "pedido": pedido}), 200
        return jsonify({"message": "Pedido no encontrado"}), 404

    def actualizar_estado_pedido(self, pedido_id, nuevo_estado):
        for pedido in self.pedidos_cola:
            if pedido.get("pedido_id") == pedido_id:
                pedido['estado'] = nuevo_estado
                resultado, status_code = ModelPedido().actualizar_pedidoDB(
                    pedido_id,
                    pedido['total'],
                    nuevo_estado
                )
                return jsonify({"message": "Estado del pedido actualizado", "pedido": pedido}), status_code
        return jsonify({"message": "Pedido no encontrado"}), 404

    def mostrar_pedidos(self):
        self.pedidos_cola.clear()
        self.cargar_pedidos_desde_db()
        
        pedidos_list = list(self.pedidos_cola)
        if pedidos_list:
            return jsonify({"pedidos": pedidos_list}), 200
        else:
            return jsonify({"message": "No hay pedidos pendientes"}), 404
    
    def mostrar_todos_pedidos(self):
        self.cargar_todos_pedidos_desde_db()
        
        pedidos_list = list(self.pedidos_cola)
        if pedidos_list:
            return jsonify({"pedidos": pedidos_list}), 200
        else:
            return jsonify({"message": "No hay pedidos"}), 404
      
    def obtener_pedido(self, id):
            pedido = ModelPedido().obtener_pedidoDB(id)
            return pedido
    def eliminar_pedido(self, id):
        resultado = ModelPedido().eliminar_pedidoDB(id)
        return resultado