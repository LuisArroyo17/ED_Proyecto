import React from 'react';

const ProximoEnvioEnCola = ({ envio, onEnviar, onCancelar }) => {
  return (
    <aside className="w-1/2 bg-white rounded-lg shadow-md p-4 ml-4">
      <h2 className="text-lg font-bold mb-4">Próximo envío en cola</h2>
      <div className="space-y-2">
        <p className="text-sm">
          <span className="font-bold">ID del envío:</span> {envio.envio_id}
        </p>
        <p className="text-sm">
          <span className="font-bold">Prioridad:</span> {envio.prioridad ? 'Alta' : 'Normal'}
        </p>
        <p className="text-sm">
          <span className="font-bold">Estado:</span> {envio.estado}
        </p>
      </div>
      <div className="mt-4">
        <button onClick={onEnviar} className="bg-blue-500 text-white p-2 rounded-md mr-2">Enviar</button>
        <button onClick={() => onCancelar()} className="bg-red-500 text-white p-2 rounded-md">Cancelar Envío</button>
      </div>
    </aside>
  );
};

export default ProximoEnvioEnCola;
