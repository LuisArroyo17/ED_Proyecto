import { Link, useLocation } from "react-router-dom"

export function LinkItem({ link, icon, onClick, label }) {

  const location = useLocation()
  const isActive = location.pathname === link

  return (
    <Link
      onClick={onClick}
      to={link}
      className={`flex gap-2 items-center px-4 py-2 rounded hover:bg-zinc-300 transition-colors text-black ${isActive ? 'bg-zinc-300' : ''}`}
    >
      {icon}
      {label}
    </Link >
  )
}
