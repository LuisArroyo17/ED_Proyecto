import React, { useState, useEffect } from "react";
import { useUser } from "../context/UserContext";
import { useNavigate } from "react-router-dom";

const UserHomePage = () => {
  const { userId } = useUser();
  console.log("ID del usuario:", userId);
  const navigate = useNavigate();

  const [productos, setProductos] = useState([]);
  const [searchQuery, setSearchQuery] = useState("");
  const [filteredProductos, setFilteredProductos] = useState([]);
  const [selectedCategory, setSelectedCategory] = useState("");

  // Función para obtener los productos desde la API
  const fetchProductos = async () => {
    try {
      const response = await fetch("http://localhost:5000/productos");
      const result = await response.json();
      setProductos(result.data);
      setFilteredProductos(result.data); // Inicializar con todos los productos
    } catch (error) {
      console.error("Error al obtener los productos:", error);
    }
  };

  // Ejecutar cuando el componente se monta
  useEffect(() => {
    fetchProductos();
  }, []);

   // Manejar el cambio en la barra de búsqueda
   const handleSearchChange = (e) => {
    const query = e.target.value;
    setSearchQuery(query);

    // Filtrar productos basados en la búsqueda
    const filtered = productos.filter((producto) =>
      producto.nombre.toLowerCase().includes(query.toLowerCase())
    );
    setFilteredProductos(filtered);
  };

  // Filtrar los productos según la categoría seleccionada
  const handleCategoryClick = (category) => {
    setSelectedCategory(category);
    const filtered = productos.filter((producto) =>
      category === "" ? true : producto.categoria === category
    );
    setFilteredProductos(filtered);
  };

  // Función para redirigir al detalle del producto
  const redirigir = () => {
    navigate("/realizarPedido");
  };

  return (
    <div className="min-h-screen bg-gray-100 flex">
      {/* Menú lateral */}
      <aside className="w-1/4 bg-white shadow-md p-4">
        <h2 className="text-lg font-bold mb-4">Menú de opciones</h2>
        <ul className="space-y-2">
          {/* Categorías */}
          <li
            className="p-2 rounded-md cursor-pointer hover:bg-gray-300"
            onClick={() => handleCategoryClick("")}
          >
            Todos los productos
          </li>
          <li
            className="p-2 rounded-md cursor-pointer hover:bg-gray-300"
            onClick={() => handleCategoryClick("Ropa")}
          >
            Ropa
          </li>
          <li
            className="p-2 rounded-md cursor-pointer hover:bg-gray-300"
            onClick={() => handleCategoryClick("Calzado")}
          >
            Calzado
          </li>
          <li
            className="p-2 rounded-md cursor-pointer hover:bg-gray-300"
            onClick={() => handleCategoryClick("Electrónica")}
          >
            Electrónica
          </li>
          <li
            className="p-2 rounded-md cursor-pointer hover:bg-gray-300"
            onClick={() => handleCategoryClick("Muebles")}
          >
            Muebles
          </li>
          <li
            className="p-2 rounded-md cursor-pointer hover:bg-gray-300"
            onClick={() => handleCategoryClick("Accesorios")}
          >
            Accesorios
          </li>
          <li
            className="p-2 rounded-md cursor-pointer hover:bg-gray-300"
            onClick={() => handleCategoryClick("Hogar")}
          >
            Hogar
          </li>
          <li
            className="p-2 rounded-md cursor-pointer hover:bg-gray-300"
            onClick={() => handleCategoryClick("Juguetes")}
          >
            Juguetes
          </li>
        </ul>
      </aside>

      {/* Contenido principal */}
      <main className="flex-1 p-4">
        <header className="flex justify-between items-center mb-4">
          <h1 className="text-2xl font-bold">StockEase</h1>
          <div className="flex items-center space-x-4">
            <button className="relative">
              <i className="fas fa-shopping-cart text-xl"></i>
              <span className="absolute -top-2 -right-2 bg-red-500 text-white text-xs w-5 h-5 flex justify-center items-center rounded-full">
                2
              </span>
            </button>
            <button className="text-red-500 font-bold">Salir</button>
          </div>
        </header>

       {/* Barra de búsqueda */}
       <div className="mb-4">
          <input
            type="text"
            placeholder="Ingresa el nombre del producto"
            className="w-3/4 p-2 border border-gray-300 rounded-md"
            value={searchQuery}
            onChange={handleSearchChange}  // Se ejecuta cada vez que el usuario escribe
          />
          <button className="p-2 bg-blue-500 text-white rounded-md ml-2">
            <i className="fas fa-search"></i>
          </button>
        </div>

        {/* Productos filtrados */}
        <section>
          <h2 className="text-lg font-bold mb-4">Productos {selectedCategory ? `- ${selectedCategory}` : ""}</h2>
          <div className="grid grid-cols-3 gap-4">
            {filteredProductos.map((producto) => (
              <div key={producto.id} className="bg-white shadow-md rounded-md p-4">
                <div className="h-32 bg-gray-200 rounded-md mb-2"></div>
                <h3 className="text-sm font-bold">{producto.nombre}</h3>
                <p className="text-sm text-gray-500">S/. {producto.precio}</p>
                <button
                  className="mt-2 p-2 bg-blue-500 text-white rounded-md w-full"
                  onClick={redirigir}
                >
                  Ver detalles
                </button>
              </div>
            ))}
          </div>
        </section>
      </main>
    </div>
  );
};

export default UserHomePage;
