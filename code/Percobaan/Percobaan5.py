try:
    daftar_angka = [1, 2, 3]
    indeks = int(input("Masukkan indeks yang ingin diakses (0-2): "))
    print("Nilai:", daftar_angka[indeks])
except IndexError as e:
    print("Terjadi IndexError. Pesan sistem:", e)
except ValueError as e:
    print("Terjadi ValueError. Pesan sistem:", e)