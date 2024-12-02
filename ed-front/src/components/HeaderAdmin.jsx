export const HeaderAdmin = () => {
  return (
    <header className="flex justify-between items-center bg-white shadow-md p-4">
      <div className="flex items-center space-x-4">
        <button className="text-xl">
          <i className="fas fa-bars"></i>
        </button>
        <h1 className="text-2xl font-bold">Panel Admin</h1>
      </div>
      <div className="flex items-center space-x-4">
        <button className="text-red-500 font-bold">Salir</button>
      </div>
    </header>

  )
}
