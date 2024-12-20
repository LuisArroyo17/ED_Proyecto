import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pymysql
import pymysql.cursors

from utils.db import get_connection


class DB:
    def __init__(self):
        db = get_connection()
        try:
            cursor = db.cursor()
            cursor.execute("SHOW TABLES;")
            db_tables = cursor.fetchall()
            if len(db_tables) > 0:
                print("Tablas ya existen")
            else:
                self.crear_tablas()
        except Exception as e:
            print(f"Error {e}")

    def crear_tablas(self):
        db = get_connection()
        try:
            cursor = db.cursor()
            
            # Crear tabla productos
            cursor.execute("""
                CREATE TABLE productos (
                    id BIGINT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
                    nombre VARCHAR(100) NOT NULL,
                    categoria VARCHAR(50) NOT NULL,
                    precio NUMERIC(10, 2) NOT NULL,
                    descripcion TEXT,
                    stock INTEGER DEFAULT 0,
                    imagen VARCHAR(255)
                );
            """)
            
            # Crear tabla usuarios
            cursor.execute("""
                CREATE TABLE usuarios (
                    id BIGINT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
                    nombre VARCHAR(100) NOT NULL,
                    email VARCHAR(100) UNIQUE NOT NULL,
                    contrasena VARCHAR(255) NOT NULL,
                    rol VARCHAR(50) DEFAULT 'cliente'
                );
            """)
            
            # Crear tabla carrito_compras
            cursor.execute("""
                CREATE TABLE carrito_compras (
                    id BIGINT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
                    usuario_id BIGINT UNSIGNED NOT NULL,
                    producto_id BIGINT UNSIGNED NOT NULL,
                    cantidad INT NOT NULL,
                    FOREIGN KEY (usuario_id) REFERENCES usuarios(id),
                    FOREIGN KEY (producto_id) REFERENCES productos(id)
                );
            """)
            
            # Crear tabla pedidos
            cursor.execute("""
                CREATE TABLE pedidos (
                    id BIGINT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
                    usuario_id BIGINT UNSIGNED NOT NULL,
                    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    total NUMERIC(10, 2) NOT NULL,
                    estado VARCHAR(50) DEFAULT 'pendiente',
                    FOREIGN KEY (usuario_id) REFERENCES usuarios(id),
                    prioridad INT DEFAULT 1,
                );
            """)
            
            # Crear tabla detalle_pedidos
            cursor.execute("""
                CREATE TABLE detalle_pedidos (
                    id BIGINT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
                    pedido_id BIGINT UNSIGNED NOT NULL,
                    producto_id BIGINT UNSIGNED NOT NULL,
                    cantidad INTEGER NOT NULL,
                    precio NUMERIC(10, 2) NOT NULL,
                    FOREIGN KEY (pedido_id) REFERENCES pedidos(id),
                    FOREIGN KEY (producto_id) REFERENCES productos(id)
                );
            """)


             # Agregar esta sección en el método crear_tablas() de creartablas.py

            # Crear tabla envios
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS envios (
                    id BIGINT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
                    pedido_id BIGINT UNSIGNED NOT NULL,
                    detalles TEXT,
                    prioridad INT DEFAULT 0,
                    estado VARCHAR(50) DEFAULT 'pendiente',
                    FOREIGN KEY (pedido_id) REFERENCES pedidos(id)
                );
            """)
       
            
            db.commit()
            print("Tablas creadas")
        except Exception as e:
            print(f"Error {e}")
        finally:
            db.close()
db= DB()