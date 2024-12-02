import React, { useState, useEffect } from 'react';

const ProximoPedidoEnCola = ({ pedido, onProcesar, onCancelar }) => {
  const [detalles, setDetalles] = useState([]); 
  const [productos, setProductos] = useState([]); 
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null); 

  useEffect(() => {
    if (!pedido) return; 

    const fetchDetalles = async () => {
      setLoading(true);
      setError(null);

      try {
        const response = await fetch(`http://127.0.0.1:5000/pedidos/${pedido.pedido_id}/detalles`);
        console.log('Respuesta detalles:', response); 
        if (!response.ok) {
          throw new Error('Error al obtener los detalles del pedido');
        }
        const data = await response.json();
        console.log('Datos detalles:', data); 
        setDetalles(data.detalles);
      } catch (error) {
        console.error('Error al obtener los detalles:', error); 
        setError(error.message);
      } finally {
        setLoading(false);
      }
    };

    fetchDetalles();
  }, [pedido]);

  useEffect(() => {
    const fetchProductos = async () => {
      try {
        const response = await fetch('http://127.0.0.1:5000/productos');
        console.log('Respuesta productos:', response); 
        if (!response.ok) {
          throw new Error('Error al obtener los productos');
        }
        const data = await response.json();
        console.log('Datos productos:', data); 
        setProductos(data.data);
      } catch (error) {
        console.error('Error al obtener productos:', error); 
        setError(error.message);
      }
    };

    fetchProductos();
  }, []); 

  if (!pedido) return null; 

  return (
    <aside className="w-1/2 bg-white rounded-lg shadow-md p-4 ml-4">
      <h2 className="text-lg font-bold mb-4">Próximo pedido en cola</h2>
      <div className="space-y-2">
        <p className="text-sm">
          <span className="font-bold">ID del pedido:</span> {pedido.pedido_id}
        </p>
        <p className="text-sm">
          <span className="font-bold">Valor del pedido:</span> S/. {pedido.total.toFixed(2)}
        </p>
        <p className="text-sm">
          <span className="font-bold">Prioridad:</span> {pedido.prioridad}
        </p>
        <p className="text-sm">
          <span className="font-bold">Fecha y hora:</span> {pedido.fecha}
        </p>
        <p className="text-sm">
          <span className="font-bold">Usuario:</span> {pedido.usuario_id}
        </p>
      </div>

      {/* Mostrar detalles del pedido */}
      <div className="mt-4">
        {loading && <p className="text-sm text-gray-500">Cargando detalles...</p>}
        {error && <p className="text-sm text-red-500">{error}</p>}
        {!loading && !error && detalles.length > 0 && (
          <div>
            <h3 className="text-md font-semibold">Detalles del pedido:</h3>
            <ul className="space-y-2">
              {detalles.map((detalle) => {
                const producto = productos.find((prod) => prod.id === detalle.producto_id);
                return (
                  <li key={detalle.id} className="flex justify-between items-center border p-4 rounded-md">
                    <div className="flex-1">
                      <p>
                        <span className="font-bold">Producto:</span> {detalle.producto_nombre}
                      </p>
                      <p>
                        <span className="font-bold">Cantidad:</span> {detalle.cantidad}
                      </p>
                      <p>
                        <span className="font-bold">Precio:</span> S/. {parseFloat(detalle.precio).toFixed(2)}
                      </p>
                    </div>
                    {producto && (
                      <div className="w-16 h-16 ml-4">
                        <img src={`${producto.imagen}`} alt={producto.nombre} className="object-cover w-full h-full rounded-md" />
                      </div>
                    )}
                  </li>
                );
              })}
            </ul>
          </div>
        )}
        {!loading && detalles.length === 0 && !error && (
          <p className="text-sm text-gray-500">No hay detalles disponibles para este pedido.</p>
        )}
      </div>

      <div className="flex space-x-4 mt-4">
        <button
          onClick={onProcesar}
          disabled={!pedido} 
          className="flex-1 bg-green-500 text-white py-2 rounded-md hover:bg-green-600 disabled:bg-gray-300"
        >
          Procesar pedido
        </button>
        <button
          onClick={onCancelar}
          disabled={!pedido} 
          className="flex-1 bg-red-500 text-white py-2 rounded-md hover:bg-red-600 disabled:bg-gray-300"
        >
          Cancelar
        </button>
      </div>
    </aside>
  );
};

export default ProximoPedidoEnCola;
