from flask import request, jsonify
from models.ModelPedido import ModelPedido
from models.ModelEnvio import ModelEnvio  # Importar ModelEnvio para la gestión de envíos

class PedidosController:
    def agregar_pedido(self):
        usuario_id = request.json.get('usuario_id')
        total = request.json.get('total')
        estado = request.json.get('estado', 'pendiente')

        # Crear el pedido en la base de datos
        pedido = ModelPedido().agregar_pedidoDB(usuario_id, total, estado)
        
        # Determinar la prioridad del envío
        prioridad = 1 if total > 89.00 else 0  # 1 = urgente, 0 = no urgente

        # Crear el envío asociado al pedido con la prioridad determinada
        if pedido and pedido[1] == 201:  # Asegurarse de que el pedido se agregó con éxito
            pedido_id = pedido[0]["data"]["pedido_id"]
            ModelEnvio().agregar_envioDB(pedido_id, "Detalles del envío", prioridad)

        return pedido

    def obtener_pedido(self, id):
        pedido = ModelPedido().obtener_pedidoDB(id)
        return pedido

    def actualizar_pedido(self, id):
        total = request.json.get('total')
        estado = request.json.get('estado')
        pedido = ModelPedido().actualizar_pedidoDB(id, total, estado)
        return pedido

    def eliminar_pedido(self, id):
        resultado = ModelPedido().eliminar_pedidoDB(id)
        return resultado
