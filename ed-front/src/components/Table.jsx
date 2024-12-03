import React, { useEffect, useState } from 'react';
import DataTable from "react-data-table-component";
import { Button } from "./Button";  // Verifica que la ruta de importación sea correcta

export const Table = ({ columns, data, loading, onAction }) => {
  if (loading) {
    return <div>Cargando...</div>; // Puedes agregar un spinner o algo más elegante
  }

  return (
    <div className="overflow-x-scroll w-full">
      <DataTable
        columns={columns}
        data={data}
        pagination
        paginationPerPage={10}
      />
    </div>
  );
}
