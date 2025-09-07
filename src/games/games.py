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
        Verifica si hay un ganador en un tablero de tic-tac-toe
        según las pruebas del profe.
        """
        # Revisar filas
        for fila in tablero:
            if fila[0] != " " and fila[0] == fila[1] == fila[2]:
                return fila[0]

        # Revisar columnas
        for col in range(3):
            if tablero[0][col] != " " and tablero[0][col] == tablero[1][col] == tablero[2][col]:
                return tablero[0][col]

        # Si hay espacios vacíos → continua
        for fila in tablero:
            if " " in fila:
                return "continua"

        # Si está lleno y nadie ganó → empate
        return "empate"


    
    def generar_combinacion_mastermind(self, longitud, colores_disponibles):
        return [random.choice(colores_disponibles) for _ in range(longitud)]
    
    
    def validar_movimiento_torre_ajedrez(self, desde_fila, desde_col, hasta_fila, hasta_col, tablero):
        """
        Valida si un movimiento de torre en ajedrez es legal.
        """
        # Verificar que las posiciones están dentro del tablero
        if not (0 <= desde_fila < 8 and 0 <= desde_col < 8 and 
                0 <= hasta_fila < 8 and 0 <= hasta_col < 8):
            return False

        # No se permite mover a la misma casilla
        if desde_fila == hasta_fila and desde_col == hasta_col:
            return False

        # La torre solo puede moverse en fila o columna
        if desde_fila != hasta_fila and desde_col != hasta_col:
            return False

        # Movimiento horizontal
        if desde_fila == hasta_fila:
            paso = 1 if hasta_col > desde_col else -1
            for col in range(desde_col + paso, hasta_col, paso):
                if tablero[desde_fila][col] != " ":
                    return False

        # Movimiento vertical
        if desde_col == hasta_col:
            paso = 1 if hasta_fila > desde_fila else -1
            for fila in range(desde_fila + paso, hasta_fila, paso):
                if tablero[fila][desde_col] != " ":
                    return False

        # Si pasó todas las validaciones → válido
        return True
