import React from "react";

const OrderSuccessPage = () => {
  const handleViewOrder = () => {
    // Redirigir a la página de seguimiento/envío
    window.location.href = "/envio";
  };

  return (
    <div className="min-h-screen bg-gray-100 flex flex-col items-center">
      {/* Encabezado */}
      <header className="flex justify-between items-center w-full bg-white shadow-md p-4">
        <div className="flex items-center space-x-4">
          <button className="text-xl">
            <i className="fas fa-bars"></i>
          </button>
          <h1 className="text-2xl font-bold">Pedido realizado</h1>
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

      {/* Contenido principal */}
      <main className="flex flex-col items-center justify-center flex-1">
        <div className="bg-white rounded-lg shadow-md p-8 text-center">
          <h2 className="text-xl font-bold mb-4">Pedido realizado con éxito</h2>
          <div className="mb-6">
            <div className="w-24 h-24 mx-auto bg-gray-200 rounded-full flex items-center justify-center">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                className="h-16 w-16 text-green-500"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
                strokeWidth={2}
              >
                <path
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  d="M9 12l2 2 4-4m-7 8a9 9 0 100-18 9 9 0 000 18z"
                />
              </svg>
            </div>
          </div>
          <button
            onClick={handleViewOrder}
            className="bg-green-500 text-white px-6 py-2 rounded-md hover:bg-green-600"
          >
            Ver envío
          </button>
        </div>
      </main>
    </div>
  );
};

export default OrderSuccessPage;
