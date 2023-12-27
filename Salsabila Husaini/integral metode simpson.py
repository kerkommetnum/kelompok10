def f(x):
    return x**2 + 3*x + 2

def simpson_one_third(f, a, b, n):
    if n % 2 != 0:
        raise ValueError("Jumlah subinterval harus genap untuk metode Simpson 1/3.")
    
    h = (b - a) / n
    integral_sum = f(a) + f(b)
    
    for i in range(1, n):
        if i % 2 == 0:
            integral_sum += 2 * f(a + i * h)
        else:
            integral_sum += 4 * f(a + i * h)
    
    return (h / 3) * integral_sum

while True:
    try:
        # Memasukkan batas bawah dan atas integral dari pengguna
        a = float(input("\nMasukkan nilai batas bawah a: "))
        b = float(input("Masukkan nilai batas atas b: "))
        
        # Memasukkan jumlah subinterval dari pengguna
        n = int(input("Masukkan jumlah subinterval n (genap): "))

        # Menggunakan metode Simpson 1/3
        integral_approx = simpson_one_third(f, a, b, n)

        print(f"\nPerkiraan integral dari f(x) antara {a} dan {b} dengan n = {n} adalah {integral_approx:.4f}")

        # Opsi untuk keluar dari program
        choice = input("\nApakah Anda ingin menghitung integral lagi? (y/n): ").lower()
        if choice != 'y':
            print("Program telah dihentikan.")
            break

    except Exception as e:
        print(f"Terjadi kesalahan: {e}. Silakan coba lagi.")
