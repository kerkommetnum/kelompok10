def f(x):
    return x**2 + 3*x + 2

def trapezoidal_rule(f, a, b, n):
    h = (b - a) / n
    integral_sum = f(a) + f(b)
    
    for i in range(1, n):
        integral_sum += 2 * f(a + i * h)
    
    return (h / 2) * integral_sum

while True:
    try:
        # Memasukkan batas bawah dan atas integral dari pengguna
        a = float(input("\nMasukkan nilai batas bawah a: "))
        b = float(input("Masukkan nilai batas atas b: "))
        
        # Memasukkan jumlah subinterval dari pengguna
        n = int(input("Masukkan jumlah subinterval n: "))

        # Menggunakan metode trapesium
        integral_approx = trapezoidal_rule(f, a, b, n)

        print(f"\nPerkiraan integral dari f(x) antara {a} dan {b} dengan n = {n} adalah {integral_approx:.4f}")

        # Opsi untuk keluar dari program
        choice = input("\nApakah Anda ingin menghitung integral lagi? (y/n): ").lower()
        if choice != 'y':
            print("Program telah dihentikan.")
            break

    except Exception as e:
        print(f"Terjadi kesalahan: {e}. Silakan coba lagi.")
