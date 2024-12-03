import React from "react";
import { HeaderClient } from "../components/HeaderClient";
import comprobado from '../assets/comprobado.png';
const OrderSuccessPage = () => {
  const handleViewOrder = () => {
    // Redirigir a la página de seguimiento/envío
    // window.location.href = "/envio";
  };

  return (
    <div className="min-h-screen bg-gray-100 flex flex-col">
      {/* Encabezado */}
      <HeaderClient/>

      {/* Contenido principal */}
      <main className="flex flex-col items-center justify-center flex-1">
        <div className="bg-white rounded-lg shadow-md p-8 text-center">
          <h2 className="text-xl font-bold mb-4">Pedido realizado con éxito</h2>
          <div className="mb-6">
            <div className="w-24 h-24 mx-auto bg-gray-200 rounded-full flex items-center justify-center">
            <img src={comprobado} alt="comprobado" className="h-15 w-15 mr-10 -mt-1 ml-10"/>
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
