import DataTable from "react-data-table-component";
import { Button } from "./Button";  // Verifica que la ruta de importación sea correcta


export const Table = () => {
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
      name: 'Actions',
      selector: row => row.actions,
    }
  ];

  const data = [
    {
      id: 1,
      nombre: 'Beetlejuice',
      precio: '1988',
      stock: '10',
      actions: <Button>Editar</Button>
    },
    {
      id: 2,
      nombre: 'Ghostbusters',
      precio: '1984',
      stock: '3',
      actions: <Button>Editar</Button>
    },
  ]

  return (
    <div className="overflow-x-scroll w-full">
      <DataTable
        columns={columns}
        data={data}
        pagination
        paginationPerPage={10}
      />
    </div>
  )
}
