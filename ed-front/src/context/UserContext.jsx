import React, { createContext, useState, useContext } from 'react';

// Creamos el contexto
const UserContext = createContext();

export const useUser = () => useContext(UserContext);

export const UserProvider = ({ children }) => {
  const [userId, setUserId] = useState(null);

  const setUser = (id) => setUserId(id);
  const logout = () => setUserId(null);

  return (
    <UserContext.Provider value={{ userId, setUser, logout }}>
      {children}
    </UserContext.Provider>
  );
};
