import React, { useState, useEffect } from 'react';

const ProximoEnvioEnColaConPrioridad = ({ onEnviarConPrioridad, onCancelar, envioConPrioridad }) => {
  if (!envioConPrioridad) {
    return (
      <div className="w-1/2 bg-white rounded-lg shadow-md p-4 ml-4">
        <h2 className="text-lg font-bold mb-4">No hay envíos con prioridad</h2>
      </div>
    );
  }

  return (
    <aside className="w-1/2 bg-white rounded-lg shadow-md p-4 ml-4">
      <h2 className="text-lg font-bold mb-4">Próximo envío en cola con prioridad</h2>
      <div className="space-y-2">
        <p className="text-sm">
          <span className="font-bold">ID del Envío:</span> {envioConPrioridad.envio_id}
        </p>
        <p className="text-sm">
          <span className="font-bold">Prioridad:</span> Alta
        </p>
        <p className="text-sm">
          <span className="font-bold">Estado:</span> {envioConPrioridad.estado}
        </p>
      </div>
      <div className="mt-4">
        <button onClick={onEnviarConPrioridad} className="bg-yellow-500 text-white p-2 rounded-md mt-4">
          Enviar con Prioridad
        </button>
        <button onClick={() => onCancelar(envioConPrioridad.envio_id)} className="bg-red-500 text-white p-2 rounded-md mt-4">
          Cancelar Envío
        </button>
      </div>
    </aside>
  );
};

export default ProximoEnvioEnColaConPrioridad;
