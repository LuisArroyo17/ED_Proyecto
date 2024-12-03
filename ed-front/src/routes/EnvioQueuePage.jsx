import React, { useState, useEffect } from 'react';
import ColaDeEnvios from '../components/ColaDeEnvios';
import ProximoEnvioEnCola from '../components/ProximoEnvioEnCola';
import ProximoEnvioEnColaConPrioridad from '../components/ProximoEnvioEnColaConPrioridad';  // Nuevo componente
import { useNavigate } from 'react-router-dom';

const EnvioQueuePage = () => {
  const [envios, setEnvios] = useState([]);
  const [proximoEnvio, setProximoEnvio] = useState(null);
  const [envioConPrioridad, setEnvioConPrioridad] = useState(null);
  const [mensaje, setMensaje] = useState('');
  const navigate = useNavigate();

  // Cargar todos los envíos en la cola
  const cargarEnvios = async () => {
    try {
      const response = await fetch('http://127.0.0.1:5000/envios');
      const data = await response.json();
      setEnvios(data.envios || []);
      if (data.envios && data.envios.length > 0) {
        setProximoEnvio(data.envios[0]);
      } else {
        setProximoEnvio(null);
      }
    } catch (error) {
      console.error('Error al cargar los envíos:', error);
    }
  };

  // Cargar el siguiente envío con prioridad
  const cargarEnvioConPrioridad = async () => {
    try {
      const response = await fetch('http://127.0.0.1:5000/envios/mayor_prioridad');
      const data = await response.json();
      setEnvioConPrioridad(data || null);
    } catch (error) {
      console.error('Error al cargar el envío con mayor prioridad:', error);
    }
  };

  useEffect(() => {
    cargarEnvios();
    cargarEnvioConPrioridad();
  }, []);

  // Enviar un envío normal
  const enviarEnvio = async () => {
    if (proximoEnvio) {
      try {
        const responseEnvio = await fetch('http://127.0.0.1:5000/envios/enviar', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ envio_id: proximoEnvio.envio_id }),
        });

        const dataEnvio = await responseEnvio.json();
        if (dataEnvio.message === 'Envío realizado') {
          setMensaje('Envío realizado exitosamente');
          cargarEnvios();
        }
      } catch (error) {
        console.error('Error al enviar el envío:', error);
      }
    }
  };

  // Enviar un envío con prioridad
  const enviarEnvioConPrioridad = async () => {
    if (envioConPrioridad) {
      try {
        const responseEnvio = await fetch('http://127.0.0.1:5000/envios/enviar_mayor_prioridad', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ envio_id: envioConPrioridad.envio_id }),
        });

        const dataEnvio = await responseEnvio.json();
        if (dataEnvio.message === 'Envío con prioridad realizado') {
          setMensaje('Envío con prioridad realizado');
          cargarEnvios();
          cargarEnvioConPrioridad();
        }
      } catch (error) {
        console.error('Error al enviar con prioridad:', error);
      }
    }
  };

  // Cancelar un envío
  const cancelarEnvio = async (envioId) => {
    try {
      const response = await fetch(`http://127.0.0.1:5000/envios/cancelar/${envioId}`, {
        method: 'POST',
      });
      const data = await response.json();
      if (data.message === 'Envío cancelado') {
        setMensaje('Envío cancelado correctamente');
        cargarEnvios();
      }
    } catch (error) {
      console.error('Error al cancelar el envío:', error);
    }
  };

  return (
    <div className="min-h-screen bg-gray-100 flex flex-col">
      <main className="flex flex-1 p-4">
        <div className="w-1/2 bg-white rounded-lg shadow-md p-4">
          <ColaDeEnvios envios={envios} />
        </div>
        {proximoEnvio ? (
          <ProximoEnvioEnCola
            envio={proximoEnvio}
            onEnviar={enviarEnvio}
            onCancelar={() => cancelarEnvio(proximoEnvio.envio_id)}
          />
        ) : (
          <div className="w-1/2 bg-white rounded-lg shadow-md p-4 ml-4">
            <h2 className="text-lg font-bold mb-4">No hay envíos en cola</h2>
          </div>
        )}

        <ProximoEnvioEnColaConPrioridad
          envioConPrioridad={envioConPrioridad}
          onEnviarConPrioridad={enviarEnvioConPrioridad}
          onCancelar={cancelarEnvio}
        />
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
