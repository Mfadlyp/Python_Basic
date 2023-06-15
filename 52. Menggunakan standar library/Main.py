'''meegunakan count'''

from collections import Counter
import io

data_angka = ["a","b","c","d","e","c","b","a"]

data_hitung = Counter(data_angka)
print(f"menghitung jumlah a = {data_hitung['a']}")


# membaca file menggunakan io
file = io.open("file_txt.txt","r") # mode r untuk membaca baris text
print(file.read())
