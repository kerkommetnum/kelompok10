import numpy as np

def LU_decomposition(A):
    n = len(A)
    L = np.zeros((n, n))
    U = np.zeros((n, n))

    for i in range(n):
        L[i][i] = 1

        for j in range(i, n):
            U[i][j] = A[i][j] - sum(L[i][k] * U[k][j] for k in range(i))

        for j in range(i + 1, n):
            L[j][i] = (A[j][i] - sum(L[j][k] * U[k][i] for k in range(i))) / U[i][i]

    return L, U

def solve_LU(L, U, b):
    n = len(L)
    y = np.zeros(n)
    x = np.zeros(n)

    for i in range(n):
        y[i] = b[i] - sum(L[i][j] * y[j] for j in range(i))

    for i in range(n - 1, -1, -1):
        x[i] = (y[i] - sum(U[i][j] * x[j] for j in range(i + 1, n))) / U[i][i]

    return y, x

# Input matriks koefisien A
n = int(input("Masukkan ukuran matriks A (n): "))
A = np.zeros((n, n))
print("Masukkan elemen matriks A:")
for i in range(n):
    A[i] = [float(x) for x in input().split()]

# Input vektor hasil b
print("Masukkan vektor hasil b:")
b = np.array([float(x) for x in input().split()])

# Melakukan dekomposisi LU
L, U = LU_decomposition(A)

# Menyelesaikan SPL dengan metode LU
y, x = solve_LU(L, U, b)

print("Matriks L:")
print(L)
print("Matriks U:")
print(U)
print("Vektor Y:")
print(y)
print("Solusi X:")
print(x)