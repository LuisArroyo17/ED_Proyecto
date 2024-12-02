import { useNavigate } from 'react-router-dom';
import { useState } from 'react';
import ONG from '../../public/ONG.png';
import Modal from '../components/Modal';

const ProductDetail = () => {
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

    const handleInputChange = (e) => {
        const { name, value, files } = e.target;
        if (name === 'imagen' && files.length > 0) {
            setData(prevState => ({
                data: {
                    ...prevState.data,
                    [name]: files[0]  // Guardar el archivo en el estado
                }
            }));
        } else {
            setData(prevState => ({
                data: {
                    ...prevState.data,
                    [name]: value
                }
            }));
        }
    };
    

    const handleConfirmAction = async () => {
        const formData = new FormData();
        for (let key in data.data) {
            formData.append(key, data.data[key]); 
        }
    
        try {
            const response = await fetch('http://localhost:5000/productos', {
                method: 'POST',
                body: formData 
            });
    
            if (response.ok) {
                navigate('/home');
            } else {
                const errorData = await response.json();  
                console.error('Error:', errorData.message);
            }
        } catch (error) {
            console.error("Error:", error);
        } finally {
            setShowModal(false);
        }
    };

    return (
        <div className='w-full h-screen grid place-content-center'>
            <div 
            onClick={() => navigate('/home')}
            className='ml-10'
            >
                <svg height="48" width="32" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 404.258 404.258"><path d="m289.927 18-24-18-151.596 202.129 151.596 202.129 24-18-138.096-184.129z"/></svg>
            </div>
                <div className='flex items-center justify-center h-auto mx-10'>
                    <div className='w-1/2 p-8 m-4 max-w-[600px] max-h-[500] w-[600px] h-full border bg-gray-200 place-content-center text-center'>
                        <input type='file' name='imagen' onChange={handleInputChange}></input>
                    </div>
                    <div className='w-full md:w-1/2 p-4 space-y-6'>
                        <div className='block'>
                            <h1 className='text-3xl font-bold mb-2'>Título:</h1>
                            <input type="text" name="nombre" onChange={handleInputChange} className='text-xl w-full border border-gray-300 p-2 rounded-lg' />
                        </div>
                        <div className='flex items-center'>
                            <p className='text-xl font-bold mr-4'>Precio:</p>
                            <input type="text" name="precio" onChange={handleInputChange} className='text-xl w-full border border-gray-300 p-2 rounded-lg' />
                        </div>
                        <div className='flex justify-between space-x-2'>
                            <div className='flex items-center'>
                                <p className='text-xl font-bold mr-4'>Stock:</p>
                                <input type="text" name="stock" onChange={handleInputChange} className='text-xl w-full border border-gray-300 p-2 rounded-lg' />
                            </div>
                            <div className='flex items-center'>
                                <p className='text-xl font-bold mr-4'>Categoria:</p>
                                <select type="text" name="categoria" onChange={handleInputChange} className='text-xl w-full border border-gray-300 p-2 rounded-lg' >
                                    <option value="" disabled selected>Categorias</option>
                                    <option value="Tecnología">Tecnología</option>
                                    <option value="Hogar">Hogar</option>
                                    <option value="Línea blanca">Línea blanca</option>
                                    <option value="Moda Hombre">Moda Hombre</option>
                                    <option value="Moda Mujer">Moda Mujer</option>
                                    <option value="Dormitorio">Dormitorio</option>
                                    <option value="Muebles">Muebles</option>
                                    <option value="Deportes">Deportes</option>
                                </select>
                            </div>
                        </div>
                        <div className='block'>
                            <p className='text-xl font-bold mb-2'>Descripción:</p>
                            <textarea name="descripcion" onChange={handleInputChange} className='text-xl w-full border border-gray-300 p-2 rounded-lg' rows="4" />
                        </div>
                        <div className='flex justify-center'>
                            <button 
                            onClick={() => handleOpenModal('create')} 
                            className='bg-green-500 hover:bg-green-700 text-white font-bold py-2 px-4 rounded-lg'>Crear</button>
                        </div>
                    </div>
                </div>
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
