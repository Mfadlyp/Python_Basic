'''contoh penggunaan try dan except'''

while True:
    angka = int(input("masukan angka : "))
    try:
        hasil = 10/angka
        print(f"hasilnya = {hasil}")
        is_done = input("Apakah sudah selesai y/n : ")
        if is_done == "y":
            break
    except:
        print("angka yg dimasukan salah")

print("akhir dari program")




