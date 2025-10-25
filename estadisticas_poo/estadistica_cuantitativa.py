from abc import ABC, abstractmethod
import math

# --- CLASE BASE ---
class EstadisticaBase(ABC):
    def __init__(self, datos):
        if not isinstance(datos, (list, tuple)):
            raise TypeError("Los datos deben estar en una lista o tupla.")
        self.datos = list(datos)
    
    @abstractmethod
    def promedio(self): pass
    @abstractmethod
    def minimo(self): pass
    @abstractmethod
    def maximo(self): pass
    @abstractmethod
    def resumen(self): pass
    def cantidad_datos(self): return len(self.datos)
    def tipo_datos(self): return self.__class__.__name__

# --- CLASE CUANTITATIVA COMPLETA ---
class EstadisticaCuantitativa(EstadisticaBase):
    def __init__(self, datos):
        if not isinstance(datos, (list, tuple)):
            raise TypeError("Los datos deben estar en una lista o tupla.")
        for dato in datos:
            if not isinstance(dato, (int, float)):
                raise TypeError(f"Todos los datos deben ser numéricos. Encontrado: {type(dato)}")
        self.datos = list(datos)
        self._datos_ordenados = None
    
    def _ordenar_datos(self):
        if self._datos_ordenados is None:
            self._datos_ordenados = sorted(self.datos)
        return self._datos_ordenados
    
    def media(self):
        if not self.datos: return None
        return sum(self.datos) / len(self.datos)
    
    def mediana(self):
        if not self.datos: return None
        datos_ordenados = self._ordenar_datos()
        n = len(datos_ordenados)
        if n % 2 == 1: return datos_ordenados[n // 2]
        else: return (datos_ordenados[n // 2 - 1] + datos_ordenados[n // 2]) / 2
    
    def moda(self):
        if not self.datos: return []
        frecuencias = {}
        for dato in self.datos:
            frecuencias[dato] = frecuencias.get(dato, 0) + 1
        max_freq = max(frecuencias.values())
        return [k for k, v in frecuencias.items() if v == max_freq]
    
    def varianza(self, poblacional=True):
        if len(self.datos) < 2: return None
        media_val = self.media()
        n = len(self.datos)
        divisor = n if poblacional else n - 1
        return sum((x - media_val) ** 2 for x in self.datos) / divisor
    
    def desviacion_estandar(self, poblacional=True):
        varianza_val = self.varianza(poblacional)
        return math.sqrt(varianza_val) if varianza_val is not None else None
    
    def rango(self):
        if not self.datos: return None
        return self.maximo() - self.minimo()
    
    def rango_intercuartilico(self):
        q1, q3 = self.percentil(25), self.percentil(75)
        return q3 - q1 if q1 and q3 else None
    
    def percentil(self, percentil):
        if not self.datos: return None
        if percentil < 0 or percentil > 100:
            raise ValueError("El percentil debe estar entre 0 y 100")
        datos_ordenados = self._ordenar_datos()
        n = len(datos_ordenados)
        pos = (percentil / 100) * (n - 1)
        pos_entera = int(pos)
        pos_decimal = pos - pos_entera
        if pos_entera == n - 1: return datos_ordenados[-1]
        else: return (datos_ordenados[pos_entera] * (1 - pos_decimal) + datos_ordenados[pos_entera + 1] * pos_decimal)
    
    def cuartiles(self):
        return (self.percentil(25), self.percentil(50), self.percentil(75))
    
    def coeficiente_variacion(self):
        media_val, desv_estandar = self.media(), self.desviacion_estandar()
        if not media_val or not desv_estandar or media_val == 0: return None
        return (desv_estandar / media_val) * 100
    
    # --- MÉTODOS OBLIGATORIOS ---
    def minimo(self): return min(self.datos) if self.datos else None
    def maximo(self): return max(self.datos) if self.datos else None
    def promedio(self): return self.media()
    def resumen(self):
        print("=" * 50)
        print("     RESUMEN ESTADÍSTICAS CUANTITATIVAS")
        print("=" * 50)
        if not self.datos:
            print("No hay datos para analizar.")
            return
        print(f"Cantidad: {self.cantidad_datos()}")
        print(f"Mínimo: {self.minimo():.2f}")
        print(f"Máximo: {self.maximo():.2f}")
        print(f"Rango: {self.rango():.2f}")
        print("\n--- TENDENCIA CENTRAL ---")
        print(f"Media: {self.media():.2f}")
        print(f"Mediana: {self.mediana():.2f}")
        print(f"Moda: {self.moda()}")
        print("\n--- DISPERSIÓN ---")
        print(f"Varianza: {self.varianza():.2f}")
        print(f"Desviación: {self.desviacion_estandar():.2f}")
        print(f"Coef. variación: {self.coeficiente_variacion():.2f}%")
        print("\n--- CUARTILES ---")
        q1, q2, q3 = self.cuartiles()
        print(f"Q1: {q1:.2f}, Q2: {q2:.2f}, Q3: {q3:.2f}")
        print(f"IQR: {self.rango_intercuartilico():.2f}")
        print("=" * 50)

print("CLASE CUANTITATIVA")

# --- PRUEBA INMEDIATA ---
print("\nProbando la clase:")
datos = [23, 45, 67, 12, 89, 45, 23, 67, 45, 78, 90, 34, 56]
estadistica = EstadisticaCuantitativa(datos)
print("Creado exitosamente uu")
estadistica.resumen()
