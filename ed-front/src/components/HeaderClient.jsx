import { useNavigate } from 'react-router-dom';
import { useState } from 'react';
import logo from '../assets/casa-silueta-negra-sin-puerta.png';
import linea from '../assets/linea.png';
import carrito from '../assets/carrito-de-compras (1).png';

export const HeaderClient = () => {
  const navigate = useNavigate();
  const [cart, setCart] = useState([]); // Estado para gestionar los elementos del carrito

  // Función para agregar un producto al carrito
  const addToCart = (item) => {
    setCart((prevCart) => [...prevCart, item]); // Añadir un nuevo item al carrito
  };

  // Función para limpiar el carrito (opcional)
  const clearCart = () => {
    setCart([]); // Limpiar el carrito
  };

  return (
    <header className="flex justify-between items-center bg-white shadow-md p-4">

      {/* Sección de logo y línea */}
      <div className="flex items-center space-x-4">
      <h1 className="text-2xl font-bold">StockEase</h1>
        <button onClick={() => navigate("/home")}>
          <img src={logo} alt="Logo" className="h-8 w-8 ml-1" />
        </button>
      </div>

      {/* Sección de carrito y salir */}
      <div className="flex items-center space-x-4">
        {/* Botón de carrito */}
        <button className="absolute right-16" onClick={() => navigate('/carrito')}>
          <img src={carrito} alt="Carrito" className="h-8 w-8 mr-10 -mt-1" />
        </button>

        <button className="relative" onClick={() => navigate(0)}>
          <i className="fas fa-shopping-cart text-xl"></i>
          <span className="absolute -top-2.5 right-16 bg-red-500 text-white text-xs w-5 h-5 flex justify-center items-center rounded-full">
            {cart.length} 
          </span>
        </button>
        
        {/* Línea decorativa */}
        <img src={linea} alt="Linea" className=" h-7 w-8 right-10" />
        
        {/* Botón de salir */}
        <button className="text-red-500 font-bold" onClick={() => navigate("/")}>
          Salir
        </button>
      </div>
    </header>
  );
};
