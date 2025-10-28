"""
Librería de Estadísticas - POO
Autores: Hilary Cruz, Maria Chavez, Jean Malvacedo, Piero Mejia
"""
"""
Este archivo convierte la carpeta en un PAQUETE Python.
Hace que: 'from estadisticas_poo import EstadisticaCuantitativa' funcione
"""
# Importar todas las clases para que estén disponibles directamente
from .EstadisticaBase import EstadisticaBase
from .estadistica_cuantitativa import EstadisticaCuantitativa
from .estadistica_cualitativa import EstadisticaCualitativa

# Lista de lo que se exporta al hacer: from estadisticas import *
__all__ = [
    'EstadisticaBase',
    'EstadisticaCuantitativa', 
    'EstadisticaCualitativa'
]

# Información del paquete
__version__ = '1.0.0'
__author__ = 'Equipo Parcial-LP2'