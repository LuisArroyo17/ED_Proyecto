import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";

const OrderPage = () => {
  const [productos, setProductos] = useState([]);
  const [loading, setLoading] = useState(true);
  const [prioridad, setPrioridad] = useState("normal"); // Prioridad seleccionada
  const navigate = useNavigate(); // Hook para redirección

  // Cargar productos desde la API
  useEffect(() => {
    const cargarProductos = async () => {
      try {
        const response = await fetch("http://127.0.0.1:5000/cargarCarrito", {
          method: "POST", // Cambié a POST
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({ usuario_id: 1 }), // Cuerpo de la solicitud
        });

        if (response.ok) {
          const data = await response.json();
          setProductos(data);
        } else {
          console.error("Error al cargar los productos.");
        }
      } catch (error) {
        console.error("Error:", error);
      } finally {
        setLoading(false);
      }
    };

    cargarProductos();
  }, []); // Solo se ejecuta una vez al montar el componente

  // Calcular el total
  const totalPagar = productos.reduce(
    (total, producto) => total + producto.cantidad * producto.precio,
    0
  );

  // Crear los detalles para el cuerpo de la solicitud
  const detalles = productos.map(producto => ({
    producto_id: producto.id,
    cantidad: producto.cantidad,
    precio: producto.precio
  }));

  // Función para realizar el pedido
  const handleRealizarPedido = async () => {
    const pedidoData = {
      usuario_id: 1,
      total: totalPagar,
      estado: "pendiente",
      detalles: detalles,
    };

    try {
      const response = await fetch("http://127.0.0.1:5000/pedidos", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(pedidoData),
      });

      const data = await response.json();

      if (response.ok) {
        alert(data.message); // Mostrar mensaje de éxito
        navigate("/pedidoconfirmado"); // Redireccionar a la página de confirmación
      } else {
        console.error(data.message);
        alert("Hubo un error al realizar el pedido.");
      }
    } catch (error) {
      console.error("Error:", error);
      alert("Hubo un error al realizar el pedido.");
    }
  };

  const handleCancelarPedido = () => {
    alert("Pedido cancelado");
  };

  const handlePrioridadChange = (e) => {
    setPrioridad(e.target.value); // Actualizamos la prioridad seleccionada
  };

  if (loading) {
    return <div>Loading...</div>;
  }

  return (
    <div className="min-h-screen bg-gray-100 flex flex-col">
      {/* Encabezado */}
      <header className="flex justify-between items-center bg-white shadow-md p-4">
        <div className="flex items-center space-x-4">
          <button className="text-xl">
            <i className="fas fa-bars"></i>
          </button>
          <h1 className="text-2xl font-bold">Realizar pedido</h1>
        </div>
        <div className="flex items-center space-x-4">
          <button className="relative">
            <i className="fas fa-shopping-cart text-xl"></i>
            <span className="absolute -top-2 -right-2 bg-red-500 text-white text-xs w-5 h-5 flex justify-center items-center rounded-full">
              {productos.length}
            </span>
          </button>
          <button className="text-red-500 font-bold">Salir</button>
        </div>
      </header>

      {/* Contenido */}
      <main className="flex flex-1 p-4">
        {/* Lista de productos */}
        <section className="w-3/5 bg-white rounded-lg shadow-md p-4">
          <h2 className="text-lg font-bold mb-4">Productos</h2>
          <div className="space-y-4">
            {productos.map((producto) => (
              <div key={producto.id} className="flex items-center justify-between border p-4 rounded-md">
                <div className="flex items-center space-x-4">
                  <div className="w-16 h-16 bg-gray-200 rounded-md">
                    <img
                      src={`${producto.imagen}`}
                      alt={producto.nombre}
                      className="w-full h-full object-cover rounded-md"
                    />
                  </div>
                  <div>
                    <p className="font-semibold">{producto.nombre}</p>
                    <p className="text-sm text-gray-600">Precio: ${producto.precio}</p>
                    <p className="text-sm text-gray-600">Cantidad: {producto.cantidad}</p>
                  </div>
                </div>
                <p className="text-lg font-semibold">${producto.precio * producto.cantidad}</p>
              </div>
            ))}
          </div>
        </section>

        {/* Resumen y detalles */}
        <section className="w-2/5 bg-white rounded-lg shadow-md p-4 ml-4">
          <h2 className="text-lg font-bold mb-4">Resumen del Pedido</h2>
          <div className="mb-4">
            <label className="font-semibold">Prioridad</label>
            <select
              value={prioridad}
              onChange={handlePrioridadChange}
              className="mt-2 p-2 border rounded-md w-full"
            >
              <option value="normal">Normal</option>
              <option value="alta">Alta</option>
            </select>
          </div>
          <div className="mb-4">
            <p className="font-semibold">Total a pagar: ${totalPagar.toFixed(2)}</p>
          </div>
          <div className="flex justify-between">
            <button
              onClick={handleRealizarPedido}
              className="bg-blue-500 text-white py-2 px-4 rounded-md"
            >
              Realizar Pedido
            </button>
            <button
              onClick={handleCancelarPedido}
              className="bg-gray-500 text-white py-2 px-4 rounded-md"
            >
              Cancelar
            </button>
          </div>
        </section>
      </main>
    </div>
  );
};

export default OrderPage;
