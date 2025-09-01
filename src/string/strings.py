class Strings:
    """
    Clase con métodos para manipulación y operaciones con cadenas de texto.
    Incluye funciones para manipular, validar y transformar strings.
    """
    
    def es_palindromo(self, texto):
        """
        Verifica si una cadena es un palíndromo (se lee igual de izquierda a derecha y viceversa).
        """
        texto_limpio = "".join(c.lower() for c in texto if c.isalnum())
        return texto_limpio == texto_limpio[::-1]
    
    def invertir_cadena(self, texto):
        """
        Invierte una cadena de texto sin usar slicing ni reversed().
        """
        cadena_invertida = ""
        for char in texto:
            cadena_invertida = char + cadena_invertida
        return cadena_invertida
    
    def contar_vocales(self, texto):
        """
        Cuenta el número de vocales en una cadena.
        """
        vocales = "aeiouAEIOU"
        contador = 0
        for char in texto:
            if char in vocales:
                contador += 1
        return contador
    
    def contar_consonantes(self, texto):
        """
        Cuenta el número de consonantes en una cadena.
        """
        vocales = "aeiouAEIOU"
        contador = 0
        for char in texto:
            if char.isalpha() and char not in vocales:
                contador += 1
        return contador
    
    def es_anagrama(self, texto1, texto2):
        """
        Verifica si dos cadenas son anagramas (contienen exactamente los mismos caracteres).
        """
        texto1_limpio = "".join(sorted(c.lower() for c in texto1 if c.isalnum()))
        texto2_limpio = "".join(sorted(c.lower() for c in texto2 if c.isalnum()))
        return texto1_limpio == texto2_limpio
    
    def contar_palabras(self, texto):
        """
        Cuenta el número de palabras en una cadena.
        """
        palabras = texto.split()
        return len(palabras)
    
    def palabras_mayus(self, texto):
        """
        Pon en Mayuscula la primera letra de cada palabra en una cadena.
        """
        return texto.title()
    
    import re

    def eliminar_espacios_duplicados(self, texto):
        """
        Elimina espacios duplicados en una cadena.
        """
        # Reemplaza grupos de 2 o más espacios por uno solo
        return re.sub(r' {2,}', ' ', texto)


    
    def es_numero_entero(self, texto):
        """
        Verifica si una cadena representa un número entero sin usar isdigit().
        """
        texto = texto.strip()
        if not texto:
            return False
        
        inicio = 0
        if texto[0] in ('+', '-'):
            inicio = 1
        
        for i in range(inicio, len(texto)):
            if not '0' <= texto[i] <= '9':
                return False
        
        return True
    
    def cifrar_cesar(self, texto, desplazamiento):
        """
        Aplica el cifrado César a una cadena de texto.
        """
        resultado = ""
        for char in texto:
            if 'a' <= char <= 'z':
                posicion = ord(char) - ord('a')
                nueva_posicion = (posicion + desplazamiento) % 26
                nuevo_char = chr(nueva_posicion + ord('a'))
                resultado += nuevo_char
            elif 'A' <= char <= 'Z':
                posicion = ord(char) - ord('A')
                nueva_posicion = (posicion + desplazamiento) % 26
                nuevo_char = chr(nueva_posicion + ord('A'))
                resultado += nuevo_char
            else:
                resultado += char
        return resultado
    
    def descifrar_cesar(self, texto, desplazamiento):
        """
        Descifra una cadena cifrada con el método César.
        """
        return self.cifrar_cesar(texto, -desplazamiento)
    
    def encontrar_subcadena(self, texto, subcadena):
        if not subcadena:  # Si la subcadena es vacía
            return []

        posiciones = []
        for i in range(len(texto) - len(subcadena) + 1):
            if texto[i:i + len(subcadena)] == subcadena:
                posiciones.append(i)
        return posiciones
