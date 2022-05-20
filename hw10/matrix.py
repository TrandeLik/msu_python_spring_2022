import time
import random
import copy

MATRIX_SIZE = 100
FIELD_CHARACTERISTICS = 100000000
MATRIX_COUNT = 100


def get_matrix(n):
    result = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            result[i][j] = random.randint(0, 10000)
    return result


def matrix_multiplication(first, second, size, p):
    first_copy = copy.deepcopy(first)
    for i in range(size):
        for j in range(size):
            first[i][j] = 0
            for k in range(size):
                first[i][j] += ((second[i][k] % p) * (first_copy[k][j] % p)) % p
                first[i][j] %= p


if __name__ == "__main__":
    begin = time.time()
    a = get_matrix(MATRIX_SIZE)
    for i in range(MATRIX_COUNT):
        b = get_matrix(MATRIX_SIZE)
        matrix_multiplication(a, b, MATRIX_SIZE, FIELD_CHARACTERISTICS)
    print("Python version: ", time.time() - begin)
