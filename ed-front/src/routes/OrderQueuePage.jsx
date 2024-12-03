import React, { useState, useEffect } from 'react';
import ColaDePedidos from '../components/ColaDePedidos';
import ProximoPedidoEnCola from '../components/ProximoPedidoEnCola';
import { useNavigate } from 'react-router-dom';

const OrderQueuePage = () => {
  const [pedidos, setPedidos] = useState([]);
  const [proximoPedido, setProximoPedido] = useState(null);
  const [mensaje, setMensaje] = useState('');
  const navigate = useNavigate();
  const cargarPedidos = async () => {
    try {
      const response = await fetch('http://127.0.0.1:5000/pedidos');
      const data = await response.json();
      setPedidos(data.pedidos || []);
      if (data.pedidos && data.pedidos.length > 0) {
        setProximoPedido(data.pedidos[0]); 
      } else {
        setProximoPedido(null);
      }
    } catch (error) {
      console.error("Error al cargar los pedidos:", error);
    }
  };

  useEffect(() => {
    cargarPedidos();
  }, []);

  const procesarPedido = async () => {
    if (proximoPedido) {
      console.log('Procesando pedido:', proximoPedido.pedido_id);
      try {
        const responsePedido = await fetch('http://127.0.0.1:5000/pedidos/procesar', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ pedido_id: proximoPedido.pedido_id }),
        });
  
        const dataPedido = await responsePedido.json();
        console.log('Respuesta del servidor para pedido:', dataPedido);
  
        if (dataPedido.message === 'Pedido procesado') {
          setMensaje('Pedido procesado exitosamente');
          console.log('Pedido procesado exitosamente');
  
          const envioResponse = await fetch('http://127.0.0.1:5000/envios', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
            },
            body: JSON.stringify({
              pedido_id: proximoPedido.pedido_id,
              detalles: 'Envio de televisor a SJL', 
              prioridad: 1,
              estado: 'pendiente',
            }),
          });
  
          const dataEnvio = await envioResponse.json();
          console.log('Respuesta del servidor para envío:', dataEnvio);
  
          if (dataEnvio.message === 'Envio agregado') {
            console.log('Envio agregado correctamente');
          }
  
          cargarPedidos();
        }
      } catch (error) {
        console.error('Error al procesar el pedido o el envío:', error);
      }
    }
  };
  

  const cancelarPedido = async () => {
    if (proximoPedido) {
      try {
        const response = await fetch(`http://127.0.0.1:5000/pedidos/cancelar/${proximoPedido.pedido_id}`, {
          method: 'POST',
        });
        const data = await response.json();
        console.log('Respuesta del servidor:', data);
        if (data.message === 'Pedido cancelado') {
          setMensaje('Pedido cancelado correctamente');
          cargarPedidos();
        }
      } catch (error) {
        console.error('Error al cancelar el pedido:', error);
      }
    }
  };

  return (
    <div className="min-h-screen bg-gray-100 flex flex-col">
      <main className="flex flex-1 p-4">
        <div className="w-1/2 bg-white rounded-lg shadow-md p-4">
          <ColaDePedidos pedidos={pedidos} />
        </div>
        {proximoPedido ? (
          <ProximoPedidoEnCola
            pedido={proximoPedido}
            onProcesar={procesarPedido}
            onCancelar={cancelarPedido}
          />
        ) : (
          <div className="w-1/2 bg-white rounded-lg shadow-md p-4 ml-4">
            <h2 className="text-lg font-bold mb-4">No hay pedidos en cola</h2>
          </div>
        )}
      </main>

      {mensaje && (
        <div className="fixed bottom-4 right-4 bg-green-500 text-white p-4 rounded-md">
          {mensaje}
        </div>
      )}
    </div>
  );
};

export default OrderQueuePage;
