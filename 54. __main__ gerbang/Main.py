'''__main__ gerbang'''

# __main__ adalah top level environment

# __name__ == __main__ akan terjadi jika ada di file utama

# __name__ pada file program utama
print(f"nilai __name__ Main.py = '{__name__}'")

## __name__ pada program exkternal
import fungsi
import package

## contoh penggunaan main

# deklarasi
def tambah(a:int,b:int)->int:
    return a+b

# fungsi utama
if __name__ == "__main__":
    angka1 = 10
    angka2 = 5
    hasil = tambah(angka1,angka2)
    print(f"hasilnya adalah {hasil}")