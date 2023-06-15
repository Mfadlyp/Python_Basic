'''init pada package'''

from sains import matematika, fisika
import sains

HASIL = matematika.tambah(2,4)
print(f"Hasil tambah = {HASIL}")

HASIL = fisika.gaya(2,4)
print(f"hasil gaya = {HASIL}")

HASIL = sains.kali(2,4) # cara memangil module saja
print(f"hasil kali = {HASIL}")

