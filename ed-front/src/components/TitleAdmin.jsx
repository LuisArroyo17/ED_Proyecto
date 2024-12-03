import { Button } from "./Button"

export const TitleAdmin = ({ title, onClick }) => {
  return (
    <header className="flex justify-between py-6">
      <h2 className="text-4xl font-bold text-nowrap">{title}</h2>
      <Button
        onClick={onClick}
      >
        Crear Nuevo
      </Button>
    </header>
  )
}
