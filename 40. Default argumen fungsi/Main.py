# default argumen

# def fungsi(argument):
# def fungsi(argument = nilai default nya)

def say_hello(nama = "kamu"):
    '''fungsi say hello'''
    print(f"Hello {nama}")

say_hello("ucup")
say_hello() # hasilnya kkan di print default

# contoh lain
def pangkat_angka(pangkat,angka):
    '''fungsi pangkat'''
    hasil = angka**pangkat
    return hasil

print(pangkat_angka(2,5))
RESULT= pangkat_angka(pangkat=5, angka=2)
print(RESULT)
