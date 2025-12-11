try:
    val = int(input("Masukkan sebuah bilangan bulat positif: "))
    print("Anda memasukkan:", val)
    hasil = 10 / val
    print("10 dibagi angka tersebut adalah:", hasil)
except ValueError:
    print("Input salah! Pastikan Anda memasukkan angka, bukan huruf.")
except ZeroDivisionError:
    print("Input salah! Angka tidak boleh nol.")
except Exception as e:
    print(f"Terjadi error yang tidak diketahui: {e}")