import heapq
from flask import request, jsonify
from collections import deque
from models.ModelEnvio import ModelEnvios

class EnviosController:
    def __init__(self):
        self.envios_cola = deque()
        self.envios_heap = []
        # Cargar envíos al inicializar el controlador
        self.cargar_todos_envios_desde_db()
            
    def agregar_envio_con_prioridad(self, envio_id, prioridad):
        heapq.heappush(self.envios_heap, (-prioridad, envio_id))
    
    def obtener_envio_con_mayor_prioridad(self):
        if self.envios_heap:
            prioridad, envio_id = self.envios_heap[0]
            return {
                "envio_id": envio_id,
                "prioridad": -prioridad 
            }
        else:
            return {"message": "No hay envios en el heap"}

    def mostrar_todos_los_envios_priorizados(self):
        # Asegurarse de cargar los envíos desde la base de datos antes de mostrar
        self.cargar_todos_envios_desde_db()
        
        if not self.envios_heap:
            return []

        envios_priorizados = sorted(
            [(-prioridad, envio_id) for prioridad, envio_id in self.envios_heap],
            reverse=True
        )
        return [{"envio_id": eid, "prioridad": prioridad} for prioridad, eid in envios_priorizados]
    
    def extraer_envio_con_mayor_prioridad(self):
        if self.envios_heap:
            prioridad, envio_id = heapq.heappop(self.envios_heap)
            return {
                "envio_id": envio_id,
                "prioridad": -prioridad  
            }
        else:
            return {"message": "No hay envios en el heap"}
      
    def cargar_todos_envios_desde_db(self):
        self.envios_cola.clear()
        self.envios_heap.clear()  # Asegurarse de limpiar el heap también
        envios, status_code = ModelEnvios().obtener_todos_envios()
        
        if status_code == 200:
            for envio in envios:
                envio_dict = {
                    "envio_id": envio["id"],
                    "pedido_id": envio["pedido_id"],
                    "detalles": envio["detalles"],
                    "prioridad": envio["prioridad"],
                    "estado": envio["estado"]
                }
                if not any(e["envio_id"] == envio_dict["envio_id"] for e in self.envios_cola):
                    self.envios_cola.append(envio_dict)
                    self.agregar_envio_con_prioridad(envio_dict["envio_id"], envio_dict["prioridad"])  # Agregar al heap

                        
    def cargar_envios_desde_db(self):
        self.envios_cola.clear()
        self.envios_heap.clear()  # Asegurarse de limpiar el heap también
        envios, status_code = ModelEnvios().obtener_envios_pendientes()
        
        if status_code == 200:
            for envio in envios:
                envio_dict = {
                    "envio_id": envio["id"],
                    "pedido_id": envio["pedido_id"],
                    "detalles": envio["detalles"],
                    "prioridad": envio["prioridad"],
                    "estado": envio["estado"]
                }
                
                if not any(e["envio_id"] == envio_dict["envio_id"] for e in self.envios_cola):
                    self.envios_cola.append(envio_dict)
                    self.agregar_envio_con_prioridad(envio_dict["envio_id"], envio_dict["prioridad"])  # Agregar al heap

                        
    def agregar_envio(self):
        pedido_id = request.json.get('pedido_id')
        detalles = request.json.get('detalles', '')
        prioridad = request.json.get('prioridad', 1)  # Eliminada la línea duplicada
        estado = 'pendiente'

        resultado, status_code = ModelEnvios().agregar_envioDB(pedido_id, detalles, prioridad, estado)
        if status_code == 201:
            envio = {
                "envio_id": resultado['data']['envio_id'],
                "pedido_id": pedido_id,
                "detalles": detalles,
                "prioridad": prioridad,
                "estado": estado
            }
            # Agregar al heap de prioridad
            self.agregar_envio_con_prioridad(envio['envio_id'], prioridad)
        
            # Agregar a la cola
            self.envios_cola.append(envio)
        return jsonify(resultado), status_code

    def enviar_envio(self):
        if self.envios_cola:
            envio = self.envios_cola.popleft()
            envio_id = envio.get("envio_id")

            resultado, status_code = ModelEnvios().actualizar_estadoDB(
                envio_id,
                'en camino'
            )
            if status_code == 200:
                return jsonify({"message": "Envio en camino", "envio": envio}), status_code
            else:
                self.envios_cola.appendleft(envio)
                return jsonify(resultado), status_code
        else:
            return jsonify({"message": "No hay envios para enviar"}), 404


    def ver_siguiente_envio(self):
        if self.envios_cola:
            siguiente_envio = self.envios_cola[0]  
            return jsonify({"message": "Siguiente envio en la cola", "envio": siguiente_envio}), 200
        else:
            return jsonify({"message": "No hay envios en la cola"}), 404
    
    def cancelar_envio(self, envio_id):
        for envio in self.envios_cola:
            if envio.get('envio_id') == int(envio_id):
                resultado, status_code = ModelEnvios().actualizar_estadoDB(envio_id, 'Cancelado')
                if status_code == 200:
                    self.envios_cola.remove(envio)  # Eliminar el envío de la cola
                    # También eliminar del heap
                    self.envios_heap = [item for item in self.envios_heap if item[1] != envio_id]
                    heapq.heapify(self.envios_heap)
                    return jsonify({"message": "Envio Cancelado", "envio": envio}), 200
                else:
                    return jsonify(resultado), status_code

        return jsonify({"message": "Envio no encontrado"}), 404


    def actualizar_estado_envio(self, envio_id, nuevo_estado):
        for envio in self.envios_cola:
            if envio.get("envio_id") == envio_id:
                envio['estado'] = nuevo_estado
                resultado, status_code = ModelEnvios().actualizar_estadoDB(
                    envio_id,
                    nuevo_estado
                )
                return jsonify({"message": "Estado del envio actualizado", "envio": envio}), status_code
        return jsonify({"message": "Envio no encontrado"}), 404

    def mostrar_envios(self):
        self.envios_cola.clear()
        self.cargar_envios_desde_db()
        
        envios_list = list(self.envios_cola)
        if envios_list:
            return jsonify({"envios": envios_list}), 200
        else:
            return jsonify({"message": "No hay envios pendientes"}), 404
    
    def mostrar_todos_envios(self):
        self.cargar_todos_envios_desde_db()
        
        envios_list = list(self.envios_cola)
        if envios_list:
            return jsonify({"envios": envios_list}), 200
        else:
            return jsonify({"message": "No hay envios"}), 404
        
    def obtener_envio_id(self, envio_id):
        resultado = ModelEnvios().obtener_envio_por_id(envio_id)
        return jsonify({"envio": resultado}), 200
        
    def enviar_envio_con_mayor_prioridad(self):
        if self.envios_heap:
            envio_con_prioridad = self.extraer_envio_con_mayor_prioridad()  # Extraemos el envío con mayor prioridad
            if "envio_id" in envio_con_prioridad:
                envio_id = envio_con_prioridad["envio_id"]
                # Reutilizamos la lógica de enviar_envio
                envio = next((e for e in self.envios_cola if e["envio_id"] == envio_id), None)
                if envio:
                    self.envios_cola.remove(envio)
                    resultado, status_code = ModelEnvios().actualizar_estadoDB(envio_id, 'en camino')
                    if status_code == 200:
                        return jsonify({"message": "Envio con mayor prioridad en camino", "envio": envio}), status_code
                    else:
                        # Volver a agregar al heap en caso de error
                        self.agregar_envio_con_prioridad(envio_id, envio_con_prioridad["prioridad"])
                        return jsonify(resultado), status_code
                else:
                    return jsonify({"message": "Envio no encontrado en la cola"}), 404
            else:
                return jsonify(envio_con_prioridad), 404  # No hay envíos en el heap
        else:
            return jsonify({"message": "No hay envios en el heap"}), 404
        

    # Obtener todos los envíos de un usuario
    def obtener_envios_por_usuario(self, usuario_id):
        envios, status_code = ModelEnvios().obtener_envio_por_usuario(usuario_id)
        if status_code == 200:
            return jsonify({"envios": envios}), 200
        return jsonify(envios), status_code

    # Obtener los envíos de un usuario por estado
    def obtener_envios_por_estado(self, usuario_id, estado):
        envios, status_code = ModelEnvios().obtener_envios_por_estado(usuario_id, estado)
        if status_code == 200:
            return jsonify({"envios": envios}), 200
        return jsonify(envios), status_code
