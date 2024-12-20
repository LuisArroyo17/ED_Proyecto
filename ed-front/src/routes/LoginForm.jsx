import { useState } from "react";
import { useUser } from "../context/UserContext";
import { useNavigate } from "react-router-dom"; // Importamos useNavigate

const LoginForm = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [errorMessage, setErrorMessage] = useState("");
  const [successMessage, setSuccessMessage] = useState("");
  const { setUserId } = useUser();
  const navigate = useNavigate(); // Hook para navegar sin recargar la página

  const handleLogin = async (e) => {
    e.preventDefault();
    try {
      const response = await fetch("http://127.0.0.1:5000/login", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ email, contrasena: password }),
      });
      const data = await response.json();

      if (response.ok) {
        // Al iniciar sesión correctamente, almacenamos el ID del usuario
        setUserId(data.usuario.id);

        // Imprimimos el ID del usuario en consola
        console.log("ID del usuario:", data.usuario.id);

        if (data.usuario.rol === "admin") {
          navigate("/admin"); // Navegamos a /admin sin recargar la página
        } else {
          navigate("/home"); // Navegamos a /home sin recargar la página
        }
      } else {
        setErrorMessage(data.message || "Error al iniciar sesión");
      }
    } catch (error) {
      setErrorMessage("Hubo un problema al conectar con el servidor");
    }
  };

  return (
    <div className="flex justify-center items-center min-h-screen bg-gray-100">
      <div className="w-full max-w-sm bg-white rounded-lg shadow-md p-6">
        <h2 className="text-center text-2xl font-bold mb-4">Inicio de sesión</h2>
        <form onSubmit={handleLogin}>
          <div className="mb-4">
            <label htmlFor="email" className="block text-sm font-medium mb-2">
              Correo electrónico
            </label>
            <input
              type="email"
              id="email"
              placeholder="Correo electrónico"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              className="w-full p-2 border border-gray-300 rounded-md"
            />
          </div>
          <div className="mb-6">
            <label htmlFor="password" className="block text-sm font-medium mb-2">
              Contraseña
            </label>
            <input
              type="password"
              id="password"
              placeholder="Contraseña"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              className="w-full p-2 border border-gray-300 rounded-md"
            />
          </div>
          {errorMessage && <p className="text-red-500 text-sm mt-2">{errorMessage}</p>}
          {successMessage && <p className="text-green-500 text-sm mt-2">{successMessage}</p>}
          <button
            type="submit"
            className="w-full bg-blue-500 text-white py-2 rounded-md hover:bg-blue-600"
          >
            Iniciar sesión
          </button>
        </form>
        <button
          onClick={() => navigate("/register")} // Usamos navigate para ir a la página de registro
          className="mt-4 w-full bg-green-500 text-white py-2 rounded-md hover:bg-green-600"
        >
          Registrar
        </button>
      </div>
    </div>
  );
};

export default LoginForm;
