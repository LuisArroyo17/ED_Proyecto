import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import './index.css'

import LoginForm from './routes/LoginForm.jsx'
import RegisterForm from './routes/RegisterForm.jsx' 
import UserHomePage from './routes/UserHomePage.jsx'
import OrderPage from './routes/OrderPage.jsx'
import OrderQueuePage from './routes/OrderQueuePage.jsx'
import ShoppingCartPage from './routes/ShoppingCartPage.jsx'
import AdminPanelPage from './routes/AdminPanelPage.jsx'

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <Router>
      <Routes>
        <Route path="/" element={<LoginForm />} />
        <Route path="/register" element={<RegisterForm />} />
        <Route path="/home" element={<UserHomePage />} />
        <Route path="/realizarPedido" element={<OrderPage/>} />
        <Route path="/orderQueuePage" element={<OrderQueuePage/>} />
        <Route path="/carrito" element={<ShoppingCartPage/>} />
        <Route path="/PanelAdmin" element={<AdminPanelPage/>} />

      </Routes>
    </Router>
  </StrictMode>
);
