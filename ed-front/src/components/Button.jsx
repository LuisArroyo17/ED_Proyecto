export const Button = ({ children, onClick }) => {
  return (
    <button
      className="w-full p-2 bg-black rounded-lg focus:outline-none hover:bg-zinc-700 transition-colors max-w-44 text-white"
      onClick={onClick}
    >
      {children}
    </button>
  )
}
