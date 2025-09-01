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
        """
        Verifica si hay un ganador en un tablero de tic-tac-toe.
        """
        # Revisar filas
        for fila in tablero:
            if fila[0] != " " and fila[0] == fila[1] == fila[2]:
                return fila[0]

        # Revisar columnas
        for col in range(3):
            if tablero[0][col] != " " and tablero[0][col] == tablero[1][col] == tablero[2][col]:
                return tablero[0][col]

        # Revisar diagonal principal
        if tablero[0][0] != " " and tablero[0][0] == tablero[1][1] == tablero[2][2]:
            return tablero[0][0]

        # Revisar diagonal secundaria
        if tablero[0][2] != " " and tablero[0][2] == tablero[1][1] == tablero[2][0]:
            return tablero[0][2]

        # Verificar si hay espacios vacíos
        for fila in tablero:
            if " " in fila:
                return "continua"

        # Si no hay vacíos y nadie ganó → empate
        return "empate"

    
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