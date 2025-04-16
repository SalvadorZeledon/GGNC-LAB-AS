import psycopg2
from psycopg2 import DatabaseError 
from decouple import config

def get_connection():
    try:
        host = config("PGSQL_HOST")
        user = config("PGSQL_USER")
        password = config("PGSQL_PASSWORD")
        database = config("PGSQL_DATABASE")

        print("🔧 Conectando a PostgreSQL con:")
        print(f"Host: {host}, User: {user}, DB: {database}")

        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        return connection
    except Exception as ex:
        print("❌ Error al conectar a la base de datos:", ex)
        return None
