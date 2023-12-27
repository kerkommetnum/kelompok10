def newton_interpolation(x, y, value):
    n = len(x)
    if n != len(y):
        raise ValueError("Jumlah elemen x dan y harus sama")
    
    # Inisialisasi tabel diferensi terbagi
    table = [[None for _ in range(n)] for _ in range(n)]
    for i in range(n):
        table[i][0] = y[i]
    
    # Hitung tabel diferensi terbagi
    for j in range(1, n):
        for i in range(n-j):
            table[i][j] = (table[i+1][j-1] - table[i][j-1]) / (x[i+j] - x[i])
    
    # Hitung polinomial interpolasi
    result = 0
    for j in range(n):
        term = table[0][j]
        for i in range(j):
            term *= (value - x[i])
        result += term
    
    return result

# Memasukkan data
x_data = []
y_data = []

num_points = int(input("Masukkan jumlah titik data: "))

for i in range(num_points):
    x_val = float(input(f"Masukkan nilai x ke-{i+1}: "))
    y_val = float(input(f"Masukkan nilai y ke-{i+1}: "))
    x_data.append(x_val)
    y_data.append(y_val)

# Menentukan nilai x untuk interpolasi
x_value = float(input("\nMasukkan nilai x untuk interpolasi: "))

# Hasil interpolasi
interpolated_value = newton_interpolation(x_data, y_data, x_value)
print(f"\nNilai interpolasi di x = {x_value} adalah {interpolated_value}")
