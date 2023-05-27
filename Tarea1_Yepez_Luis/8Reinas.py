class EightQueensHeuristic:
    def __init__(self):
        self.size = 8  # Tamaño del tablero

    def evaluate(self, state):
        collisions = 0  # Contador de colisiones

        for i in range(self.size):
            for j in range(i + 1, self.size):
                # Verificar si hay colisión entre las reinas
                if state[i] == state[j]:
                    collisions += 1  # Sumar 1 por cada colisión en la misma columna
                elif abs(state[i] - state[j]) == abs(i - j):
                    collisions += 1  # Sumar 1 por cada colisión en diagonal

        return collisions

def print_board(board):
    size = len(board)

    # Imprimir los números de las casillas superiores
    print("  ", end="")
    for i in range(size):
        print(i, end=" ")
    print()

    # Imprimir la parte superior de la cuadrícula
    print("+" + "-" * (2*size - 1) + "+")

    # Imprimir las filas del tablero
    for row in range(size):
        line = str(row) + "|"
        for col in range(size):
            if board[row] == col:
                line += "Q|"
            else:
                line += " |"
        print(line)

    # Imprimir la parte inferior de la cuadrícula
    print("+" + "-" * (2*size - 1) + "+")

def main():
    heuristic = EightQueensHeuristic()

    # Ejemplo 1: Solución incorrecta
    state1 = [0, 1, 2, 3, 4, 5, 6, 6]
    collisions1 = heuristic.evaluate(state1)
    print("Ejemplo 1 - Solución incorrecta")
    print("Cantidad de colisiones:", collisions1)
    print("Tablero:")
    print_board(state1)
    print()

    # Ejemplo 2: Solución incorrecta
    state2 = [0, 0, 0, 0, 0, 0, 0, 0]
    collisions2 = heuristic.evaluate(state2)
    print("Ejemplo 2 - Solución incorrecta")
    print("Cantidad de colisiones:", collisions2)
    print("Tablero:")
    print_board(state2)
    print()

    # Ejemplo 3: Solución correcta
    state3 = [0, 4, 7, 5, 2, 6, 1, 3]
    collisions3 = heuristic.evaluate(state3)
    print("Ejemplo 3 - Solución correcta")
    print("Cantidad de colisiones:", collisions3)
    print("Tablero:")
    print_board(state3)
    print()

    # Justificación del método heurístico utilizado
    print("Justificación del método heurístico:")
    print("El método heurístico utilizado evalúa un estado del tablero")
    print("de las 8 reinas contando las colisiones entre las reinas.")
    print("Cada vez que dos reinas están en la misma columna o en la misma diagonal,")
    print("se incrementa el contador de colisiones. Una solución válida y sin colisiones")
    print("tendrá un contador de colisiones igual a cero. El objetivo es encontrar")
    print("una configuración de las reinas con la menor cantidad de colisiones posible.")
    print("En este caso, el método heurístico se basa en la evaluación de colisiones")
    print("y no garantiza encontrar la solución óptima, pero puede ayudar a guiar")
    print("la búsqueda de soluciones válidas.")
    print()

if __name__ == "__main__":
    main()
