// src/components/ProductCard.jsx
import React from "react";

export const ProductCard = ({ producto, onSelectProduct }) => {
  return (
    <div className="bg-white shadow-md rounded-md p-4">
      <div className="h-32 bg-gray-200 rounded-md mb-2"></div>
      <h3 className="text-sm font-bold">{producto.nombre}</h3>
      <p className="text-sm text-gray-500">S/. {producto.precio}</p>
      <button
        className="mt-2 p-2 bg-blue-500 text-white rounded-md w-full"
        onClick={() => onSelectProduct(producto)} // Abrir el modal
      >
        Ver detalles
      </button>
    </div>
  );
};
