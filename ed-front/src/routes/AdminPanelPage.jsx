import React from "react";
import logo from '../assets/casa-silueta-negra-sin-puerta.png';
import logo1 from '../assets/menu.png';
import linea from '../assets/linea.png';
import envios from '../assets/envios.jpg';  
import caja from '../assets/caja.jpg';
import pedidos from '../assets/pedidos.jpg';
import {useNavigate} from "react-router-dom";

const AdminPanelPage = () => {
  const navigate = useNavigate(); //HOOk
  

  return (
    <div className="min-h-screen bg-gray-100 flex flex-col">
      {/* Encabezado */}
      <header className="flex justify-between items-center bg-yellow-300 shadow-md p-2">
        <div className="flex items-center -space-x-0">
        <button >
          <img src={logo} alt="Logo" className="h-8 w-8 ml-1" onClick={() => navigate(0)}/>
          </button>
          <img src={linea} alt="linea" className="h-8 w-8 " />
          <button>
          <img src={logo1} alt="Logo" className="h-8 w-8 -ml-0 mt-1"/>
          </button>
        </div>  
        <div className="flex items-center">
        <button className="absolute text-red-500 font-bold right-3 top-4"  onClick={() => navigate("/")}>Salir</button>
        </div>
      </header>

      <h1 className="absolute text-2xl font-bold inset-0 m-auto w-max h-max mt-24">
       PANEL ADMINISTRATIVO
      </h1>
      {/* Contenido principal */}
      <main className="flex flex-1 justify-center items-center p-4">
        <div className="grid grid-cols-3 gap-8">
          {/* Gestionar Productos */}
          <div className="bg-white rounded-lg shadow-md p-6 text-center">
          <img
                      src={pedidos}
                      alt={pedidos}
                      className="w-32 h-32 object-cover rounded-md ml-10"
                    />
            <h2 className="text-lg font-bold mb-4">Gestionar Productos</h2>
            <p className="text-sm text-gray-500 mb-6">Administrar productos en el sistema</p>
            <button
              onClick={() => navigate("/admin")}
              className="bg-green-500 text-white px-4 py-2 rounded-md hover:bg-green-600"
            >
              Gestionar
            </button>
          </div>

          {/* Gestionar Envíos */}
          <div className="bg-white rounded-lg shadow-md p-6 text-center">
          <img
                      src={envios}
                      alt={envios}
                      className="w-32 h-32 object-cover rounded-md ml-10"
                    />
            <h2 className="text-lg font-bold mb-4">Gestionar Envíos</h2>
            <p className="text-sm text-gray-500 mb-6">Administrar envíos pendientes</p>
            <button
              onClick={() => navigate("/gestionar-envios")}
              className="bg-green-500 text-white px-4 py-2 rounded-md hover:bg-green-600"
            >
              Gestionar
            </button>
          </div>

          {/* Gestionar Pedidos */}
          <div className="bg-white rounded-lg shadow-md p-6 text-center">
          <img
                      src={caja}
                      alt={caja}
                      className="w-32 h-32 object-cover rounded-md ml-10"
                    />
            <h2 className="text-lg font-bold mb-4">Gestionar Pedidos</h2>
            <p className="text-sm text-gray-500 mb-6">Revisar y administrar pedidos</p>
            <button
              onClick={() => navigate("/pedidoGestion")}
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
