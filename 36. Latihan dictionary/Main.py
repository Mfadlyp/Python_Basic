## latihan dictionary

import datetime
import os
import string
import random

# membuat dict template
mahasiswa_template = {
    "nama":"nama",
    "nim":000000000,
    "sks_lulus":000,
    "beasiswa":0,
    "lahir":datetime.datetime(1111,1,11)
}

# membuat template kosong
data_mahasiswa = {}

# membuat dict baru dengan key dari template
mahasiswa = dict.fromkeys(mahasiswa_template.keys())

# membuat input user, yg akan lansung masuk ke template baru
while True:
    os.system("cls")
    print(f"{'SELAMAT DATANG':^20}")
    print(f"{'INPUT DATA':^20}")

    mahasiswa["nama"] = input("Masukan nama mahasiswa : ")
    mahasiswa["nim"] = input("Masukan nim anda : ")
    mahasiswa["sks_lulus"] = input("Masukan jumlah sks : ")
    mahasiswa["beasiswa"] = input("Beasiswa True/False : ")
    TAHUN_LAHIR = int(input("Masukan tahun lahir (YYYY)"))
    BULAN_LAHIR = int(input("Masukan bulan lahir (MM)"))
    TANGGAL_LAHIR = int(input("Masukan tanggal lahir (DD)"))
    mahasiswa['lahir'] = datetime.datetime(TAHUN_LAHIR,BULAN_LAHIR,TANGGAL_LAHIR)

    # memebuat string key random
    KEY = "".join({random.choice(string.ascii_uppercase) for i in range(6)})
    data_mahasiswa.update({"key":mahasiswa})

    print(f"{'KEY':<8} | {'NAMA':<20} | {'NIM':<15} | {'SKS':<5} | {'BEASISWA':<10} | {'LAHIR':<15}")
    print("="*50)

    for mahasiswa in data_mahasiswa:
        KEY = mahasiswa
        NAMA = data_mahasiswa[KEY]["nama"]
        NIM = data_mahasiswa[KEY]["nim"]
        SKS = data_mahasiswa[KEY]["sks_lulus"]
        BEASISWA = data_mahasiswa[KEY]["beasiswa"]
        LAHIR = data_mahasiswa[KEY]["lahir"].strftime("%x")

        

        print(f"{KEY:<8} | {NAMA:<20} | {NIM:<15} | {SKS:<5} | {BEASISWA:<10} | {LAHIR:<15}")
    
    print("\n")
    is_done = input("Apakah selesai y/n = ")
    if is_done == "y":
        break

print("Akhir dari program")
