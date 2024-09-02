import pymysql
import pymysql.cursors
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path="../.envvars")

class DB:
    def __init__(self):
        db= self.connection()
        try:
            cursor = db.cursor()
            cursor.execute("SHOW TABLES;")
            db_tables = cursor.fetchall()
            if (db_tables.__len__() > 0):
                print("Tablas ya existen")
            else:
                self.crear_tablas()
        except Exception as e:
            print(f"Error {e}")

    def connection(self):
        db = pymysql.connections.Connection(
            host="localhost",#os.getenv("DB_HOST"),
            user="root",#os.getenv("DB_USER"),
            password="77063414",#os.getenv("DB_PASSWORD"),
            database="ed_proyecto",#os.getenv("DB_NAME"),
            cursorclass=pymysql.cursors.DictCursor
        )
        print("Conexión exitosa")
        return db

    def crear_tablas(self):
        db = self.connection()
        try:
            cursor= db.cursor()
            
            cursor.execute("""
                create table if not exists admin
                (
                id_admin   int auto_increment
                    primary key,
                username   varchar(30) not null,
                password   varchar(70) not null,
                first_name varchar(50) not null,
                last_name  varchar(50) not null
                );
            """)

            cursor.execute("""
                create table if not exists client
                (
                id_client int auto_increment
                    primary key,
                name      varchar(50) not null,
                latitud   double      not null,
                longitud  double      not null
                );
            """)

            cursor.execute("""
                create table if not exists nodo
                (
                id_nodo  bigint    not null
                    primary key,
                latitud  double not null,
                longitud double not null
                );
            """)         

            cursor.execute("""
                create table if not exists arista
                (
                id_arista int auto_increment
                    primary key,
                distancia double not null,
                origen    bigint    not null,
                destino   bigint    not null,
                constraint arista_nodo_id_fk
                    foreign key (origen) references nodo (id_nodo),
                constraint arista_nodo_id_fk_2
                    foreign key (destino) references nodo (id_nodo)
                );
            """)

            db.commit()
            print("Tablas creadas")
        except Exception as e:
            print(f"Error {e}")
        finally:
            db.close()