"""
Configuración para el empaquetado e instalación de la librería de estadísticas.

Este módulo define la configuración del paquete 'estadisticas_poo' 
para distribución e instalación via pip. Incluye metadatos del proyecto,
dependencias y estructura de paquetes.

Ejemplo de uso:
    pip install -e .  # Instalación en modo desarrollo
"""

from setuptools import setup, find_packages

# Configuración principal del paquete
setup(
    # Información básica del proyecto
    name="estadisticas-poo",
    version="1.0.0",
    
    # Metadatos descriptivos
    author="Hilary Cruz, Maria Chavez, Jean Malvacedo, Piero Mejia",
    author_email="",  # Pueden agregar emails si quieren
    description="Librería de estadísticas básicas implementada con Programación Orientada a Objetos",
    long_description="""
    Estadísticas-POO es una librería educativa que proporciona funciones estadísticas
    básicas implementadas usando paradigmas de Programación Orientada a Objetos.
    
    Características principales:
    - Cálculo de medidas de tendencia central (media, mediana, moda)
    - Cálculo de medidas de dispersión (varianza, desviación estándar)
    - Generación de datos simulados para pruebas
    - Implementación modular y extensible
    """,
    
    # Estructura de paquetes
    packages=find_packages(),
    
    # Requisitos del sistema
    python_requires=">=3.6",
    
    # Clasificaciones para PyPI (si eventualmente publican)
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Education",
        "Topic :: Scientific/Engineering :: Mathematics",
    ],
    
    # Palabras clave para búsqueda
    keywords="estadísticas, matemáticas, educación, POO, ciencia de datos",
    
    # Si tienen una URL del proyecto (GitHub)
    url="https://github.com/mar93681-jpg/Parcial-LP2",
    
    # Licencia:
    license="MIT",
)