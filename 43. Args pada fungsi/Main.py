## *args pada fungsi

# studi kasus

def angka1(*args):
    '''fungsi args'''
    nama = args[0]
    tinggi = args[1]
    berat = args[2]
    print(f"nama {nama} tinggi {tinggi} berat {berat}")

angka1("ucup",170,50)

def fungsi(*data) -> int: # data tipe nya tuple, dia bisa diiiterasi
    '''fungsi'''
    output = 0
    for angka in data:
        output += angka
    return output

HASIL = fungsi(1,2,3,4,5,6,7,8,9)
print(f"Hasil {HASIL}")
