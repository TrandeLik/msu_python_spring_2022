#include <stdio.h>
#include <stdlib.h>
#include <time.h>

enum
{
    MATRIX_SIZE = 100,
    FIELD_CHARACTERISTICS = 100000000,
    MATRIX_COUNT = 100
};

int**
matrixAlloc(int n)
{
    int** res = malloc(sizeof(int*) * n);
    for (int i = 0; i < n; ++i) {
        res[i] = malloc(sizeof(int) * n);
    }
    return res;
}

void
matrixFree(int** matrix, int n)
{
    for (int i = 0; i < n; ++i) {
        free(matrix[i]);
    }
    free(matrix);
}

int**
matrixCpy(int** source, int size)
{
    int** res = matrixAlloc(size);
    for (int i = 0; i < size; ++i) {
        for (int j = 0; j < size; ++j) {
            res[i][j] = source[i][j];
        }
    }
    return res;
}

void
matrixMultiplication(int** first, int** second, int size, int p)
{
    int** first_copy = matrixCpy(first, size);
    for (int i = 0; i < size; ++i) {
        for (int j = 0; j < size; ++j) {
            first[i][j] = 0;
            for (int k = 0; k < size; ++k) {
                first[i][j] += ((long long)(second[i][k] % p) * (first_copy[k][j] % p)) % p;
                first[i][j] %= p;
            }
        }
    }
    matrixFree(first_copy, size);
}

void
fillMatrix(int** matrix, int size)
{
    for (int i = 0; i < size; ++i) {
        for (int j = 0; j < size; ++j) {
            matrix[i][j] = rand();
        }
    }
}

int
main(void) {
    clock_t begin = clock();
    srand(time(NULL));
    int** a = matrixAlloc(MATRIX_SIZE);
    fillMatrix(a, MATRIX_SIZE);
    for (int i = 0; i < MATRIX_COUNT; ++i) {
        int** b = matrixAlloc(MATRIX_SIZE);
        fillMatrix(b, MATRIX_SIZE);
        matrixMultiplication(a, b, MATRIX_SIZE, FIELD_CHARACTERISTICS);
        matrixFree(b, MATRIX_SIZE);
    }
    printf("C version: %lf\n", (double)(clock() - begin) / CLOCKS_PER_SEC);
}