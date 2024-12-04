import React from 'react';

const ColaDeEnvios = ({ envios }) => {
  return (
    <section className="w-full bg-white rounded-lg shadow-md p-4">
      <h2 className="text-lg font-bold mb-4">Cola de envíos</h2>
      <div className="space-y-4">
        {envios.map((envio) => (
          <div
            key={envio.envio_id}
            className={`flex justify-between items-center border p-4 rounded-md ${
              envio.estado === 'Enviado'
                ? 'bg-green-100'
                : envio.estado === 'Cancelado'
                ? 'bg-red-100'
                : 'bg-white-100'
            }`}
          >
            <div>
              <p className="font-bold">ID del envío: {envio.envio_id}</p>
              <p className="text-sm text-gray-500">Estado: {envio.estado}</p>
              <p className="text-sm text-gray-500">Prioridad: {envio.prioridad ? 'Alta' : 'Normal'}</p>
            </div>
          </div>
        ))}
      </div>
    </section>
  );
};

export default ColaDeEnvios;
