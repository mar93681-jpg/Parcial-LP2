import random
import csv

def generar_datos(n=200, archivo='datos_simulados.csv'):
    """Genera datos simulados y los guarda en un archivo CSV."""

    # Variables cualitativas
    colores = ['rojo', 'azul', 'verde', 'amarillo', 'negro', 'blanco', 'morado']
    ocupaciones = ['ingeniero', 'docente', 'estudiante', 'médico', 'vendedor', 'programador']
    estados_civiles = ['soltero', 'casado', 'divorciado', 'viudo']
    generos = ['masculino', 'femenino', 'otro']

    # Crear archivo CSV
    with open(archivo, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([
            'ID',
            'Edad',
            'Horas_trabajadas_por_semana',
            'Ingreso_mensual_miles',
            'Gasto_mensual_miles',
            'Color_favorito',
            'Ocupacion',
            'Estado_civil',
            'Genero'])

        # Generar datos simulados
        for i in range(1, n + 1):
            edad = random.randint(18, 65)
            horas = random.randint(20, 60)
            ingreso = round(random.uniform(1.5, 10.0), 2)
            gasto = round(random.uniform(0.8 * ingreso, ingreso), 2)
            color = random.choice(colores)
            ocupacion = random.choice(ocupaciones)
            estado = random.choice(estados_civiles)
            genero = random.choice(generos)

            writer.writerow([i,edad,horas,ingreso,gasto,color,ocupacion,estado,genero])

    print('✅ Datos simulados guardados en:', archivo)


if __name__ == '__main__':
    generar_datos()
