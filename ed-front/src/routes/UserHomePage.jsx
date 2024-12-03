import React from "react";
import { useUser } from "../context/UserContext";
import { useNavigate } from "react-router-dom";
import { HeaderClient } from "../components/HeaderClient";
const UserHomePage = () => {
  const { userId } = useUser();
  console.log("ID del usuario:", userId);
  const navigate = useNavigate();
  
  const redirigir = () => {
    navigate("/realizarPedido");
  };
  
  return (
    <>
     <HeaderClient/>
    <div className="min-h-screen bg-gray-100 flex">
      {/* Menú lateral */}
      <aside className="w-1/4 bg-white shadow-md p-4">
        <h2 className="text-lg font-bold mb-4">Menú de opciones</h2>
        <ul className="space-y-2">
          <li className="p-2 bg-gray-200 rounded-md cursor-pointer hover:bg-gray-300">Categorías</li>
          <li className="p-2 rounded-md cursor-pointer hover:bg-gray-300">Tecnología</li>
          <li className="p-2 rounded-md cursor-pointer hover:bg-gray-300">Hogar</li>
          <li className="p-2 rounded-md cursor-pointer hover:bg-gray-300">Línea blanca</li>
          <li className="p-2 rounded-md cursor-pointer hover:bg-gray-300">Moda Hombre</li>
          <li className="p-2 rounded-md cursor-pointer hover:bg-gray-300">Moda Mujer</li>
          <li className="p-2 rounded-md cursor-pointer hover:bg-gray-300">Dormitorio</li>
          <li className="p-2 rounded-md cursor-pointer hover:bg-gray-300">Muebles</li>
          <li className="p-2 rounded-md cursor-pointer hover:bg-gray-300">Deportes</li>
        </ul>
      </aside>

      {/* Contenido principal */}
      <main className="flex-1 p-4">

        {/* Barra de búsqueda */}
        <div className="mb-4">
          <input
            type="text"
            placeholder="Ingresa el nombre del producto"
            className="w-3/4 p-2 border border-gray-300 rounded-md"
          />
          <button className="p-2 bg-blue-500 text-white rounded-md ml-2">
            <i className="fas fa-search"></i>
          </button>
        </div>

        {/* Productos destacados */}
        <section>
          <h2 className="text-lg font-bold mb-4">Lo Más Buscado</h2>
          <div className="grid grid-cols-3 gap-4">
            <div className="bg-white shadow-md rounded-md p-4">
              <div className="h-32 bg-gray-200 rounded-md mb-2"></div>
              <h3 className="text-sm font-bold">Nombre del producto</h3>
              <p className="text-sm text-gray-500">S/. 30.00</p>
              <button
                className="mt-2 p-2 bg-blue-500 text-white rounded-md w-full"
                onClick={redirigir}
              >
                Ver detalles
              </button>
            </div>
            <div className="bg-white shadow-md rounded-md p-4">
              <div className="h-32 bg-gray-200 rounded-md mb-2"></div>
              <h3 className="text-sm font-bold">Nombre del producto</h3>
              <p className="text-sm text-gray-500">S/. 30.00</p>
              <button className="mt-2 p-2 bg-blue-500 text-white rounded-md w-full">
                Ver detalles
              </button>
            </div>
            <div className="bg-white shadow-md rounded-md p-4">
              <div className="h-32 bg-gray-200 rounded-md mb-2"></div>
              <h3 className="text-sm font-bold">Nombre del producto</h3>
              <p className="text-sm text-gray-500">S/. 30.00</p>
              <button className="mt-2 p-2 bg-blue-500 text-white rounded-md w-full">
                Ver detalles
              </button>
            </div>
          </div>
        </section>
      </main>
    </div>
    </>
  );
};

export default UserHomePage;
