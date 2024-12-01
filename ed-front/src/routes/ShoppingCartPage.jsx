import React, { useState } from "react";
import logo from '../assets/casa-silueta-negra-sin-puerta.png';
import logo1 from '../assets/menu.png';
import linea from '../assets/linea.png';
import carrito from '../assets/carrito-de-compras (1).png';

const ShoppingCartPage = () => {
  // Datos simulados de productos en el carrito
  const [cart, setCart] = useState([
    { id: 1, nombre: "Producto 1", cantidad: 2, precio: 599.0 },
    { id: 2, nombre: "Producto 2", cantidad: 3, precio: 49.0 },
    { id: 3, nombre: "Producto 3", cantidad: 1, precio: 69.0 },
    { id: 4, nombre: "Producto 4", cantidad: 5, precio: 199.0 },
  ]);

  // Calcular total a pagar
  const totalPagar = cart.reduce(
    (total, producto) => total + producto.cantidad * producto.precio,
    0
  );

  const handleRemoveItem = (id) => {
    const updatedCart = cart.filter((item) => item.id !== id);
    setCart(updatedCart);
  };

  const handleCheckout = () => {
    alert("Compra realizada con éxito");
  };

  return (
    <div className="min-h-screen bg-gray-20 flex flex-col">
      {/* Encabezado */}
      <header className="flex justify-between items-center bg-purple-300 shadow-md p-2">
        <div className="flex items-center -space-x-0">
          <button >
          <img src={logo} alt="Logo" className="h-8 w-8 ml-1" onClick={() => (window.location.href = "/home")}/>
          </button>
          <img src={linea} alt="linea" className="h-8 w-8 " />
          <button>
          <img src={logo1} alt="Logo" className="h-8 w-8 -ml-0 mt-1"/>
          </button>
         
        </div>
        <div className="flex items-center">

          <button className=" absolute right-16" onClick={() => (window.location.href = "/carrito")}>

          <img src={carrito} alt="carrito" className="h-8 w-8 mr-10 -mt-1"/>
          </button>
          <button className="relative" onClick={() => (window.location.href = "/carrito")}>
            <i className="fas fa-shopping-cart text-xl"></i>
            <span className="absolute -top-2.5 right-16 bg-red-500 text-white text-xs w-5 h-5 flex justify-center items-center rounded-full">
              {cart.length}
            </span>
          </button>
          
          <img src={linea} alt="linea" className="absolute h-8 w-8 right-10"/>
          <button className="absolute text-red-500 font-bold right-3 top-4"  onClick={() => (window.location.href = "/")}>Salir</button>
          
          
        </div>
      </header>

      
      
      <h1 className="text-2xl font-bold absolute mt-16 ml-3.5">Mi carrito</h1>


      {/* Contenido principal */}
      <main className="flex flex-1 p-4 mt-10" >
        
        {/* Lista de productos */} 
        <section className="w-2/3 bg-red-100 rounded-lg shadow-md p-5">
          
          <h2 className="text-lg font-bold mb-4 ml-4">Productos
          <span className="text-lg font-bold ml-96">Subtotal</span>
          </h2>
     
          
        
          <div className="space-y-4">
            {cart.map((producto) => (
              <div
                key={producto.id}
                className="flex justify-between items-center border p-4 rounded-md"
              >
                <div className="flex items-center space-x-4">
                  <div className="w-16 h-16 bg-red-200 rounded-md"></div>
                  <div>
                    <h3 className="font-bold">{producto.nombre}</h3>
                    <p className="text-sm text-gray-500">
                      Cantidad: {producto.cantidad}
                    </p>
                  </div>
                </div>
                <p className="font-bold">
                  S/. {(producto.cantidad * producto.precio).toFixed(2)}
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
                <span className="font-bold">{producto.nombre}:</span>{" "}
                S/. {(producto.cantidad * producto.precio).toFixed(2)}
              </p>
            ))}
          </div>
          <hr className="my-4" />
          <p className="text-sm font-bold">
            Total a pagar: S/. {totalPagar.toFixed(2)}
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
  );


  
};




export default ShoppingCartPage;
