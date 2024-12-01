import React from "react";

const OrderPage = () => {
  const productos = [
    { id: 1, nombre: "Producto 1", cantidad: 2, precio: 30.0 },
    { id: 2, nombre: "Producto 2", cantidad: 3, precio: 50.0 },
    { id: 3, nombre: "Producto 3", cantidad: 1, precio: 20.0 },
  ];

  const totalPagar = productos.reduce(
    (total, producto) => total + producto.cantidad * producto.precio,
    0
  );

  const handleRealizarPedido = () => {
    alert("Pedido realizado con éxito");
  };

  const handleCancelarPedido = () => {
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
            <i className="fas fa-shopping-cart text-xl"></i>
            <span className="absolute -top-2 -right-2 bg-red-500 text-white text-xs w-5 h-5 flex justify-center items-center rounded-full">
              2
            </span>
          </button>
          <button className="text-red-500 font-bold">Salir</button>
        </div>
      </header>

      {/* Contenido */}
      <main className="flex flex-1 p-4">
        {/* Lista de productos */}
        <section className="w-3/5 bg-white rounded-lg shadow-md p-4">
          <h2 className="text-lg font-bold mb-4">Productos</h2>
          <div className="space-y-4">
            {productos.map((producto) => (
              <div
                key={producto.id}
                className="flex items-center justify-between border p-4 rounded-md"
              >
                <div className="flex items-center space-x-4">
                  <div className="w-16 h-16 bg-gray-200 rounded-md"></div>
                  <div>
                    <h3 className="font-bold">{producto.nombre}</h3>
                    <p className="text-sm text-gray-500">Cantidad: {producto.cantidad}</p>
                  </div>
                </div>
                <p className="font-bold">
                  S/. {(producto.cantidad * producto.precio).toFixed(2)}
                </p>
              </div>
            ))}
          </div>
        </section>

        {/* Resumen del pedido */}
        <aside className="w-2/5 bg-white rounded-lg shadow-md p-4 ml-4">
          <h2 className="text-lg font-bold mb-4">Resumen del pedido</h2>
          <div className="space-y-2">
            <p className="text-sm">
              <span className="font-bold">Total a pagar:</span> S/.{" "}
              {totalPagar.toFixed(2)}
            </p>
            <p className="text-sm">
              <span className="font-bold">Prioridad:</span> Alta
            </p>
            <p className="text-sm">
              <span className="font-bold">Fecha y hora:</span> {new Date().toLocaleString()}
            </p>
            <p className="text-sm">
              <span className="font-bold">Usuario:</span> Usuario123
            </p>
          </div>
          <div className="flex space-x-4 mt-4">
            <button
              onClick={handleRealizarPedido}
              className="flex-1 bg-green-500 text-white py-2 rounded-md hover:bg-green-600"
            >
              Realizar pedido
            </button>
            <button
              onClick={handleCancelarPedido}
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

export default OrderPage;
