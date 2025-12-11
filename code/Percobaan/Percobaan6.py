def cek_level(level):
    if level < 1:
        raise ValueError("Level tidak valid! Harus minimal 1.")
    print(f"Level {level} diterima.")
try:
    lvl = int(input("Masukkan level karakter: "))
    cek_level(lvl)
except ValueError as e:
    print("Peringatan:", e)