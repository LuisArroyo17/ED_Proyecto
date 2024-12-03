import React, { useState } from "react";

export const ProductDetailModal = ({ product, onClose }) => {
  const [quantity, setQuantity] = useState(1);

  const handleAddToCart = async () => {
    console.log(`Añadido al carrito: ${product.nombre}, Cantidad: ${quantity}`);
    try {
      const response = await fetch('http://localhost:5000/carrito/temporal/agregar', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          producto_id: product.id,
          cantidad: quantity,
        }),
      });
      const data = await response.json();
      if (response.ok) {
        console.log('Carrito actualizado:', data.carrito);
      } else {
        console.error('Error al añadir al carrito:', data.message);
      }
    } catch (error) {
      console.error('Error en la solicitud:', error);
    }
  };

  const incrementQuantity = () => setQuantity(quantity + 1);
  const decrementQuantity = () => {
    if (quantity > 1) setQuantity(quantity - 1);
  };

  return (
    <div className="fixed inset-0 bg-black bg-opacity-50 flex justify-center items-center">
      <div className="bg-white p-6 rounded-md shadow-md max-w-sm w-full">
        <h2 className="text-xl font-bold mb-4">{product.nombre}</h2>
        <p className="text-sm text-gray-500">Categoría: {product.categoria}</p>
        <p className="text-lg font-bold my-2">S/. {product.precio}</p>
        <p className="text-sm text-gray-600">{product.descripcion}</p>

        <div className="flex items-center mt-4">
          <button
            className="p-2 bg-gray-200 text-gray-800 rounded-l-md"
            onClick={decrementQuantity}
          >
            -
          </button>
          <input
            type="text"
            readOnly
            value={quantity}
            className="w-10 text-center border border-gray-300"
          />
          <button
            className="p-2 bg-gray-200 text-gray-800 rounded-r-md"
            onClick={incrementQuantity}
          >
            +
          </button>
        </div>

        <div className="mt-4 flex justify-between">
          <button
            className="bg-red-500 text-white px-4 py-2 rounded-md"
            onClick={onClose}
          >
            Cerrar
          </button>
          <button
            className="bg-blue-500 text-white px-4 py-2 rounded-md"
            onClick={handleAddToCart}
          >
            Añadir al carrito
          </button>
        </div>
      </div>
    </div>
  );
};
