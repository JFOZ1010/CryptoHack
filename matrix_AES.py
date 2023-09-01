matrix = [
    [99, 114, 121, 112],
    [116, 111, 123, 105],
    [110, 109, 97, 116],
    [114, 105, 120, 125],
]
ciphertext = b'\xd1O\x14j\xa4+O\xb6\xa1\xc4\x08B)\x8f\x12\xdd' # 16 bytes


def bytes2matrix(text):
    """ Converts a 16-byte array into a 4x4 matrix.  """
    #return [list(text[i:i+4]) for i in range(0, len(text), 4)]
    return [[text[i + j] for j in range(4)] for i in range(0, len(text), 4)]


def matrix2bytes(matrix):
    #Converts a 4x4 matrix into a 16-byte array

    return bytes(sum(matrix, []))

 

if __name__ == "__main__":
    matrix = bytes2matrix(ciphertext)
    for row in matrix:
       print(row)
    print("matrix: ", matrix)
    print(matrix2bytes(matrix))
