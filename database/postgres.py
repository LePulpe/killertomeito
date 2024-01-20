import psycopg2
from database.dbconf import DbConf

class ConSQLManager:
    def __init__(self):
        self.dbname = DbConf.DBNAME
        self.user = DbConf.USER
        self.password = DbConf.PASSWORD
        self.host = DbConf.HOST
        self.port = DbConf.PORT
        self.connection = None
        self.cursor = None

    def connect(self):
        try:
            self.connection = psycopg2.connect(
                dbname=self.dbname,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port
            )
            self.cursor = self.connection.cursor()
            print("Conexión a la base de datos PostgreSQL establecida.")
        except psycopg2.Error as e:
            print(f"Error al conectar a la base de datos PostgreSQL: {e}")

    def disconnect(self):
        if self.connection:
            self.connection.close()
            print("Conexión a la base de datos PostgreSQL cerrada.")

    def execute_query(self, query, parameters=None):
        try:
            if parameters:
                self.cursor.execute(query, parameters)
            else:
                self.cursor.execute(query)
            self.connection.commit()
            print("Consulta ejecutada correctamente.")
        except psycopg2.Error as e:
            print(f"Error al ejecutar la consulta: {e}")

    def fetch_all(self, query):
        try:
            self.cursor.execute(query)
            rows = self.cursor.fetchall()
            return rows
        except psycopg2.Error as e:
            print(f"Error al obtener los resultados: {e}")
            return None

