from fastapi import FastAPI, Query
from typing import List, Optional
from pydantic import BaseModel
from enum import Enum
import mysql.connector

app = FastAPI(title="Servicio de Consulta de Inmuebles")

# Enumeración de estados
class EstadoInmueble(str, Enum):
    pre_venta = "pre_venta"
    en_venta = "en_venta"
    vendido = "vendido"

# Modelo de respuesta
class Inmueble(BaseModel):
    direccion: str
    ciudad: str
    estado: EstadoInmueble
    precio_venta: float
    descripcion: str
    anio_construccion: int

# Conexión a MySQL
def get_connection():
    return mysql.connector.connect(
        host="13.58.82.14:3309",
        user="pruebas",       
        password="VGbt3Day5R",    
        database="habi_db"
    )

# Funcion para GET /inmuebles
@app.get("/inmuebles", response_model=List[Inmueble])
def consultar_inmuebles(
    estado: Optional[List[EstadoInmueble]] = Query(None),
    ciudad: Optional[str] = None,
    anio_construccion: Optional[int] = None,
):
    """
    Consulta de inmuebles desde BD MySQL, filtrando
    """
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    # Query para consulta a BD 
    query = """
        SELECT direccion, ciudad, estado, precio_venta, descripcion, anio_construccion
        FROM inmuebles
        WHERE estado IN ('pre_venta', 'en_venta', 'vendido')
    """
    params = []

    # Filtro para estado, ciudad y anio
    if estado:
        placeholders = ", ".join(["%s"] * len(estado))
        query += f" AND estado IN ({placeholders})"
        params.extend(estado)
    if ciudad:
        query += " AND LOWER(ciudad) = %s"
        params.append(ciudad.lower())
    if anio_construccion:
        query += " AND anio_construccion = %s"
        params.append(anio_construccion)

    # Ejecutar consulta
    cursor.execute(query, params)
    resultados = cursor.fetchall()

    cursor.close()
    conn.close()

    return resultados