# latihan membuat fungsi

import os

def header():
    '''fungsi header'''
    os.system("cls")
    print(f"{'PROGRAM MENGHITUNG LUAS':^40}")
    print(f"{'DAN KELILING PERSEGI PANGJANG':^40}")
    print(f"{'-'*40:^40}")

def input_user():
    '''fungsi input user'''
    panjang = int(input("Masukan panjang : "))
    lebar = int(input("Masukan lebar : "))
    return panjang,lebar

def hitung_luas(panjang,lebar):
    '''fungsi hitung luas'''
    return panjang*lebar

def hitung_keliling(panjang,lebar):
    '''fungsi hitung keliling'''
    return 2*(lebar,panjang)

def display(message,value):
    '''fungsi display'''
    print(f"Hasil perhitungan {message} = {value}")

while True:
    header()
    PANJANG,LEBAR = input_user() # mengambil data dari fungsi input_user
    LUAS = hitung_luas(PANJANG,LEBAR)
    KELILING = hitung_keliling(PANJANG,LEBAR)

    display("luas",LUAS)
    display("keliling",KELILING)

    is_done = input("Apakah lanjut (y/n)? :")
    if is_done == "n":
        break

print("program berakhir")
