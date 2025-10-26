from abc import ABC, abstractmethod

class EstadisticaBase:
    def __init__(self, datos):
        # Validar que los datos sean una lista o tupla numérica
        if not isinstance(datos, (list, tuple)):
            raise TypeError("Los datos deben estar en una lista o tupla.")
        if not all(isinstance(x, (int, float)) for x in datos):
            raise ValueError("Todos los elementos deben ser números.")
        
        self.datos = datos

    @abstractmethod
    def promedio(self): pass
    @abstractmethod
    def minimo(self): pass
    @abstractmethod
    def maximo(self): pass
    @abstractmethod
    def resumen(self): pass
    def cantidad_datos(self):
        return len(self.datos)
    def tipo_datos(self):
        return self.__class__.__name__

class EstadCB(EstadisticaBase):

    def promedio(self):
        return sum(self.datos) / len(self.datos) if self.datos else 0

    def minimo(self):
        return min(self.datos)

    def maximo(self):
        return max(self.datos)

    def resumen(self):
        print("----- RESUMEN DE DATOS -----")
        print(f"Tipo de clase: {self.tipo_datos()}")
        print(f"Cantidad de datos: {self.cantidad_datos()}")
        print(f"Valor mínimo: {self.minimo()}")
        print(f"Valor máximo: {self.maximo()}")
        print(f"Promedio: {self.promedio():.2f}")
        print("----------------------------")


