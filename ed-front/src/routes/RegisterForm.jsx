import { useState } from "react";

const RegisterForm = () => {
  const [nombre, setNombre] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [rol, setRol] = useState("cliente"); // Rol por defecto
  const [errorMessage, setErrorMessage] = useState("");
  const [successMessage, setSuccessMessage] = useState("");

  const handleRegister = async (e) => {
    e.preventDefault();
    try {
      const response = await fetch("http://127.0.0.1:5000/register", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ nombre, email, contrasena: password, rol }),
      });
      const data = await response.json();

      if (response.ok) {
        setSuccessMessage(data.message || "Usuario registrado exitosamente");
        setErrorMessage("");
        setNombre("");
        setEmail("");
        setPassword("");
      } else {
        setErrorMessage(data.message || "Error al registrar usuario");
        setSuccessMessage("");
      }
    } catch (error) {
      setErrorMessage("Hubo un problema al conectar con el servidor");
      setSuccessMessage("");
    }
  };

  return (
    <div className="flex justify-center items-center min-h-screen bg-gray-100">
      <div className="w-full max-w-sm bg-white rounded-lg shadow-md p-6">
        <h2 className="text-center text-2xl font-bold mb-4">Registrar usuario</h2>
        <form onSubmit={handleRegister}>
          <div className="mb-4">
            <label htmlFor="nombre" className="block text-sm font-medium mb-2">
              Nombre
            </label>
            <input
              type="text"
              id="nombre"
              placeholder="Nombre completo"
              value={nombre}
              onChange={(e) => setNombre(e.target.value)}
              className="w-full p-2 border border-gray-300 rounded-md"
            />
          </div>
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
          <div className="mb-4">
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
          <div className="mb-4">
            <label htmlFor="rol" className="block text-sm font-medium mb-2">
              Rol (opcional)
            </label>
            <select
              id="rol"
              value={rol}
              onChange={(e) => setRol(e.target.value)}
              className="w-full p-2 border border-gray-300 rounded-md"
            >
              <option value="cliente">Cliente</option>
              <option value="admin">Admin</option>
            </select>
          </div>
          {errorMessage && (
            <p className="text-red-500 text-sm mt-2">{errorMessage}</p>
          )}
          {successMessage && (
            <p className="text-green-500 text-sm mt-2">{successMessage}</p>
          )}
          <button
            type="submit"
            className="w-full bg-green-500 text-white py-2 rounded-md hover:bg-green-600"
          >
            Registrar
          </button>
        </form>
        <button
          onClick={() => (window.location.href = "/")}
          className="mt-4 w-full bg-blue-500 text-white py-2 rounded-md hover:bg-blue-600"
        >
          Volver al inicio
        </button>
      </div>
    </div>
  );
};

export default RegisterForm;
