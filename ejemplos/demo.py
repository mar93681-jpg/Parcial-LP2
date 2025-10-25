
from estadisticas_poo import EstadisticaCuantitativa, EstadisticaCualitativa

# Prueba para cuantitativa
datos_numeros = [10, 20, 30, 40, 50]
estadistica_num = EstadisticaCuantitativa(datos_numeros)
print("¡Funciona! Media:", estadistica_num.media())

# Prueba para cualitativa  
datos_colores = ["rojo", "azul", "rojo", "verde"]
estadistica_color = EstadisticaCualitativa(datos_colores)
print("Moda:", estadistica_color.moda())