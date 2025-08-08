from fastapi import FastAPI, Query
from typing import List, Optional
from pydantic import BaseModel
from enum import Enum

app = FastAPI(title="Servicio de Consulta de Inmuebles")


# Estados permitidos para mostrar
class EstadoInmueble(str, Enum):
    pre_venta = "pre_venta"
    en_venta = "en_venta"
    vendido = "vendido"


# Modelo de respuesta
class Inmueble(BaseModel):
    inmueble_id: int
    direccion: str
    ciudad: str
    estado: EstadoInmueble
    precio_venta: float
    descripcion: str
    anio_construccion: int
    total_me_gusta: int


# Base de datos simulada
INMUEBLES_DB = [
    {
        "inmueble_id": 1,
        "direccion": "Calle 100 #48a-47",
        "ciudad": "Bogotá",
        "estado": "en_venta",
        "precio_venta": 580000000,
        "descripcion": "Apartamento nuevo con terraza",
        "anio_construccion": 2024,
        "total_me_gusta": 150
    },
    {
        "inmueble_id": 2,
        "direccion": "Av. la Esperanza #742",
        "ciudad": "Medellín",
        "estado": "vendido",
        "precio_venta": 120000000,
        "descripcion": "Apartamento duplex amplio con vista al parque.",
        "anio_construccion": 2005,
        "total_me_gusta": 360
    },
    {
        "inmueble_id": 3,
        "direccion": "Cra 68 #32-25",
        "ciudad": "Cartagena",
        "estado": "pre_venta",
        "precio_venta": 678000000,
        "descripcion": "Apartamento al frente de la playa.",
        "anio_construccion": 2012,
        "total_me_gusta": 54
    },
    {
        "inmueble_id": 4,
        "direccion": "Cra 13 #44-39",
        "ciudad": "Bogotá",
        "estado": "reservado",  # No debe aparecer
        "precio_venta": 280000000,
        "descripcion": "Apartaestudio moderno en Chapinero.",
        "anio_construccion": 2010,
        "total_me_gusta": 580
    },
]


@app.get("/inmuebles", response_model=List[Inmueble])
def consultar_inmuebles(
    estado: Optional[List[EstadoInmueble]] = Query(None),
    ciudad: Optional[str] = None,
    anio_construccion: Optional[int] = None,
):
    # Descripción que sirve como documentación interna del método.
    """
    Consulta de inmuebles disponibles, vendidos o en pre_venta.
    Filtros: estado, ciudad y año de construcción.
    """
    # filtrado inicial
    inmuebles_visibles = [
        inmueble
        for inmueble in INMUEBLES_DB
        if inmueble["estado"] in EstadoInmueble.__members__
    ]
    
    # filtro por estado
    if estado:
        inmuebles_visibles = [
            i for i in inmuebles_visibles if i["estado"] in estado
        ]
        
    # filtro por estado
    if ciudad:
        inmuebles_visibles = [
            i for i in inmuebles_visibles if i["ciudad"].lower() == ciudad.lower()
        ]
        
    # filtro por anio
    if anio_construccion:
        inmuebles_visibles = [
            i
            for i in inmuebles_visibles
            if i["anio_construccion"] == anio_construccion
        ]

    return inmuebles_visibles