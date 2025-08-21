import math

class Magic:
    """
    Clase con métodos para juegos matemáticos, secuencias especiales y algoritmos numéricos.
    Incluye implementaciones de Fibonacci, números perfectos, triangulo de pascal etc.
    """
    
    def fibonacci(self, n):
        """
        Calcula el n-ésimo número de la secuencia de Fibonacci.
        """
        if n < 0:
            return None
        if n <= 1:
            return n
        
        a, b = 0, 1
        for _ in range(n - 1):
            a, b = b, a + b
        return b
    
    def secuencia_fibonacci(self, n):
        """
        Genera los primeros n números de la secuencia de Fibonacci.
        """
        if n <= 0:
            return []
        
        lista_fib = [0]
        if n > 1:
            lista_fib.append(1)
            while len(lista_fib) < n:
                siguiente = lista_fib[-1] + lista_fib[-2]
                lista_fib.append(siguiente)
        return lista_fib
    
    def es_primo(self, n):
        """
        Verifica si un número es primo.
        """
        if n <= 1:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True
    
    def generar_primos(self, n):
        """
        Genera una lista de números primos hasta n.
        """
        primos = []
        for numero in range(2, n + 1):
            if self.es_primo(numero):
                primos.append(numero)
        return primos
    
    def es_numero_perfecto(self, n):
        """
        Verifica si un número es perfecto (igual a la suma de sus divisores propios).
        """
        if n <= 1:
            return False
            
        suma_divisores = 1
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                suma_divisores += i
                if i * i != n:
                    suma_divisores += n // i
                    
        return suma_divisores == n
    
    def triangulo_pascal(self, filas):
        """
        Genera las primeras n filas del triángulo de Pascal.
        """
        if filas <= 0:
            return []
            
        triangulo = [[1]]
        for i in range(1, filas):
            fila_anterior = triangulo[-1]
            nueva_fila = [1]
            for j in range(len(fila_anterior) - 1):
                nueva_fila.append(fila_anterior[j] + fila_anterior[j+1])
            nueva_fila.append(1)
            triangulo.append(nueva_fila)
            
        return triangulo
    
    def factorial(self, n):
        """
        Calcula el factorial de un número.
        """
        if n < 0:
            return None
        if n == 0:
            return 1
            
        resultado = 1
        for i in range(1, n + 1):
            resultado *= i
        return resultado
    
    def mcd(self, a, b):
        """
        Calcula el máximo común divisor de dos números.
        """
        while b:
            a, b = b, a % b
        return a
    
    def mcm(self, a, b):
        """
        Calcula el mínimo común múltiplo de dos números.
        """
        if a == 0 or b == 0:
            return 0
        return abs(a * b) // self.mcd(a, b)
    
    def suma_digitos(self, n):
        """
        Calcula la suma de los dígitos de un número.
        """
        suma = 0
        numero_abs = abs(n)
        for digito in str(numero_abs):
            suma += int(digito)
        return suma
    
    def es_numero_armstrong(self, n):
        """
        Verifica si un número es de Armstrong (igual a la suma de sus dígitos elevados a la potencia del número de dígitos).
        """
        if n < 0:
            return False
        
        n_str = str(n)
        num_digitos = len(n_str)
        suma = 0
        for digito in n_str:
            suma += int(digito) ** num_digitos
        
        return suma == n
    
    def es_cuadrado_magico(self, matriz):
        """
        Verifica si una matriz es un cuadrado mágico (suma igual en filas, columnas y diagonales).
        """
        if not matriz or len(matriz) == 0:
            return False
            
        n = len(matriz)
        # Calcula la suma mágica de la primera fila
        suma_magica = sum(matriz[0])
        
        # Verifica sumas de filas
        for fila in matriz:
            if sum(fila) != suma_magica:
                return False
                
        # Verifica sumas de columnas
        for j in range(n):
            suma_columna = sum(matriz[i][j] for i in range(n))
            if suma_columna != suma_magica:
                return False
                
        # Verifica diagonal principal
        suma_diag1 = sum(matriz[i][i] for i in range(n))
        if suma_diag1 != suma_magica:
            return False
            
        # Verifica diagonal secundaria
        suma_diag2 = sum(matriz[i][n-1-i] for i in range(n))
        if suma_diag2 != suma_magica:
            return False
            
        return True