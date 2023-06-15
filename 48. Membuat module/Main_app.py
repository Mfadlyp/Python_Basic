'''fungsi utama menjalankan module'''

import module_matematika
# from module_matematika import * => mengimport semua
# from module_matematika import kali,tambah,pangkat => tidak perlu di panggil ketika akan digunakan

# fungsi tambah
result = module_matematika.tambah(2,5)
print(f"Hasil tambah = {result}")


# fungsi kali
result = module_matematika.kali(2,3)
print(f"Hasil kali = {result}")


# fungsi pangkat
result = module_matematika.pangkat(5)
print(f"Hasil pangkat = {result}")
