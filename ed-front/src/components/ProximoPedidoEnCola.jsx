import React from 'react';

const ProximoPedidoEnCola = ({ pedido, onProcesar, onCancelar }) => {
  if (!pedido) return null; // Si no hay pedido, no mostrar el componente

  return (
    <aside className="w-1/2 bg-white rounded-lg shadow-md p-4 ml-4">
      <h2 className="text-lg font-bold mb-4">Próximo pedido en cola</h2>
      <div className="space-y-2">
        <p className="text-sm">
          <span className="font-bold">ID del pedido:</span> {pedido.pedido_id}
        </p>
        <p className="text-sm">
          <span className="font-bold">Valor del pedido:</span> S/. {pedido.total.toFixed(2)}
        </p>
        <p className="text-sm">
          <span className="font-bold">Prioridad:</span> {pedido.prioridad}
        </p>
        <p className="text-sm">
          <span className="font-bold">Fecha y hora:</span> {pedido.fecha}
        </p>
        <p className="text-sm">
          <span className="font-bold">Usuario:</span> {pedido.usuario_id}
        </p>
      </div>
      <div className="flex space-x-4 mt-4">
        <button
          onClick={onProcesar}
          disabled={!pedido} // Deshabilitar el botón si no hay pedido
          className="flex-1 bg-green-500 text-white py-2 rounded-md hover:bg-green-600 disabled:bg-gray-300"
        >
          Procesar pedido
        </button>
        <button
          onClick={onCancelar}
          disabled={!pedido} // Deshabilitar el botón si no hay pedido
          className="flex-1 bg-red-500 text-white py-2 rounded-md hover:bg-red-600 disabled:bg-gray-300"
        >
          Cancelar
        </button>
      </div>
    </aside>
  );
};

export default ProximoPedidoEnCola;
