import pymysql
import pymysql.cursors
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path=".envvars")

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
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME"),
            cursorclass=pymysql.cursors.DictCursor
        )
        return db
    
    def crear_tablas(self):
        db = self.connection()
        cursor = db.cursor()
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
                create table if not exists client_exact
                (
                id_client_exact int auto_increment
                    primary key,
                id_client   int    not null,
                id_nodo     bigint not null,
                constraint client_exact_client_id_client_fk
                    foreign key (id_client) references client (id_client),
                constraint client_exact_nodo_id_nodo_fk
                    foreign key (id_nodo) references nodo (id_nodo)
                );
            """)
            
            cursor.execute("""
                create table if not exists driver
                (
                id_driver  int auto_increment
                    primary key,
                username   varchar(30) not null,
                password   varchar(70) not null,
                first_name varchar(50) not null,
                last_name  varchar(50) not null,
                status     varchar(20) not null,
                created_by int         not null,
                constraint driver_admin_id_admin_fk
                    foreign key (created_by) references admin (id_admin)
                );
            """)
            
            cursor.execute("""
                create table if not exists driver_client
                (
                id_driver_client int auto_increment
                    primary key,
                id_client_exact  int not null,
                id_driver        int not null,
                constraint driver_client_client_exact_id_client_exact_fk
                    foreign key (id_client_exact) references client_exact (id_client_exact),
                constraint driver_client_driver_id_driver_fk
                    foreign key (id_driver) references driver (id_driver)
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
            
            cursor.execute("""
                create table if not exists route
                (
                id_route       int auto_increment
                    primary key,
                total_distance double not null,
                id_driver      int    not null,
                constraint route_driver_id_driver_fk
                    foreign key (id_driver) references driver (id_driver)
                );
            """)
            
            cursor.execute("""
                create table if not exists point
                (
                id_point int auto_increment
                    primary key,
                id_nodo  bigint not null,
                id_route int null,
                constraint point_nodo_id_fk
                    foreign key (id_nodo) references nodo (id_nodo),
                constraint point_route_id_route_fk
                    foreign key (id_route) references route (id_route)
                );
            """)
            
            db.commit()
            print("Tablas creadas")
        except Exception as e:
            print(f"Error {e}")
        finally:
            db.close()