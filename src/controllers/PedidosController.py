from flask import request
from models.ModelPedido import ModelPedido

class PedidosController:
    def agregar_pedido(self):
        usuario_id = request.json.get('usuario_id')
        total = request.json.get('total')
        estado = request.json.get('estado')

        pedido = ModelPedido().agregar_pedidoDB(usuario_id, total, estado)
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
