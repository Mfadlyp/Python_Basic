# date dan time

import datetime as dt

hari_ini = dt.date.today()
print(hari_ini)

# cetak tangga sesuai keinginan
tanggal = dt.date(20220,10,10)
print(tanggal)
print(f"Hari ini adalah tanggal, {tanggal:%A}")

# membuat tool sederhana cek umur
tanggal = int(input("Masukan tanggal : "))
bulan = int(input("Masukan bulan : "))
tahun = int(input("Masukan tahun :"))

tanggal_lahir = dt.date(tahun,bulan,tanggal)
print(f"Tanggal lahir anda adalah : {tahun,bulan,tanggal}")
print(f"Hari nya adalah : {tanggal_lahir:%A}")

# ambil tanggal hari ini
hari_sekarang = dt.date.today()
# lalu kita kurangkan dengan tanggal lahir
umur_hari = hari_sekarang - tanggal_lahir
# karena hasilnya hari bukan tahun, maka rubah ke tahun lebih dahulu
umur_tahun = umur_hari.days() // 365
# kita print
print(f"Umur anda adalah: {umur_tahun} tahun") 