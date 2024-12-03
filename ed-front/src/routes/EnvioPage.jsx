import { useState, useEffect } from "react";
import { useUser } from "../context/UserContext";

const EnvioPage = () => {
  const { userId } = useUser();
  const [envios, setEnvios] = useState([]);
  const [error, setError] = useState(null);

  useEffect(() => {
    console.log("UserId:", userId); // Verifica si el userId es correcto
    if (!userId) {
      setError("No se encontró el ID del usuario.");
      return;
    }

    const fetchEnvios = async () => {
      try {
        const response = await fetch(`http://127.0.0.1:5000/envios/usuario/${userId}`);
        if (!response.ok) {
          throw new Error("Error al cargar los envíos.");
        }

        const data = await response.json();
        console.log("Envios data:", data); // Verifica los datos que recibes de la API
        setEnvios(data);
      } catch (error) {
        console.error(error);
        setError(error.message);
      }
    };

    fetchEnvios();
  }, [userId]);

  if (error) {
    return <div>Hubo un error: {error}</div>;
  }

  console.log("Envios state:", envios); // Verifica el estado antes de renderizar

  return (
    <div className="min-h-screen bg-gray-100 p-4">
      <h2 className="text-2xl font-bold mb-4">Mis Envíos</h2>
      {envios.length === 0 ? (
        <p>No tienes envíos registrados.</p>
      ) : (
        <ul className="space-y-4">
          {envios.map((envio) => (
            <li key={envio.id} className="bg-white rounded-lg shadow-md p-4 border border-gray-200">
              <p className="font-semibold">Pedido ID: {envio.pedido_id}</p>
              <p>Detalles: {envio.detalles}</p>
              <p>Prioridad: {envio.prioridad}</p>
              <p>Estado: {envio.estado}</p>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
};

export default EnvioPage;
