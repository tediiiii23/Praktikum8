print('Silakan masukkan dua angka untuk pembagian.')
try:
    num1 = int(input('Masukkan angka yang akan dibagi: '))
    num2 = int(input('Masukkan angka pembagi: '))
    print('{0} dibagi {1} = {2}'.format(num1, num2, num1/num2))
except ZeroDivisionError:
    print('Error: Tidak bisa membagi bilangan dengan nol.')