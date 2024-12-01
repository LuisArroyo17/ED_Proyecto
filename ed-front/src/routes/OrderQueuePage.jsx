import React, { useState } from "react";

const OrderQueuePage = () => {
  // Datos simulados para la cola de pedidos
  const [orders, setOrders] = useState([
    { id: 1, estado: "Pendiente", prioridad: 1 },
    { id: 2, estado: "En proceso", prioridad: 2 },
    { id: 3, estado: "Pendiente", prioridad: 2 },
  ]);

  // Simulación del próximo pedido
  const [currentOrder, setCurrentOrder] = useState({
    id: 1,
    valor: 717.0,
    prioridad: "Alta",
    fecha: new Date().toLocaleString(),
    usuario: "Usuario123",
  });

  const handleProcessOrder = () => {
    alert("Pedido procesado exitosamente");
  };

  const handleCancelOrder = () => {
    alert("Pedido cancelado");
  };

  return (
    <div className="min-h-screen bg-gray-100 flex flex-col">
      {/* Encabezado */}
      <header className="flex justify-between items-center bg-white shadow-md p-4">
        <div className="flex items-center space-x-4">
          <button className="text-xl">
            <i className="fas fa-bars"></i>
          </button>
          <h1 className="text-2xl font-bold">Realizar pedido</h1>
        </div>
        <div className="flex items-center space-x-4">
          <button className="relative">
            <i className="fas fa-clock text-xl"></i>
          </button>
          <button className="text-red-500 font-bold">Salir</button>
        </div>
      </header>

      {/* Contenido principal */}
      <main className="flex flex-1 p-4">
        {/* Cola de pedidos */}
        <section className="w-1/2 bg-white rounded-lg shadow-md p-4">
          <h2 className="text-lg font-bold mb-4">Cola de pedidos</h2>
          <div className="space-y-4">
            {orders.map((order) => (
              <div
                key={order.id}
                className="flex justify-between items-center border p-4 rounded-md"
              >
                <div>
                  <p className="font-bold">ID del pedido: {order.id}</p>
                  <p className="text-sm text-gray-500">Estado: {order.estado}</p>
                  <p className="text-sm text-gray-500">
                    Prioridad: {order.prioridad}
                  </p>
                </div>
                <div className="w-16 h-16 bg-gray-200 rounded-md"></div>
              </div>
            ))}
          </div>
        </section>

        {/* Detalles del próximo pedido */}
        <aside className="w-1/2 bg-white rounded-lg shadow-md p-4 ml-4">
          <h2 className="text-lg font-bold mb-4">Próximo pedido en cola</h2>
          <div className="space-y-2">
            <p className="text-sm">
              <span className="font-bold">ID del pedido:</span> {currentOrder.id}
            </p>
            <p className="text-sm">
              <span className="font-bold">Valor del pedido:</span> S/.{" "}
              {currentOrder.valor.toFixed(2)}
            </p>
            <p className="text-sm">
              <span className="font-bold">Prioridad:</span> {currentOrder.prioridad}
            </p>
            <p className="text-sm">
              <span className="font-bold">Fecha y hora:</span> {currentOrder.fecha}
            </p>
            <p className="text-sm">
              <span className="font-bold">Usuario:</span> {currentOrder.usuario}
            </p>
          </div>
          <div className="flex space-x-4 mt-4">
            <button
              onClick={handleProcessOrder}
              className="flex-1 bg-green-500 text-white py-2 rounded-md hover:bg-green-600"
            >
              Procesar pedido
            </button>
            <button
              onClick={handleCancelOrder}
              className="flex-1 bg-red-500 text-white py-2 rounded-md hover:bg-red-600"
            >
              Cancelar
            </button>
          </div>
        </aside>
      </main>
    </div>
  );
};

export default OrderQueuePage;
