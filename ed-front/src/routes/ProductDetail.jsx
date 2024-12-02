import { useParams , useNavigate } from 'react-router-dom';
import { useState, useEffect } from 'react';
import ONG from '../../public/ONG.png';
import Modal from '../components/Modal';

const ProductDetail = () => {
    const { id } = useParams();
    const navigate = useNavigate();
    const [data, setData] = useState({
        data: {
            categoria: null,
            descripcion: null,
            id: null,
            nombre: null,
            precio: null,
            stock: null,
            imagen: null
        }
    });
    const [showModal, setShowModal] = useState(false);
    const [modalAction, setModalAction] = useState(null);

    const handleOpenModal = (action) => {
        setModalAction(action);
        setShowModal(true);     
    };

    const handleConfirmAction = async () => {
        const url = `http://localhost:5000/productos/${id}`;
        const options = {
          method: modalAction === 'delete' ? 'DELETE' : 'PUT',
          headers: { 'Content-Type': 'application/json' },
          body: modalAction === 'update' ? JSON.stringify(data.data) : null
        };
    
        try {
          const response = await fetch(url, options);
          if (response.ok) {
            console.log(`Producto ${modalAction === 'delete' ? 'eliminado' : 'actualizado'} correctamente.`);
            navigate('/home');
          } else {
            console.error(`Error al ${modalAction === 'delete' ? 'eliminar' : 'actualizar'} el producto.`);
          }
        } catch (error) {
          console.error("Error:", error);
        } finally {
          setShowModal(false);
        }
      };
    const handleInputChange = (e) => {
        const { name, value } = e.target;
        setData(prevState => ({
            data: {
                ...prevState.data,
                [name]: value
            }
        }));
    };
    useEffect(() => {
        const cargarProducto = async () => {
            try {
                const response = await fetch(`http://localhost:5000/productos/${id}`);
                if (response.ok) {
                    const data = await response.json();
                    setData(data);
                    console.log(data);
                } else {
                    console.error("Error al cargar los productos.");
                }
            } catch (error) {
                console.error("Error:", error);
            }
        };
        cargarProducto();
    }, [id]);

    return (
        <div className='w-full h-screen grid place-content-center'>
            <div 
            onClick={() => navigate('/home')}
            className='ml-10'
            >
                <svg height="48" width="32" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 404.258 404.258"><path d="m289.927 18-24-18-151.596 202.129 151.596 202.129 24-18-138.096-184.129z"/></svg>
            </div>
            {data.data.id ? (
                <div className='flex items-center justify-center h-auto mx-10'>
                    <div className='w-1/2 p-8 m-4 max-w-[600px] max-h-[500'>
                        <img src={ONG} alt="imagen del producto" />
                    </div>
                    <div className='w-full md:w-1/2 p-4 space-y-6'>
                        <div className='block'>
                            <h1 className='text-3xl font-bold mb-2'>Título:</h1>
                            <input type="text" name="nombre" value={data.data.nombre} onChange={handleInputChange} className='text-xl w-full border border-gray-300 p-2 rounded-lg' />
                        </div>
                        <div className='flex items-center'>
                            <p className='text-xl font-bold mr-4'>Precio:</p>
                            <input type="text" name="precio" value={data.data.precio} onChange={handleInputChange} className='text-xl w-full border border-gray-300 p-2 rounded-lg' />
                        </div>
                        <div className='flex justify-between'>
                            <div className='flex items-center'>
                                <p className='text-xl font-bold mr-4'>Stock:</p>
                                <input type="text" name="stock" value={data.data.stock} onChange={handleInputChange} className='text-xl w-full border border-gray-300 p-2 rounded-lg' />
                            </div>
                            <div className='flex items-center'>
                                <p className='text-xl font-bold mr-4'>Categoria:</p>
                                <input type="text" name="categoria" value={data.data.categoria} onChange={handleInputChange} className='text-xl w-full border border-gray-300 p-2 rounded-lg' />
                            </div>
                        </div>
                        <div className='block'>
                            <p className='text-xl font-bold mb-2'>Descripción:</p>
                            <textarea name="descripcion" value={data.data.descripcion} onChange={handleInputChange} className='text-xl w-full border border-gray-300 p-2 rounded-lg' rows="4" />
                        </div>
                        <div className='flex justify-center gap-6'>
                            <button 
                            onClick={ () => handleOpenModal('delete')}
                            className='bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-4 rounded-lg'>
                                Eliminar
                            </button>
                            <button 
                            onClick={() => handleOpenModal('update')} 
                            className='bg-green-500 hover:bg-green-700 text-white font-bold py-2 px-4 rounded-lg'>Actualizar</button>
                        </div>
                    </div>
                </div>
            ) : (
                <div className='w-full h-full flex items-center justify-center'>
                    <p className='text-2xl'>No hay producto registrado</p>
                </div>
            )}
            {showModal && (
                <Modal
                onClose={() => setShowModal(false)}
                onConfirm={handleConfirmAction}
                action={modalAction}
                />
            )}
        </div>
    );
};

export default ProductDetail;
