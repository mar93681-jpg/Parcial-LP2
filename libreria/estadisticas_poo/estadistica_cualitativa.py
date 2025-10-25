#Creación de subclase para Estadísticas Cualitativas
from EstadisticaBase import EstadisticaBase

class EstadisticaCualitativa(EstadisticaBase):
    
    def __init__(self, datos):
        
        if not isinstance(datos, (list, tuple)):
            raise TypeError("Los datos deben estar en una lista o tupla.")
        self.datos = datos

    # --- Implementación de nuevos métodos ---

    def moda(self):
        if not self.datos:
            return []
            
        frecuencias = self.tabla_frecuencias()
        
        if not frecuencias:
            return []

        # Encontrar la frecuencia máxima
        max_freq = max(frecuencias.values())

        # Recolectar todas las claves que tengan esa frecuencia máxima
        modas = [k for k, v in frecuencias.items() if v == max_freq]
        
        return modas

    def tabla_frecuencias(self):
        
        frecuencias = {}
        for item in self.datos:
            if item in frecuencias:
                frecuencias[item] += 1
            else:
                frecuencias[item] = 1
        return frecuencias

    # --- Sobrescritura de métodos incompatibles ---

    def promedio(self):
        return None

    def minimo(self):
        try:
            return min(self.datos) if self.datos else None
        except TypeError:
            return "N/A (tipos mixtos)"

    def maximo(self):
        try:
            return max(self.datos) if self.datos else None
        except TypeError:
            return "N/A (tipos mixtos)"

    def resumen(self):
        
        print("----- RESUMEN DE DATOS (CUALITATIVOS) -----")
        print(f"Cantidad de datos: {self.cantidad_datos()}")
        
        mods = self.moda()
        print(f"Moda(s): {', '.join(map(str, mods)) if mods else 'N/A'}")

        print("\n--- Tabla de Frecuencias ---")
        frecuencias = self.tabla_frecuencias()
        
        if not frecuencias:
            print("No hay datos.")
        else:
            
            frecuencias_ordenadas = sorted(
                frecuencias.items(), 
                key=lambda par: par[1], 
                reverse=True
            )
            
            for item, cuenta in frecuencias_ordenadas:
                print(f"  - {item}: {cuenta}")
        
        print("-----------------------------------------------------")

#Ejemplo de uso de la nueva subclase
if __name__ == "__main__":
    print("--- EJEMPLO: DATOS CUALITATIVOS (STRINGS)  ---")
    datos_colores = ["rojo", "azul", "verde", "rojo", "azul", "rojo", "amarillo", "verde"]
    est_cualitativa = EstadisticaCualitativa(datos_colores)
    est_cualitativa.resumen()

    print("\n--- EJEMPLO: DATOS CUALITATIVOS (NÚMEROS)  ---")
    datos_categorias_num = [1, 2, 5, 2, 1, 5, 5, 3, 2, 5]
    est_cualitativa_num = EstadisticaCualitativa(datos_categorias_num)
    est_cualitativa_num.resumen()
