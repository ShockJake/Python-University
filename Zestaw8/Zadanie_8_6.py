# Za pomocą techniki programowania dynamicznego napisać program obliczający wartości funkcji P(i, j).
# Porównać z wersją rekurencyjną programu.

import time


def recursiveP(i, j):
    if(i == 0 and j == 0):
        return 0.5
    elif(i > 0 and j == 0):
        return 0.0
    elif(j > 0 and i == 0):
        return 1.0
    elif(i > 0 and j > 0):
        return 0.5*(recursiveP(i-1, j) + recursiveP(i, j-1))


def dynamicP(i, j):

    A = [None] * (i+1)
    for z in range(i+1):
        A[z] = [None] * (j+1)

    for x in range(i+1):
        A[x][0] = 0.0
    for x in range(j+1):
        A[0][x] = 1.0
    A[0][0] = 0.5
    x = 1
    y = 1
    for x in range(1, i+1):
        for y in range(1, j+1):
            A[x][y] = 0.5*(A[x-1][y] + A[x][y-1])

    return A[i][j]


time_of_start = time.time()
print(dynamicP(21, 7))
time_of_end = time.time()
print("Dynamic solution time: " + str(time_of_end - time_of_start))

time_of_start = time.time()
print(recursiveP(21, 7))
time_of_end = time.time()
print("Recursive solution time: " + str(time_of_end - time_of_start))
