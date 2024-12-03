import { useNavigate } from 'react-router-dom';
import logo from '../assets/casa-silueta-negra-sin-puerta.png';
import linea from '../assets/linea.png';
import carrito from '../assets/carrito-de-compras (1).png';

export const HeaderClient = () => {
  const navigate = useNavigate();
    
  const clearCart = () => {
    setCart([]); // Limpiar el carrito
    navigate("/")
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
