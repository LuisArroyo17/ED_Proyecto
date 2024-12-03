import React, { useState, useEffect } from 'react'; 
import { useNavigate, useParams } from 'react-router-dom';
import { useUser } from "../context/UserContext";



const EnvioPage = () => {
  const { id } = useParams();  // Obtener el parámetro de la URL
  const [envio, setEnvio] = useState(null);
  const navigate = useNavigate();
  const { userId } = useUser();

  useEffect(() => {
    const obtenerEnvio = async () => {
      try {
        const response = await fetch(`http://localhost:5000/envios/${id}`);  // Usar el ID dinámico
        const data = await response.json();
        setEnvio(data);
      } catch (error) {
        console.error("Error al cargar el envío:", error);
      }
    };

    obtenerEnvio();
  }, [id]);

  const regresar = () => {
    navigate('/home');  // Redirige a la página principal
  };

  return (
    <div className="min-h-screen bg-gray-100 p-4">
      <div className="bg-white shadow-md p-8 rounded-md">
        <header className="flex justify-between items-center mb-4">
          <h1 className="text-2xl font-bold">Detalles del Envío</h1>
          <button className="text-red-500 font-bold" onClick={regresar}>Salir</button>
        </header>
        <h2 className="text-lg font-bold mb-4">Información del Envío</h2>
        {envio ? (
          <div>
            <p>ID del Envío: {envio.envio_id}</p>
            <p>Pedido ID: {envio.pedido_id}</p>
            <p>Prioridad: {envio.prioridad}</p>
            <p>Estado: {envio.estado}</p>
            <p>Detalles: {envio.detalles}</p>
          </div>
        ) : (
          <p>Cargando...</p>
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