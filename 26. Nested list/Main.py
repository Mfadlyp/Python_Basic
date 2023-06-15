## nested list atau list bersarang

data_0 = [1,2]
data_1 = [3,4]

data_list = [data_0,data_1] # nested list
print(f"ini adalah data list = {data_list}")

# contoh penggunaan nested list

peserta_0 = ["ucup",20,"Laki-laki"]
peserta_1 = ["otong",25,"Laki-laki"]
peserta_2 = ["dedeh",50,"Wanita"]

data_peserta =[peserta_0,peserta_1,peserta_2]
print(f"ini adalah data peserta list = {data_list}")

# kita print satu-satu menggunakan for loop
for peserta in data_peserta:
    print(f"Nama peserta = {peserta[0]}") # gunakan index untuk mengambil data
    print(f"Umur peserta = {peserta[1]}")
    print(f"gender peserta = {peserta[3]}")