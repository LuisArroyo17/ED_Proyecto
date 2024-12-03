// src/components/ProductDetailModal.jsx
import React from "react";

export const ProductDetailModal = ({ product, onClose }) => {
  return (
    <div className="fixed inset-0 bg-black bg-opacity-50 flex justify-center items-center">
      <div className="bg-white p-6 rounded-lg max-w-lg w-full">
        <h2 className="text-xl font-bold">{product.nombre}</h2>
        <p className="text-sm text-gray-500 mb-4">Categoría: {product.categoria}</p>
        <p className="text-lg font-semibold mb-4">S/. {product.precio}</p>
        <p className="mb-4">{product.descripcion}</p>
        <button
          className="p-2 bg-red-500 text-white rounded-md"
          onClick={onClose} // Cerrar el modal
        >
          Cerrar
        </button>
      </div>
    </div>
  );
};
