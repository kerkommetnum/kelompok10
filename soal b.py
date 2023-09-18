import numpy as np
import matplotlib.pyplot as plt

# Minta pengguna untuk memasukkan fungsi f(x) sebagai string
f_str = input(
    "Masukkan fungsi f(x) sebagai string (contoh: 'np.exp(x) - x'): ")
a = float(input("Masukkan batas awal a: "))
b = float(input("Masukkan batas awal b: "))
n = 0  # Inisialisasi variabel n dengan 0

# Minta pengguna untuk memasukkan nilai toleransi (e)
e = float(input("Masukkan nilai toleransi (e): "))

# Membuat fungsi f(x) dari input pengguna


def f(x):
    return eval(f_str)


def my_bisection(f, a, b, n, e):
    if f(a) * f(b) > 0:
        raise ValueError(
            "Fungsi f(a) dan f(b) harus memiliki tanda yang berlawanan di [a, b].")

    while n > 0:  # Menggunakan n sebagai jumlah iterasi yang diinginkan
        midpoint = (a + b) / 2.0
        f_midpoint = f(midpoint)
        if f_midpoint == 0 or (b - a) / 2.0 < e:
            return midpoint
        elif f(a) * f_midpoint < 0:
            b = midpoint
        else:
            a = midpoint
        n -= 1

    return (a + b) / 2.0


n = int(input("Masukkan jumlah iterasi: "))
n_result = my_bisection(f, a, b, n, e)
print("n_result =", n_result)
print(f"f({n_result}) =", f(n_result))

# Plot fungsi
x = np.linspace(a, b, 1000)
y = f(x)
plt.plot(x, y, label=f'{f_str}')
plt.axhline(0, color='black', linestyle='--', linewidth=0.7)
plt.axvline(n_result, color='red', linestyle='--',
            linewidth=0.7, label=f'Akar: {n_result:.6f}')
plt.legend()
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Plot Fungsi dan Akarnya')
plt.grid(True)
plt.show()
