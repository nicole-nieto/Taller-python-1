#corrigiendo errores en las pruebas de data.py
class Data:


    def invertir_lista(self, lista):
        # Usamos dos punteros: uno al inicio y otro al final, intercambiamos hasta la mitad
        inicio, fin = 0, len(lista) - 1
        while inicio < fin:
            lista[inicio], lista[fin] = lista[fin], lista[inicio]
            inicio += 1
            fin -= 1
        return lista
    
    def buscar_elemento(self, lista, elemento):
        # Recorrer la lista y comparar manualmente
        for i in range(len(lista)):
            if lista[i] == elemento:
                return i
        return -1
    
    def eliminar_duplicados(self, lista):
        # Convertimos la lista a un conjunto para eliminar duplicados.
        # Un conjunto es una colección de elementos únicos y desordenados.
        conjunto_sin_duplicados = set(lista)
        # Convertimos el conjunto de nuevo a una lista para mantener la estructura deseada.
        lista_sin_duplicados = list(conjunto_sin_duplicados)
        return lista_sin_duplicados
    
    def merge_ordenado(self, lista1, lista2):
        # Combinar usando el patrón "dos punteros"
        i, j = 0, 0
        resultado = []
        while i < len(lista1) and j < len(lista2):
            if lista1[i] < lista2[j]:
                resultado.append(lista1[i])
                i += 1
            else:
                resultado.append(lista2[j])
                j += 1
        resultado.extend(lista1[i:])
        resultado.extend(lista2[j:])
        return resultado

    def rotar_lista(self, lista, k):
        if not lista:
            return []
        n = len(lista)
        k = k % n  # Maneja rotaciones mayores al tamaño de la lista
        # Divide la lista en dos partes: los últimos k elementos y los primeros n-k
        # Luego los une en el orden correcto
        parte_final = lista[n-k:]
        parte_inicial = lista[:n-k]
        
        return parte_final + parte_inicial  

    def encuentra_numero_faltante(self, lista):
        # Usamos la fórmula de la suma de 1..n y restamos la suma de la lista
        n = len(lista) + 1  # porque falta un número
        suma_total = n * (n + 1) // 2
        return suma_total - sum(lista)
    
    def es_subconjunto(self, conjunto1, conjunto2):
        for elemento in conjunto1:
            if elemento not in conjunto2:
                return False
        return True
    
    def implementar_pila(self):
        pila = []
        return {
            "push": lambda x: pila.append(x),
            "pop": lambda: pila.pop() if pila else None,
            "peek": lambda: pila[-1] if pila else None,
            "is_empty": lambda: len(pila) == 0
        }
    
    def implementar_cola(self):
        cola = []
        return {
            "enqueue": lambda x: cola.append(x),
            "dequeue": lambda: cola.pop(0) if cola else None,
            "peek": lambda: cola[0] if cola else None,
            "is_empty": lambda: len(cola) == 0
        }

    
    def matriz_transpuesta(self, matriz):
        if not matriz or not matriz[0]:
            return []
        # Usamos zip() para agrupar los elementos de cada columna y luego
        # creamos una lista de listas con el resultado.
        return [list(fila) for fila in zip(*matriz)]