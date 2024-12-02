import { Table } from "../../components/Table";
import { TitleAdmin } from "../../components/TitleAdmin";

export function GestionarPedidosPage() {
  return (
    <section className="w-[80%] flex flex-col gap-10">
      <TitleAdmin title="Gestionar Pedidos" />
      <Table />
    </section>
  )
}
