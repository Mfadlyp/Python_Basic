## operasi list

data_angka = [1,2,3,5,2,3,6,7,8,9,2,5,10,1,2,3,4]
print(f"data angka saat ini = \n{data_angka}")

# menjumlahkan data pada data angka
data_count_3 = data_angka.count(3)
data_count_5 = data_angka.count(5)

print(f"Jumlah data 3 adalah = {data_count_3}")
print(f"Jumlah data 3 adalah = {data_count_5}")

# mengambil posisi data
data_huruf = ["ujang","ucup","otong","asep"]

data_index = data_huruf.index("ujang")
print(f"posisi data ujang ada di = {data_index}")

# mengurutkan angka atau huruf
print(f"Angka sebelum sort = \n{data_angka}")
print(f"Huuruf sebelum sort = \n{data_huruf}")
data_angka.sort()
data_huruf.sort()
print(f"Angka sesudah sort = \n{data_angka}")
print(f"Huuruf sesudah sort = \n{data_huruf}")

# membalikan data setelah disort
data_angka.reverse()
data_huruf.reverse()
print(f"Angka sesudah reverse = \n{data_angka}")
print(f"Huuruf sesudah reverse = \n{data_huruf}")
