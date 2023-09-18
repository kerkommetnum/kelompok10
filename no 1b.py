import numpy as np


def f(x):
    return np.exp(x) - x


a = -1  # Batas awal a
b = 1   # Batas awal b
e = 2.718  # Toleransi yang lebih kecil (gunakan notasi ilmiah)


def my_bisection(f, a, b, e):
    if np.sign(f(a)) == np.sign(f(b)):
        raise Exception('Tidak ada akar pada interval a dan b')

    while (b - a) / 2.0 > e:
        midpoint = (a + b) / 2.0
        f_midpoint = f(midpoint)
        if f_midpoint == 0:
            return midpoint
        elif np.sign(f(a)) * np.sign(f_midpoint) < 0:
            b = midpoint
        else:
            a = midpoint

    return (a + b) / 2.0


r1 = my_bisection(f, a, b, e)
print("r1 =", r1)
print("f(r1) =", f(r1))
