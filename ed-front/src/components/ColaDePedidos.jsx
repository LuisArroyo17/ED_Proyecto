import React from 'react';

const ColaDePedidos = ({ pedidos }) => {
  return (
    <section className="w-full bg-white rounded-lg shadow-md p-4">
      <h2 className="text-lg font-bold mb-4">Cola de pedidos</h2>
      <div className="space-y-4">
        {pedidos.map((pedido) => (
          <div
            key={pedido.pedido_id}
            className={`flex justify-between items-center border p-4 rounded-md ${
              pedido.estado === 'Procesado'
                ? 'bg-green-100'
                : pedido.estado === 'Cancelado'
                ? 'bg-red-100'
                : 'bg-white-100'
            }`}
          >
            <div>
              <p className="font-bold">ID del pedido: {pedido.pedido_id}</p>
              <p className="text-sm text-gray-500">Estado: {pedido.estado}</p>
              <p className="text-sm text-gray-500">Prioridad: {pedido.prioridad}</p>
            </div>
            <div className="w-16 h-16 bg-gray-200 rounded-md"></div>
          </div>
        ))}
      </div>
    </section>
  );
};

export default ColaDePedidos;
