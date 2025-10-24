class EstadisticaBase:
    def __init__(self, datos):
        # Validar que los datos sean una lista o tupla numérica
        if not isinstance(datos, (list, tuple)):
            raise TypeError("Los datos deben estar en una lista o tupla.")
        if not all(isinstance(x, (int, float)) for x in datos):
            raise ValueError("Todos los elementos deben ser números.")
        
        self.datos = datos

    def cantidad_datos(self):
        """Devuelve la cantidad total de datos"""
        return len(self.datos)

    def minimo(self):
        """Devuelve el valor mínimo del conjunto de datos"""
        return min(self.datos)

    def maximo(self):
        """Devuelve el valor máximo del conjunto de datos"""
        return max(self.datos)

    def promedio(self):
        """Calcula el promedio de los datos"""
        return sum(self.datos) / len(self.datos) if self.datos else 0

    def resumen(self):
        """Muestra un resumen general de los datos"""
        print("----- RESUMEN DE DATOS -----")
        print(f"Cantidad de datos: {self.cantidad_datos()}")
        print(f"Valor mínimo: {self.minimo()}")
        print(f"Valor máximo: {self.maximo()}")
        print(f"Promedio: {self.promedio():.2f}")
        print("----------------------------")


# Ejemplo de uso
if __name__ == "__main__":
    datos = [10, 20, 30, 40, 50]
    estadistica = EstadisticaBase(datos)
    estadistica.resumen()
