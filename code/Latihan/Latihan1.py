try:
    # Meminta input angka dari pengguna
    angka1 = float(input("Masukkan angka pertama: "))
    angka2 = float(input("Masukkan angka kedua : "))
    
    # Meminta input operator
    operator = input("Masukkan operator (+, -, *, /): ")

    # Mengecek operator valid
    if operator not in ['+', '-', '*', '/']:
        raise Exception("Operator tidak valid! Gunakan hanya +, -, *, atau /.")

    # Melakukan operasi
    if operator == '+':
        hasil = angka1 + angka2
    elif operator == '-':
        hasil = angka1 - angka2
    elif operator == '*':
        hasil = angka1 * angka2
    elif operator == '/':
        # Menangani pembagian dengan nol
        try:
            hasil = angka1 / angka2
        except ZeroDivisionError:
            print("Error: Tidak dapat membagi dengan nol!")
            exit()

    print(f"Hasil: {hasil}")

# Menangani input bukan angka
except ValueError:
    print("Error: Input harus berupa angka!")

# Menangani error operator kustom
except Exception as e:
    print("Error:", e)
