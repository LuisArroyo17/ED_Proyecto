import React, { useState, useEffect } from "react";
import { useUser } from "../context/UserContext";
import logo from '../assets/casa-silueta-negra-sin-puerta.png';
import linea from '../assets/linea.png';
import carrito from '../assets/carrito-de-compras (1).png';
import {useNavigate} from "react-router-dom";

const ShoppingCartPage = () => {
  // Estado para almacenar los productos del carrito
  const navigate = useNavigate(); //HOOk
  const [cart, setCart] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const { userId } = useUser();
  // Cargar los productos del carrito temporal al montar el componente
  useEffect(() => {
    const fetchCart = async () => {
      try {
        const response = await fetch("http://localhost:5000/carrito/temporal/ver");
        
        if (!response.ok) {
          throw new Error("Error al cargar el carrito");
        }
        const data = await response.json();
        setCart(data); // Actualizar el estado con los datos obtenidos
      } catch (error) {
        setError(error.message); // Capturar errores
      } finally {
        setLoading(false); // Ocultar el estado de carga
      }
    };

    fetchCart();
  }, []); // [] asegura que se ejecute solo al montar el componente

  // Manejar la eliminación de un producto del carrito
  const handleRemoveItem = async (id) => {
    try {
      const response = await fetch("http://localhost:5000/carrito/temporal/eliminar", {
        method: "DELETE",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({producto_id: id }),
      });
      if (response.ok) {
        setCart(cart.filter((item) => item.id !== id)); // Actualizar el estado
      } else {
        alert("Error al eliminar el producto");
      }
    } catch (error) {
      console.error("Error al eliminar el producto:", error);
    }
  };

  // Manejar el envío del carrito a la base de datos
  const handleCheckout = async () => {
    try {
      const response = await fetch("http://localhost:5000/carrito/oficial", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ usuario_id: userId }), // Reemplaza con el ID del usuario real
      });
      if (response.ok) {
        alert("Compra preparada con éxito");
        setCart([]); // Limpiar el carrito después de la compra
        navigate("/realizarPedido");
      } else {
        alert("Error al procesar la compra");
      }
    } catch (error) {
      console.error("Error al procesar la compra:", error);
    }
    
  };

  // Eliminar la lista temporal completa al salir de la sesion
  const handleRemoveAll = async () => {
    try {
      const response = await fetch("http://localhost:5000/carrito/temporal/vaciar",{
      method: 'DELETE', 
      });

        if (!response.ok) {
          throw new Error("Error al cargar el carrito");
        }
        const data = await response.json();
        console.log(data.message);
        navigate("/")
      } catch (error) {
        setError(error.message); // Capturar errores
      } finally {
        setLoading(false); // Ocultar el estado de carga
      }
  };

  if (loading) {
    return <div>Cargando carrito...</div>;
  }

  if (error) {
    return <div>Error: {error}</div>;
  }

  return (
    <>
    <div className="min-h-screen bg-gray-20 flex flex-col">
      {/* Encabezado */}
      <header className="flex justify-between items-center bg-white shadow-md p-4">
        <div className="flex items-center space-x-4">
        <h1 className="text-2xl font-bold">StockEase</h1>
        <button onClick={() => navigate("/home")}>
          <img src={logo} alt="Logo" className="h-8 w-8 ml-1" />
        </button>
          
        </div>
        <div className="flex items-center">

          <button className=" absolute right-16" onClick={() => navigate(0)}>

          <img src={carrito} alt="carrito" className="h-8 w-8 mr-10 -mt-1"/>
          </button>
          <button className="relative" onClick={() => navigate(0)} >
            <i className="fas fa-shopping-cart text-xl"></i>
            <span className="absolute -top-2.5 right-16 bg-red-500 text-white text-xs w-5 h-5 flex justify-center items-center rounded-full">
              {cart.length}
            </span>
          </button>
          
          <img src={linea} alt="linea" className="absolute h-8 w-8 right-10"/>
          <button className="absolute text-red-500 font-bold right-3"  onClick={() => handleRemoveAll()}>Salir</button>
          
          
        </div>
        </header>
        <h1 className="text-2xl font-bold absolute mt-20 ml-3.5">Mi carrito</h1>


        <main className="flex flex-1 p-4 mt-10" >
        {/* Lista de productos en el carrito */}
        <section className="w-2/3 bg-white rounded-lg shadow-md p-5">
          <h2 className="text-lg font-bold mb-4">Productos</h2>
          <div className="space-y-4">
            {cart.map((producto) => (
              <div
                key={producto.id}
                className="flex justify-between items-center border p-4 rounded-md"
              >
                <div className="w-16 h-16 bg-gray-200 rounded-md ">
                    <img
                      src={`${producto.imagen}`}
                      alt={producto.nombre}
                      className="w-full h-full object-cover rounded-md"
                    />
                  </div>

                <div className="absolute ml-20">
                  <h3 className="font-bold">{producto.nombre}</h3>
                  <p className="text-sm text-black-500">Cantidad: {producto.cantidad}</p>
                  <p className="text-sm text-black-500">Precio: S/. {producto.precio}</p>
                </div>
                <p className="font-bold ml-1">
                  Subtotal: S/. {(producto.cantidad * producto.precio).toFixed(2)}
                </p>
                <button
                  onClick={() => handleRemoveItem(producto.id)}
                  className="text-red-500 text-sm hover:underline"
                >
                  Eliminar
                  
                </button>
                
              </div>
            ))}
          </div>
        </section>

        {/* Resumen de compra */}
        <aside className="w-1/3 bg-white rounded-lg shadow-md p-4 ml-4">
          <h2 className="text-lg font-bold mb-4">Resumen de compra</h2>
          <div className="space-y-2">
            {cart.map((producto) => (
              <p key={producto.id} className="text-sm">
                {producto.nombre}: S/. {(producto.cantidad * producto.precio).toFixed(2)}
              </p>
            ))}
          </div>
          <hr className="my-4" />
          <p className="text-sm font-bold">
            Total a pagar: S/.{" "}
            {cart.reduce((total, producto) => total + producto.cantidad * producto.precio, 0).toFixed(2)}
          </p>
          <button
            onClick={handleCheckout}
            className="mt-4 w-full bg-green-500 text-white py-2 rounded-md hover:bg-green-600"
          >
            Comprar
          </button>
        </aside>
      </main>
    </div>
    </>
  );
};

export default ShoppingCartPage;