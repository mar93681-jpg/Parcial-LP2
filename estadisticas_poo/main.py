import csv
from estadistica_cuantitativa import EstadisticaCuantitativa
from estadistica_cualitativa import EstadisticaCualitativa

# -------------------------------
# Cargar los datos desde el CSV
# -------------------------------
def cargar_datos(archivo='datos_simulados.csv'):
    """Carga los datos desde un archivo CSV y devuelve una lista de diccionarios."""
    with open(archivo, 'r', encoding='utf-8') as f:
        lector = csv.DictReader(f)
        datos = [fila for fila in lector]
    return datos


# -------------------------------
# Función polimórfica
# -------------------------------
def mostrar_resumen(objeto_estadistico):
    """Muestra el resumen, sin importar el tipo de estadística."""
    print(f'\n Resumen ({objeto_estadistico.tipo_datos()})')
    objeto_estadistico.resumen()


# -------------------------------
# Programa principal
# -------------------------------
def main():
    datos = cargar_datos()

    # -------------------------------
    # Variables cuantitativas
    # -------------------------------
    edades = [int(f['Edad']) for f in datos]
    ingresos = [float(f['Ingreso_mensual_miles']) for f in datos]
    horas = [float(f['Horas_trabajadas_por_semana']) for f in datos]
    gastos = [float(f['Gasto_mensual_miles']) for f in datos]

    # -------------------------------
    # Variables cualitativas
    # -------------------------------
    colores = [f['Color_favorito'] for f in datos]
    ocupaciones = [f['Ocupacion'] for f in datos]
    generos = [f['Genero'] for f in datos]
    estados = [f['Estado_civil'] for f in datos]

    # -------------------------------
    # Crear objetos de análisis
    # -------------------------------
    estad_edad = EstadisticaCuantitativa(edades)
    estad_ingreso = EstadisticaCuantitativa(ingresos)
    estad_horas = EstadisticaCuantitativa(horas)
    estad_gasto = EstadisticaCuantitativa(gastos)

    estad_color = EstadisticaCualitativa(colores)
    estad_ocupacion = EstadisticaCualitativa(ocupaciones)
    estad_genero = EstadisticaCualitativa(generos)
    estad_estado = EstadisticaCualitativa(estados)

    # -------------------------------
    # Mostrar resultados (polimorfismo)
    # -------------------------------
    mostrar_resumen(estad_edad)
    mostrar_resumen(estad_ingreso)
    mostrar_resumen(estad_horas)
    mostrar_resumen(estad_gasto)

    mostrar_resumen(estad_color)
    mostrar_resumen(estad_ocupacion)
    mostrar_resumen(estad_genero)
    mostrar_resumen(estad_estado)


# -------------------------------
# Ejecutar programa
# -------------------------------
if __name__ == '__main__':
    main()
    
