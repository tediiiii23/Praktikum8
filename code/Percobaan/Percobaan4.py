try:
    x = int(input("Masukkan angka: "))
except ValueError:
    print("Itu bukan angka!")
else:
    print(f"Terima kasih, Anda memasukkan angka {x}")
    # Logika lanjutan yang aman dijalankan jika input benar
finally:
    print("Sesi input selesai (blok finally selalu dieksekusi).")