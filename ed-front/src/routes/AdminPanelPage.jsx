import React from "react";

const AdminPanelPage = () => {
  const handleNavigation = (route) => {
    window.location.href = route; // Redirige a la ruta correspondiente
  };

  return (
    <div className="min-h-screen bg-gray-100 flex flex-col">
      {/* Encabezado */}
      <header className="flex justify-between items-center bg-white shadow-md p-4">
        <div className="flex items-center space-x-4">
          <button className="text-xl">
            <i className="fas fa-bars"></i>
          </button>
          <h1 className="text-2xl font-bold">Panel Admin</h1>
        </div>
        <div className="flex items-center space-x-4">
          <button className="text-red-500 font-bold">Salir</button>
        </div>
      </header>

      {/* Contenido principal */}
      <main className="flex flex-1 justify-center items-center p-4">
        <div className="grid grid-cols-3 gap-8">
          {/* Gestionar Productos */}
          <div className="bg-white rounded-lg shadow-md p-6 text-center">
            <h2 className="text-lg font-bold mb-4">Gestionar Productos</h2>
            <p className="text-sm text-gray-500 mb-6">Administrar productos en el sistema</p>
            <button
              onClick={() => handleNavigation("/gestionar-productos")}
              className="bg-green-500 text-white px-4 py-2 rounded-md hover:bg-green-600"
            >
              Gestionar
            </button>
          </div>

          {/* Gestionar Envíos */}
          <div className="bg-white rounded-lg shadow-md p-6 text-center">
            <h2 className="text-lg font-bold mb-4">Gestionar Envíos</h2>
            <p className="text-sm text-gray-500 mb-6">Administrar envíos pendientes</p>
            <button
              onClick={() => handleNavigation("/gestionar-envios")}
              className="bg-green-500 text-white px-4 py-2 rounded-md hover:bg-green-600"
            >
              Gestionar
            </button>
          </div>

          {/* Gestionar Pedidos */}
          <div className="bg-white rounded-lg shadow-md p-6 text-center">
            <h2 className="text-lg font-bold mb-4">Gestionar Pedidos</h2>
            <p className="text-sm text-gray-500 mb-6">Revisar y administrar pedidos</p>
            <button
              onClick={() => handleNavigation("/gestionar-pedidos")}
              className="bg-green-500 text-white px-4 py-2 rounded-md hover:bg-green-600"
            >
              Gestionar
            </button>
          </div>
        </div>
      </main>
    </div>
  );
};

export default AdminPanelPage;
