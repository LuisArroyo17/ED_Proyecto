import React, { createContext, useContext, useState, useEffect } from 'react';

const UserContext = createContext();

export function UserProvider({ children }) {
  // Leer el ID de usuario desde localStorage al montar el componente
  const [userId, setUserId] = useState(() => {
    // Obtener el ID de usuario desde localStorage, si existe
    const savedUserId = localStorage.getItem('userId');
    return savedUserId ? JSON.parse(savedUserId) : null;
  });

  // Guardar el ID de usuario en localStorage cuando cambie
  useEffect(() => {
    if (userId !== null) {
      localStorage.setItem('userId', JSON.stringify(userId));
    }
  }, [userId]);

  return (
    <UserContext.Provider value={{ userId, setUserId }}>
      {children}
    </UserContext.Provider>
  );
}

export function useUser() {
  return useContext(UserContext);
}
