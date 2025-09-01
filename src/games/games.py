#corrigiendo games.py
import random

class Games:
        
    def piedra_papel_tijera(self, jugador1, jugador2):
        """
        Determina el ganador del juego piedra, papel o tijera.
        """
        # Normalizar entradas (ignorar mayúsculas/minúsculas)
        j1 = jugador1.lower()
        j2 = jugador2.lower()

        # Opciones válidas
        opciones = ["piedra", "papel", "tijera"]

        # Validar entradas
        if j1 not in opciones or j2 not in opciones:
            return "invalid"

        # Caso de empate
        if j1 == j2:
            return "empate"

        # Reglas de victoria
        reglas = {
            "piedra": "tijera",   # piedra vence a tijera
            "tijera": "papel",    # tijera vence a papel
            "papel": "piedra"     # papel vence a piedra
        }

        if reglas[j1] == j2:
            return "jugador1"
        else:
            return "jugador2"

    
    def adivinar_numero_pista(self, numero_secreto, intento):
        if intento == numero_secreto:
            return "correcto"
        elif intento > numero_secreto:
            return "muy alto"
        else:
            return "muy bajo"
    
    def ta_te_ti_ganador(self, tablero):
    # Funciones auxiliares para revisar filas, columnas y diagonales
        def revisar_linea(linea):
            if linea[0] != " " and linea[0] == linea[1] == linea[2]:
                return linea[0]
            return None
        
        # Revisa filas
        for fila in tablero:
            ganador = revisar_linea(fila)
            if ganador:
                return ganador
                
        # Revisa columnas
        for j in range(3):
            columna = [tablero[i][j] for i in range(3)]
            ganador = revisar_linea(columna)
            if ganador:
                return ganador
                
        # Revisa diagonales
        diagonal1 = [tablero[i][i] for i in range(3)]
        ganador = revisar_linea(diagonal1)
        if ganador:
            return ganador
            
        diagonal2 = [tablero[i][2-i] for i in range(3)]
        ganador = revisar_linea(diagonal2)
        if ganador:
            return ganador
            
        # Revisa si hay un empate (no hay espacios vacíos)
        for fila in tablero:
            if " " in fila:
                return "continua" # Todavía hay movimientos disponibles
                
        return "empate" # No hay ganador y el tablero está lleno
    
    def generar_combinacion_mastermind(self, longitud, colores_disponibles):
        return [random.choice(colores_disponibles) for _ in range(longitud)]
    
    def validar_movimiento_torre_ajedrez(self, desde_fila, desde_col, hasta_fila, hasta_col, tablero):
        # 1. Movimiento válido: la torre debe moverse en línea recta
        # Horizontal
        es_horizontal = (desde_fila == hasta_fila) and (desde_col != hasta_col)
        # Vertical
        es_vertical = (desde_col == hasta_col) and (desde_fila != hasta_fila)

        if not es_horizontal and not es_vertical:
            return False # No es un movimiento horizontal ni vertical
            
        # 2. No puede haber piezas en el camino (revisar casillas intermedias)
        
        # Movimiento horizontal
        if es_horizontal:
            paso = 1 if hasta_col > desde_col else -1
            for col in range(desde_col + paso, hasta_col, paso):
                if tablero[desde_fila][col] != " ":
                    return False # Hay una pieza en el camino
                    
        # Movimiento vertical
        if es_vertical:
            paso = 1 if hasta_fila > desde_fila else -1
            for fila in range(desde_fila + paso, hasta_fila, paso):
                if tablero[fila][desde_col] != " ":
                    return False # Hay una pieza en el camino
                    
        # 3. La casilla de destino no puede tener una pieza del mismo color
        # Suponiendo que las piezas se representan por un carácter y los espacios vacíos por " "
        pieza_origen = tablero[desde_fila][desde_col]
        pieza_destino = tablero[hasta_fila][hasta_col]
        
        # Esta parte es una suposición de cómo se manejan los colores,
        # pero es un buen punto a considerar para la lógica completa.
        # Por ahora, solo validaremos que el camino esté libre.
        
        return True