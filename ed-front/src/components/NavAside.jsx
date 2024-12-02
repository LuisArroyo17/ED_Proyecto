import { BoxIcon, DeliveryIcon, RouteIcon } from "../icons"
import { LinkItem } from "./LinkItem"

const links = [
  {
    link: '/gestionar-productos',
    label: 'Productos',
    icon: <BoxIcon />
  },
  {
    link: '/gestionar-envios',
    label: 'Envios',
    icon: <RouteIcon />
  },
  {
    link: '/gestionar-pedidos',
    label: 'Pedidos',
    icon: <DeliveryIcon />
  }
]

export const NavAside = () => {
  return (
    <aside className='flex flex-col items-center px-2 py-4  justify-between border-r-2'>
      <div className='flex flex-col gap-20'>
        {/* <a href='/'> */}
        {/*   <img src={logo} alt="logo" className="w-16" /> */}
        {/* </a> */}
        <nav>
          <ul className='flex flex-col gap-4 text-white'>
            {
              links.map((link) => (
                <li key={link.link}>
                  <LinkItem
                    link={`/admin${link.link}`}
                    label={link.label}
                    icon={link.icon}
                  />
                </li>
              ))
            }
          </ul>
        </nav>
      </div>
      <LinkItem
        link="/"
      // icon={<LogoutIcon />}
      // onClick={handleLogout}
      />
    </aside>
  )
}
