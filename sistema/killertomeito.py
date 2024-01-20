
from database.postgres import ConSQLManager


class KillerTomeito: 
    def __init__(self):
        self.db = ConSQLManager()
        self.db.connect()

    def get_alltomeitos(self):
        query = "SELECT * FROM tomeito"
        return self.db.fetch_all(query)

    def set_tomeito(self, nombre : str):
        insert= "INSERT INTO tomeito(nombre) VALUES(%s)"
        nombre_insert = (nombre,)  
        return self.db.execute_query(insert,nombre_insert)
    