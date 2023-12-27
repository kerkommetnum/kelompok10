def forward_difference(f, x, h):
    return (f(x + h) - f(x)) / h

while True:
    # Memasukkan persamaan fungsinya dari pengguna
    equation = input("\nMasukkan persamaan f(x) atau ketik 'exit' untuk keluar (gunakan x sebagai variabel): ")
    
    if equation.lower() == 'exit':
        print("Program telah dihentikan.")
        break

    try:
        # Evaluasi ekspresi matematika dari input pengguna
        f = lambda x: eval(equation)
        
        # Memasukkan nilai x dari pengguna
        x_value = float(input("Masukkan nilai x: "))
        
        # Memasukkan nilai h dari pengguna
        h = float(input("Masukkan nilai h: "))

        # Menggunakan metode selisih maju
        approx_derivative = forward_difference(f, x_value, h)

        print(f"\nPerkiraan turunan pada x = {x_value} dengan h = {h} adalah {approx_derivative}")

    except Exception as e:
        print(f"Terjadi kesalahan: {e}. Silakan coba lagi.")
