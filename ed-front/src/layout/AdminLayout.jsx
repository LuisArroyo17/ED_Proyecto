import { Outlet } from "react-router-dom"
import { NavAside } from "../components/NavAside"
import { HeaderAdmin } from "../components/HeaderAdmin"

export const AdminLayout = () => {
  return (
    <>
      <HeaderAdmin />
      <main className="px-8 py-12 flex gap-28 min-h-dvh ">
        <NavAside />
        <Outlet />
      </main>
    </>
  )
}
