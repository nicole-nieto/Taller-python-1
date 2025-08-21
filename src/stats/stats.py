import math
from collections import Counter

class Stats:
    def promedio(self, numeros):
        """
        Calcula la media aritmética de una lista de números.
        """
        if not numeros:
            return 0.0
        return sum(numeros) / len(numeros)
    
    def mediana(self, numeros):
        """
        Encuentra el valor mediano de una lista de números.
        """
        if not numeros:
            return None
        
        numeros_ordenados = sorted(numeros)
        n = len(numeros_ordenados)
        indice_medio = n // 2
        
        if n % 2 == 1:
            # Si la lista tiene un número impar de elementos
            return float(numeros_ordenados[indice_medio])
        else:
            # Si la lista tiene un número par de elementos
            valor1 = numeros_ordenados[indice_medio - 1]
            valor2 = numeros_ordenados[indice_medio]
            return (valor1 + valor2) / 2.0
    
    def moda(self, numeros):
        """
        Encuentra el valor que aparece con mayor frecuencia en la lista.
        """
        if not numeros:
            return None
            
        # Contamos la frecuencia de cada número
        contador = Counter(numeros)
        
        # Encontramos la frecuencia máxima
        max_frecuencia = max(contador.values())
        
        # Buscamos el primer número que tenga esa frecuencia máxima
        for numero in numeros:
            if contador[numero] == max_frecuencia:
                return numero
    
    def desviacion_estandar(self, numeros):
        """
        Calcula la desviación estándar de una lista de números.
        """
        if not numeros:
            return 0.0
            
        n = len(numeros)
        media = self.promedio(numeros)
        
        # Calcula la suma de los cuadrados de las diferencias
        suma_diferencias = sum([(x - media) ** 2 for x in numeros])
        
        # Varianza poblacional
        varianza = suma_diferencias / n
        
        return math.sqrt(varianza)
    
    def varianza(self, numeros):
        """
        Calcula la varianza de una lista de números.
        """
        if not numeros:
            return 0.0
            
        n = len(numeros)
        media = self.promedio(numeros)
        
        # Calcula la suma de los cuadrados de las diferencias
        suma_diferencias = sum([(x - media) ** 2 for x in numeros])
        
        # Varianza poblacional
        return suma_diferencias / n
    
    def rango(self, numeros):
        """
        Calcula el rango (diferencia entre el valor máximo y mínimo).
        """
        if not numeros:
            return 0
        return max(numeros) - min(numeros)