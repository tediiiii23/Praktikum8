nilai = [80, 90, 'A', 70, 100, 'B']

total = 0
jumlah_valid = 0

for n in nilai:
    try:
        # Coba ubah menjadi angka
        angka = float(n)
        total += angka
        jumlah_valid += 1
    except ValueError:
        # Jika bukan angka, skip
        print(f"Data '{n}' dilewati (bukan angka).")
        continue

# Hitung rata-rata jika ada data valid
if jumlah_valid > 0:
    rata_rata = total / jumlah_valid
    print(f"\nRata-rata nilai valid: {rata_rata}")
else:
    print("Tidak ada nilai valid.")
