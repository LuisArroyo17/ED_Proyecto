import React from 'react';

const Modal = ({ onClose, onConfirm, action }) => {
  return (
    <div className='fixed inset-0 flex items-center justify-center bg-gray-800 bg-opacity-50'>
      <div className='bg-white p-6 rounded-lg shadow-lg max-w-md w-full'>
        <h2 className='text-xl font-bold mb-4'>
          {action === 'delete' ? '¿Estás seguro de eliminar este producto?' : '¿Estás seguro de actualizar este producto?'}
        </h2>
        <p className='mb-6 text-gray-700'>Esta acción no se puede deshacer.</p>
        <div className='flex justify-end gap-4'>
          <button
            onClick={onClose}
            className='bg-gray-400 hover:bg-gray-600 text-white py-2 px-4 rounded-lg transition duration-200'>
            Cancelar
          </button>
          <button
            onClick={onConfirm}
            className={`py-2 px-4 rounded-lg text-white transition duration-200 ${
              action === 'delete' ? 'bg-red-500 hover:bg-red-700' : 'bg-green-500 hover:bg-green-700'
            }`}>
            Confirmar
          </button>
        </div>
      </div>
    </div>
  );
};

export default Modal;