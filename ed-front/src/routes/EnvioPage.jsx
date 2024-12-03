import React, { useState, useEffect } from 'react'; 
import { useNavigate } from 'react-router-dom'; 
import { useUser } from "../context/UserContext";

const EnvioPage = () => {
  const { userId } = useUser();  // Obtener el userId del contexto
  const [envios, setEnvios] = useState([]); // Estado para almacenar los envíos del usuario
  const navigate = useNavigate();

  useEffect(() => {
    const obtenerEnvios = async () => {
      try {
        // 1. Obtener los pedidos del usuario
        const pedidosResponse = await fetch(`http://localhost:5000/pedidos?usuario_id=${userId}`);
        const pedidosData = await pedidosResponse.json();

        if (pedidosData.length > 0) {
          // 2. Obtener los envíos asociados a esos pedidos
          const pedidosIds = pedidosData.map(pedido => pedido.pedido_id); // Extraemos los IDs de los pedidos
          const enviosResponse = await fetch(`http://localhost:5000/envios?pedido_id_in=${pedidosIds.join(',')}`);
          const enviosData = await enviosResponse.json();
          setEnvios(enviosData); // Guardamos los envíos asociados a los pedidos
        } else {
          setEnvios([]); // Si no hay pedidos, no hay envíos asociados
        }
      } catch (error) {
        console.error("Error al cargar los envíos:", error);
      }
    };

    obtenerEnvios();
  }, [userId]); // Dependencia de userId para recargar los datos al cambiar el usuario

  const regresar = () => {
    navigate('/home');  // Redirige a la página principal
  };

  return (
    <div className="min-h-screen bg-gray-100 p-4">
      <div className="bg-white shadow-md p-8 rounded-md">
        <header className="flex justify-between items-center mb-4">
          <h1 className="text-2xl font-bold">Detalles de los Envíos</h1>
          <button className="text-red-500 font-bold" onClick={regresar}>Salir</button>
        </header>
        <h2 className="text-lg font-bold mb-4">Envíos asociados a tu cuenta</h2>
        {envios.length > 0 ? (
          <div>
            {envios.map((envio) => (
              <div key={envio.envio_id} className="mb-4">
                <p><strong>ID del Envío:</strong> {envio.envio_id}</p>
                <p><strong>Pedido ID:</strong> {envio.pedido_id}</p>
                <p><strong>Prioridad:</strong> {envio.prioridad}</p>
                <p><strong>Estado:</strong> {envio.estado}</p>
                <p><strong>Detalles:</strong> {envio.detalles}</p>
              </div>
            ))}
          </div>
        ) : (
          <p>No tienes envíos asociados a tus pedidos.</p>
        )}
        <button
          className="mt-4 p-2 bg-blue-500 text-white rounded-md"
          onClick={regresar}
        >
          Regresar
        </button>
      </div>
    </div>
  );
};

export default EnvioPage;
