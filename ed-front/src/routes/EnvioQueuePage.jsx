import React, { useState, useEffect } from 'react';
import ColaDeEnvios from '../components/ColaDeEnvios';
import { useNavigate } from 'react-router-dom';

const EnvioQueuePage = () => {
  const [envios, setEnvios] = useState([]);
  const [mensaje, setMensaje] = useState('');
  const navigate = useNavigate();

  // Cargar todos los envíos en la cola
  const cargarEnvios = async () => {
    try {
      const response = await fetch('http://127.0.0.1:5000/envios');
      const data = await response.json();
      setEnvios(data.envios || []);
    } catch (error) {
      console.error("Error al cargar los envíos:", error);
    }
  };

  // Cargar el siguiente envío
  const cargarSiguienteEnvio = async () => {
    try {
      const response = await fetch('http://127.0.0.1:5000/envios/ver_siguiente');
      const data = await response.json();
      if (data.envio) {
        setEnvios([data.envio, ...envios]);  // Agregar el próximo envío al principio de la cola
      }
    } catch (error) {
      console.error("Error al cargar el siguiente envío:", error);
    }
  };

  useEffect(() => {
    cargarEnvios();
  }, []);

  // Enviar un envío normal
  const enviarEnvio = async () => {
    if (envios.length > 0) {
      const envio = envios[0];
      try {
        const responseEnvio = await fetch('http://127.0.0.1:5000/envios/enviar', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ envio_id: envio.envio_id }),
        });

        const dataEnvio = await responseEnvio.json();
        if (dataEnvio.message === 'Envío realizado') {
          setMensaje('Envío realizado exitosamente');
          cargarEnvios();  // Actualiza la lista después de enviar
        }
      } catch (error) {
        console.error('Error al enviar el envío:', error);
      }
    }
  };

  // Enviar un envío con prioridad
  const enviarEnvioConPrioridad = async () => {
    if (envios.length > 0) {
      const envio = envios[0];
      try {
        const responseEnvio = await fetch('http://127.0.0.1:5000/envios/enviar_mayor_prioridad', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
        });

        const dataEnvio = await responseEnvio.json();
        if (dataEnvio.message === 'Envío con prioridad realizado') {
          setMensaje('Envío con prioridad realizado');
          cargarEnvios();  // Actualiza la lista después de enviar con prioridad
        }
      } catch (error) {
        console.error('Error al enviar con prioridad:', error);
      }
    }
  };

  // Cancelar un envío
  const cancelarEnvio = async () => {
    if (envios.length > 0) {
      const envio = envios[0];
      try {
        const response = await fetch(`http://127.0.0.1:5000/envios/cancelar/${envio.envio_id}`, {
          method: 'POST',
        });
        const data = await response.json();
        if (data.message === 'Envío cancelado') {
          setMensaje('Envío cancelado correctamente');
          cargarEnvios();  // Actualiza la lista después de cancelar
        }
      } catch (error) {
        console.error('Error al cancelar el envío:', error);
      }
    }
  };

  return (
    <div className="min-h-screen bg-gray-100 flex flex-col">
      <main className="flex flex-1 p-4">
        <div className="w-1/2 bg-white rounded-lg shadow-md p-4">
          <ColaDeEnvios envios={envios} />
        </div>
        <div className="w-1/2 bg-white rounded-lg shadow-md p-4 ml-4">
          {envios.length > 0 ? (
            <div className="space-y-4">
              {/* Título para la sección de solicitudes de envío entrante */}
              <h2 className="text-xl font-bold mb-4">Para la Solicitud de Envío Entrante</h2>

              {/* Contenedor de botones "Enviar" y "Cancelar Envío" */}
              <div className="flex justify-between items-center">
                <button onClick={enviarEnvio} className="bg-blue-500 text-white p-2 rounded-md flex-1">
                  Enviar
                </button>
                <button onClick={cancelarEnvio} className="bg-red-500 text-white p-2 rounded-md ml-4">
                  Cancelar Envío
                </button>
              </div>

              {/* Título para la sección de solicitudes de envío ordenadas por prioridad */}
              <h2 className="text-xl font-bold mt-6 mb-4">Para la Solicitud de Envío Ordenadas por Prioridad</h2>
              
              {/* Botón "Enviar con Prioridad" debajo de los otros botones */}
              <button onClick={enviarEnvioConPrioridad} className="bg-yellow-500 text-white p-2 rounded-md w-full mt-4">
                Enviar con Prioridad
              </button>
            </div>
          ) : (
            <h2 className="text-lg font-bold">No hay envíos en cola</h2>
          )}
        </div>
      </main>

      {mensaje && (
        <div className="fixed bottom-4 right-4 bg-green-500 text-white p-4 rounded-md">
          {mensaje}
        </div>
      )}
    </div>
  );
};

export default EnvioQueuePage;



