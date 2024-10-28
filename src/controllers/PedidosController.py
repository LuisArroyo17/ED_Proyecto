from flask import request, jsonify
from collections import deque
from models.ModelPedido import ModelPedido
from decimal import Decimal

class PedidosController:
    def __init__(self):
        # Inicializamos una cola en memoria para gestionar los pedidos en FIFO
        self.pedidos_cola = deque()
        
    def cargar_pedidos_desde_db(self):
        # Llamar a obtener_pedidos_pendientes para cargar pedidos pendientes de la base de datos
        pedidos, status_code = ModelPedido().obtener_pedidos_pendientes()
        
        if status_code == 200:
            for pedido in pedidos:
                # Convertir cada pedido a un diccionario con datos JSON-compatibles
                pedido_dict = {
                    "pedido_id": pedido["id"],
                    "usuario_id": pedido["usuario_id"],
                    "fecha": str(pedido["fecha"]),  # Convertir datetime a string
                    "total": float(pedido["total"]) if isinstance(pedido["total"], Decimal) else pedido["total"],  # Convertir Decimal a float
                    "estado": pedido["estado"]
                }
                # Agregar el pedido a la cola en memoria si no está duplicado
                if not any(p["pedido_id"] == pedido_dict["pedido_id"] for p in self.pedidos_cola):
                    self.pedidos_cola.append(pedido_dict)
                        
    def agregar_pedido(self):
        usuario_id = request.json.get('usuario_id')
        total = request.json.get('total')
        estado = request.json.get('estado', 'pendiente')
        detalles = request.json.get('detalles', [])

        # Enviar los detalles a agregar_pedidoDB
        resultado, status_code = ModelPedido().agregar_pedidoDB(usuario_id, total, estado, detalles)
        if status_code == 201:
            # Si se agregó correctamente a la DB, también agregamos el pedido a la cola en memoria
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
        # Procesar el pedido al frente de la cola (FIFO)
        if self.pedidos_cola:
            pedido = self.pedidos_cola.popleft()  # Retira el pedido más antiguo de la cola
            pedido_id = pedido.get("pedido_id")

            # Cambiar el estado en la base de datos a 'procesado'
            resultado, status_code = ModelPedido().actualizar_pedidoDB(
                pedido_id,
                pedido['total'],
                'procesado'
            )
            if status_code == 200:
                return jsonify({"message": "Pedido procesado", "pedido": pedido}), status_code
            else:
                # Si hubo un error al actualizar en la DB, devolver el pedido a la cola
                self.pedidos_cola.appendleft(pedido)
                return jsonify(resultado), status_code
        else:
            return jsonify({"message": "No hay pedidos para procesar"}), 404

    def ver_siguiente_pedido(self):
        # Muestra el pedido al frente de la cola sin procesarlo
        if self.pedidos_cola:
            siguiente_pedido = self.pedidos_cola[0]  # Accede al primer elemento
            return jsonify({"message": "Siguiente pedido en la cola", "pedido": siguiente_pedido}), 200
        else:
            return jsonify({"message": "No hay pedidos en la cola"}), 404

    def cancelar_pedido(self, pedido_id):
        # Buscar el pedido en la cola y eliminarlo
        for pedido in self.pedidos_cola:
            if pedido.get("pedido_id") == pedido_id:
                self.pedidos_cola.remove(pedido)  # Eliminar de la cola en memoria
                # Actualizar en la base de datos si es necesario
                ModelPedido().actualizar_pedidoDB(pedido_id, pedido['total'], 'cancelado')
                return jsonify({"message": "Pedido cancelado", "pedido": pedido}), 200
        return jsonify({"message": "Pedido no encontrado"}), 404

    def actualizar_estado_pedido(self, pedido_id, nuevo_estado):
        # Buscar el pedido en la cola y actualizar su estado
        for pedido in self.pedidos_cola:
            if pedido.get("pedido_id") == pedido_id:
                pedido['estado'] = nuevo_estado
                # Actualizar en la base de datos
                resultado, status_code = ModelPedido().actualizar_pedidoDB(
                    pedido_id,
                    pedido['total'],
                    nuevo_estado
                )
                return jsonify({"message": "Estado del pedido actualizado", "pedido": pedido}), status_code
        return jsonify({"message": "Pedido no encontrado"}), 404

    def mostrar_pedidos(self):
        # Cargar pedidos desde la base de datos en la cola en memoria antes de mostrarlos
        self.cargar_pedidos_desde_db()
        
        # Convertir la cola en memoria a una lista para mostrarla en JSON
        pedidos_list = list(self.pedidos_cola)
        if pedidos_list:
            return jsonify({"pedidos": pedidos_list}), 200
        else:
            return jsonify({"message": "No hay pedidos pendientes"}), 404
        
    def obtener_pedido(self, id):
            pedido = ModelPedido().obtener_pedidoDB(id)
            return pedido
    def eliminar_pedido(self, id):
        resultado = ModelPedido().eliminar_pedidoDB(id)
        return resultado