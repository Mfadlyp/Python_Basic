# operasi dan manipulasi string

# 1. menyambung string (concatenate)
nama_pertama = "ucup"
nama_kedua = "D"
nama_ketiga = "The Fame"

full_name = nama_pertama +""+ nama_kedua + nama_ketiga
print(full_name)

# 2. menghitung panjang string
hitung_nama = len(full_name)
print(str(hitung_nama)) # merubah dari int ke string

# 3. operator untuk string

# mengecek apakah ada komponen string atau char pda string
cek = "d" # apakah terdapat string d pada full_name
status = cek in full_name
print(status)

# mengulang string
print("wk"*10)

# indexing
print("indesx ke - ",full_name[3])
print("indesx ke - ",full_name[-3]) # menggunakan - mengambil string dari belakang

# range
print("index ke [0:5]",full_name[0:5]) # mengambil string dari ke ... sampai ke ... dengan catatan lebihkan satu hufu di 

# menggunakan increament
print("index ke [0,2,4,6,8,10]",full_name[0:10:2]) # :2 adalah increament nya

# item paling kecil
print("paling kecil - ",min(full_name))
# item paling besar
print("item paling besar -",max(full_name))

# mengecek ascii_code
ascii_code = ord("w")
print(str(ascii_code))

# 4. operator dalam method
data ="otong surotong tartotong ngabers"
rs = data.count("o") # menghitung string o
print(rs)