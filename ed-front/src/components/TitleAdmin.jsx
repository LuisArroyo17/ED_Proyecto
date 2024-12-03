import { Button } from "./Button"
import { useNavigate } from "react-router-dom"

export const TitleAdmin = ({ title, onClick }) => {
  const navigate = useNavigate();
  return (
    <header className="flex justify-between py-6">
      <h2 className="text-4xl font-bold text-nowrap">{title}</h2>
      <Button
        onClick={() => navigate('/CrearProducto')} // Corregido aquí
      >
        Crear Nuevo
      </Button>
    </header>
  )
}
