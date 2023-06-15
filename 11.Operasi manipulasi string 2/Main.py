## operator dalam bentuk method
# merubah case dari string

# merubah semua ke upper case
salam = "bro"
print("halo mas, ",salam)

upper_str = salam.upper()
print("halo mas,", upper_str)

# merubah semua ke lower case
alay ="aKu, KeZeL, AbiessZZZ ini"

result = alay.lower()
print("contoh kata alay :> ", result)

## pengecekan dengan menggunakan isX method
# contoh pengecekana lower case

salam = "sist"
apakah_lower = salam.islower() # hasilnya boolean, harus casting ke string
print("apakah isi variabel salam itu lower case ? ", str(apakah_lower))

# isaplha() <-- untuk mengecek semua huruf
# isalnum() <-- untuk mengecek huruf dan angka
# isdecimal() <-- untuk mengecek huruf angka
# isspcae() <-- untuk mengecek space, tab, \n
# istitle() <-- untuk mengecek huruf awal kapital

## mengecek menggunakan startswith() dan endswith() <-- keren
# menggunakn literal
cek_start = "Sangjanim Oppa".startswith("Sangjanim") # mengecek awalan kalimat
print("Start = ", str(cek_start))

cek_end = "Sangjanim Oppak".endswith("Oppak")
print("End = ", str(cek_end))

## penggabungan komponen join() dan slpit() pemisah komponen
# menggunakan join()
pisah = ["aku","sayang","dia"]
gabung = "".join(pisah)
koma = ",".join(pisah)
print(gabung)
print(koma)

# menggunakan split()
pisah = "akuehmsayngehmkamu"
print(pisah.split("ehm")) # menjadi list

## alokasi karakter rjust(), ljust(), center()
# rjust()
kanan = "kanan".rjust(10) # 10 adalah berapa jarak nya
print("'"+kanan+"'")

# atau custom
kekanan = "kanan".rjust(10,"-")
print("'"+kekanan+"'")

# ljust()
kiri = "kiri".ljust(10)
print("'"+kiri+"'")

# center()
tengah = "tengah".center(10)
print("'"+tengah+"'")