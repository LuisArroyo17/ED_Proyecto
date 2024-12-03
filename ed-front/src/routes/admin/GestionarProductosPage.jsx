import React, { useEffect, useState } from "react";
import { Table } from "../../components/Table";
import { TitleAdmin } from "../../components/TitleAdmin";
import { Button } from "../../components/Button";  // Importa el Button correctamente
import { useNavigate } from "react-router-dom";

export function GestionarProductosPage() {
  const [productos, setProductos] = useState([]);
  const [loading, setLoading] = useState(true);
  const [showDialog, setShowDialog] = useState(false);  // Estado para controlar la visibilidad del modal
  const [productoEditando, setProductoEditando] = useState(null);  // Estado para el producto que se está editando
  const navigate = useNavigate();
  // Función para obtener los productos desde la API
  const fetchProductos = async () => {
    try {
      const response = await fetch('http://localhost:5000/productos');
      const result = await response.json();
      setProductos(result.data); 
      setLoading(false);
    } catch (error) {
      console.error('Error al obtener los productos:', error);
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchProductos();
  }, []);

  const handleEdit = (producto) => {
    setProductoEditando(producto);  // Asignar el producto a editar
    setShowDialog(true);  // Abrir el modal
  };

  const handleCloseDialog = () => {
    setShowDialog(false);  // Cerrar el modal
    setProductoEditando(null);  // Limpiar el producto editado
  };

  const handleSave = async (e) => {
    e.preventDefault();
    // Aquí puedes agregar la lógica para guardar los cambios en el producto
    console.log("Guardando producto editado:", productoEditando);

    // Actualiza el producto en la API
    try {
      const response = await fetch(`http://localhost:5000/productos/${productoEditando.id}`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(productoEditando),
      });

      if (response.ok) {
        // Actualiza la lista de productos después de guardar
        fetchProductos();
        handleCloseDialog();
      } else {
        console.error("Error al guardar el producto.");
      }
    } catch (error) {
      console.error("Error al hacer la petición de guardado:", error);
    }
  };

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setProductoEditando(prevState => ({
      ...prevState,
      [name]: value,
    }));
  };

  const columns = [
    {
      name: 'Nombre',
      selector: row => row.nombre,
    },
    {
      name: 'Precio',
      selector: row => row.precio,
    },
    {
      name: 'Stock',
      selector: row => row.stock,
    },
    {
      name: 'Acciones',
      cell: row => <Button onClick={() => navigate(`/detalle-producto/${row.id}`)}>Editar</Button>,  // Usando el ID dinámico
    }
  ];
  

  return (
    <section className="w-[80%] flex flex-col gap-10">
      <TitleAdmin title="Gestionar Productos" />
      <Table
        columns={columns}
        data={productos}
        loading={loading}
      />

      {/* Modal para editar producto */}
      {showDialog && (
        <div className="fixed inset-0 flex justify-center items-center bg-black bg-opacity-50">
          <div className="bg-white p-6 rounded-lg w-[400px]">
            <h2 className="text-xl mb-4">Editar Producto</h2>
            <form onSubmit={handleSave}>
              <div className="mb-4">
                <label className="block text-sm font-medium">Nombre</label>
                <input
                  type="text"
                  name="nombre"
                  value={productoEditando?.nombre || ''}
                  onChange={handleInputChange}
                  className="w-full p-2 border border-gray-300 rounded"
                />
              </div>
              <div className="mb-4">
                <label className="block text-sm font-medium">Precio</label>
                <input
                  type="text"
                  name="precio"
                  value={productoEditando?.precio || ''}
                  onChange={handleInputChange}
                  className="w-full p-2 border border-gray-300 rounded"
                />
              </div>
              <div className="mb-4">
                <label className="block text-sm font-medium">Stock</label>
                <input
                  type="number"
                  name="stock"
                  value={productoEditando?.stock || ''}
                  onChange={handleInputChange}
                  className="w-full p-2 border border-gray-300 rounded"
                />
              </div>
              <div className="flex justify-between">
                <Button onClick={handleCloseDialog}>Cancelar</Button>
                <Button type="submit">Guardar</Button>
              </div>
            </form>
          </div>
        </div>
      )}
    </section>
  );
}
