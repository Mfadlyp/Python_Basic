## operasi list

# cara mengambil data dari list menggunakan index
data = ["ucup","otomg","udin"]

hasil = data[0]
print(f"data ke - {hasil}")

# mengambil info panjang list
panjang_list = len(data)
print(panjang_list)

## manipulasi list

# menemabahkan item pada list sesuai posisi
print(f"Data awal = {data}")

data.insert(1,"asep") # posisi, item yg dimasukan
print(f"data setelah insert {data}")

# menambahkan data diakhir list
data.append("zaenal")
print(f"data setelah append {data}")

# menambah list dengan list
data_baru = ["ujang","usep","saep"]
data.extend(data_baru)
print(f"data setelah digabung dengan list baru = {data}")

# merubah data pada list
data[1] = "michael"
print(f"data setelah dirubah = {data}")

# menghapus data list
data.remove("ujang")
print(f"data setelah dihapus = {data}")

# menghapus data paling belakang
data.pop()
print(f"data setelah dihapus bagian akhir = {data}")