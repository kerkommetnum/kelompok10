import numpy as np


def f(x):
    return x**3 - 2*x + 1


a = -2  # Batas awal a
b = 0  # Batas awal b
toleransi = 0.01
if np.sign(f(a)) == np.sign(f(b)):
    raise Exception('Tidak ada akar pada interval a dan b')


def my_bisection(f, a, b, tol):
    if f(a) * f(b) > 0:
        raise ValueError(
            "Fungsi f(a) dan f(b) harus memiliki tanda yang berlawanan di [a, b].")

    while (b - a) / 2.0 > tol:
        midpoint = (a + b) / 2.0
        # Evaluasi f(midpoint) sekali saja untuk efisiensi
        f_midpoint = f(midpoint)
        if f_midpoint == 0:
            return midpoint
        elif f(a) * f_midpoint < 0:
            b = midpoint
        else:
            a = midpoint

    return (a + b) / 2.0


r1 = my_bisection(f, a, b, toleransi)
print("r1 =", r1)
print("f(r1) =", f(r1))
