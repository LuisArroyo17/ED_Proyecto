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
import OrderSuccessPage from './routes/OrderSuccessPage.jsx'
import { UserProvider } from './context/UserContext';
import ProductDetail from './routes/CreateProduct.jsx';
import ProductDetailE from './routes/ProductDetail.jsx';

createRoot(document.getElementById('root')).render(
  <UserProvider>
  {/* <StrictMode> */}
    <Router>
      <Routes>
        <Route path="/" element={<LoginForm />} />
        <Route path="/register" element={<RegisterForm />} />
        <Route path="/home" element={<UserHomePage />} />
        <Route path="/admin" element={<AdminPanelPage />} />
        <Route path="/realizarPedido" element={<OrderPage/>} />
        <Route path="/pedidoconfirmado" element={<OrderSuccessPage/>} />
        <Route path="/pedidoGestion" element={<OrderQueuePage/>} />
        <Route path="/carrito" element={<ShoppingCartPage/>} />
        <Route path="/PanelAdmin" element={<AdminPanelPage/>} />
        <Route path="/CrearProducto" element={<ProductDetail/>} />
        <Route path="/ModificarProducto" element={<ProductDetailE />} />
      </Routes>
    </Router>
  {/* </StrictMode> */}
  </UserProvider>
);
