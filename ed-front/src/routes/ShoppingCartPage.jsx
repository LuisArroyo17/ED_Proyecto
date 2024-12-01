import React, { useState } from "react";

const ShoppingCartPage = () => {
  // Datos simulados de productos en el carrito
  const [cart, setCart] = useState([
    { id: 1, nombre: "Producto 1", cantidad: 2, precio: 599.0 },
    { id: 2, nombre: "Producto 2", cantidad: 3, precio: 49.0 },
    { id: 3, nombre: "Producto 3", cantidad: 1, precio: 69.0 },
  ]);

  // Calcular total a pagar
  const totalPagar = cart.reduce(
    (total, producto) => total + producto.cantidad * producto.precio,
    0
  );

  const handleRemoveItem = (id) => {
    const updatedCart = cart.filter((item) => item.id !== id);
    setCart(updatedCart);
  };

  const handleCheckout = () => {
    alert("Compra realizada con éxito");
  };

  return (
    <div className="min-h-screen bg-gray-100 flex flex-col">
      {/* Encabezado */}
      <header className="flex justify-between items-center bg-white shadow-md p-4">
        <div className="flex items-center space-x-4">
          <button className="text-xl">
            <i className="fas fa-bars"></i>
          </button>
          <h1 className="text-2xl font-bold">Mi carrito</h1>
        </div>
        <div className="flex items-center space-x-4">
          <button className="relative">
            <i className="fas fa-shopping-cart text-xl"></i>
            <span className="absolute -top-2 -right-2 bg-red-500 text-white text-xs w-5 h-5 flex justify-center items-center rounded-full">
              {cart.length}
            </span>
          </button>
          <button className="text-red-500 font-bold">Salir</button>
        </div>
      </header>

      {/* Contenido principal */}
      <main className="flex flex-1 p-4">
        {/* Lista de productos */}
        <section className="w-2/3 bg-white rounded-lg shadow-md p-4">
          <h2 className="text-lg font-bold mb-4">Productos</h2>
          <div className="space-y-4">
            {cart.map((producto) => (
              <div
                key={producto.id}
                className="flex justify-between items-center border p-4 rounded-md"
              >
                <div className="flex items-center space-x-4">
                  <div className="w-16 h-16 bg-gray-200 rounded-md"></div>
                  <div>
                    <h3 className="font-bold">{producto.nombre}</h3>
                    <p className="text-sm text-gray-500">
                      Cantidad: {producto.cantidad}
                    </p>
                  </div>
                </div>
                <p className="font-bold">
                  S/. {(producto.cantidad * producto.precio).toFixed(2)}
                </p>
                <button
                  onClick={() => handleRemoveItem(producto.id)}
                  className="text-red-500 text-sm hover:underline"
                >
                  Eliminar
                </button>
              </div>
            ))}
          </div>
        </section>

        {/* Resumen de compra */}
        <aside className="w-1/3 bg-white rounded-lg shadow-md p-4 ml-4">
          <h2 className="text-lg font-bold mb-4">Resumen de compra</h2>
          <div className="space-y-2">
            {cart.map((producto) => (
              <p key={producto.id} className="text-sm">
                <span className="font-bold">{producto.nombre}:</span>{" "}
                S/. {(producto.cantidad * producto.precio).toFixed(2)}
              </p>
            ))}
          </div>
          <hr className="my-4" />
          <p className="text-sm font-bold">
            Total a pagar: S/. {totalPagar.toFixed(2)}
          </p>
          <button
            onClick={handleCheckout}
            className="mt-4 w-full bg-green-500 text-white py-2 rounded-md hover:bg-green-600"
          >
            Comprar
          </button>
        </aside>
      </main>
    </div>
  );
};

export default ShoppingCartPage;
