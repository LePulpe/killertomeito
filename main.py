from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from sistema.killertomeito import KillerTomeito

app = FastAPI()
kt = KillerTomeito()

class Libros(BaseModel):
    titulo: str
    autor: str
    paginas: int
    editorial: Optional[str]

@app.get("/")
def index():
    return {"message": "FastAPI firts API"}

@app.get("/libros/{id}")
def mostrar_libros(id: int):
    return {"data":id}

@app.post("/libros")
def insertar_libros(libro: Libros):
    return {"message": f"Libro {libro.titulo} insertado"}

@app.get("/tomeito")
def get_all_tometos():
    return kt.get_alltomeitos()

@app.post("/addtomeito")
def add_tomeito(name: str):
    kt.set_tomeito(name)
    return "Registro insertado correctamente"
    