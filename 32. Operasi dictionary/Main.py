## operasi dictionary

data_dictionary = {
    "cp":"ucup surucup",
    "tg":"otong surotong",
    "sa":"saepun sarudin"
}

# menghitung panjang dict
LENDICT = len(data_dictionary)
print(f"pajang data dict adalah {LENDICT}")

# mengecek key ada di dict
KEY = "cp"
CHECK = KEY in data_dictionary
print(f"cek data key = {CHECK}")

# mengakses data dict, gunakan get untuk membedakan data dict
print(data_dictionary["cp"])
print(data_dictionary.get("cp"))
# cek kyy menggukan pesan yg berbeda dari default
print(data_dictionary.get("cp","Key tidak dapat ditemukan"))

# menupdate data dict
data_dictionary.update({"cp":"surucup"})
print(data_dictionary)
# jika menggunakan update data yg ada akan di update kembali
# jika data tidak tersedia akan ditambahkan ke dict
# jika kita tahu data di dict tidak tersedia gunakan add

# mendelete data di dict
del data_dictionary["cp"]
print(data_dictionary)
