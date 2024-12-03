import { Table } from "../../components/Table";
import { TitleAdmin } from "../../components/TitleAdmin";

export function GestionarProductosPage() {
  return (
    <section className="w-[80%] flex flex-col gap-10">
      <TitleAdmin title="Gestionar Productos" />
      <Table />
    </section>
  )
}
