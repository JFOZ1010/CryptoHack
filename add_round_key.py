state = [
    [206, 243, 61, 34],
    [171, 11, 93, 31],
    [16, 200, 91, 108],
    [150, 3, 194, 51],
]

round_key = [
    [173, 129, 68, 82],
    [223, 100, 38, 109],
    [32, 189, 53, 8],
    [253, 48, 187, 78],
]


def add_round_key(s, k):
    #vamos a crear una matriz de 4x4, que almacenara el resultado de la operacion XOR, 
    #entre la matriz de estado y la clave de ronda (round_key), para eso usamos la funcion zip 
    #que nos permite iterar sobre dos listas al mismo tiempo
    matriz_resultante = [[i ^ j for i, j in zip(a, b)] for a, b in zip(s, k)] # ^ es el operador XOR
    return matriz_resultante
    #print("matriz: ", matriz_resultante)

def inv_add_round_key(s, k):
    #esta funcion lo que hara sera realizar la operacion XOR entre la matriz de estado y la clave de ronda, de forma inversa
    matriz_resultante = [[i ^ j for i, j in zip(a, b)] for a, b in zip(s, k)] # ^ es el operador XOR


def matrix2bytes(matrix):
    #Converts a 4x4 matrix into a 16-byte array
    return bytes(sum(matrix, []))


if __name__ == "__main__":
    matrix = add_round_key(state, round_key) 
    print(matrix2bytes(matrix))

