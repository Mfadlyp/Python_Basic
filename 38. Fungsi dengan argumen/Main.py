'''fungsi dengan argumen'''

def hello_world(nama):
    '''fungsi hello world'''
    print(f"Selamat datang wahai {nama}")

hello_world("ucup") # memanggil fungsi

# membuat fungsi tambah
def tambah(angla_1,angka_2):
    '''fungsi tambah'''
    hasil = angla_1 + angka_2
    print(f"{angla_1} + {angka_2} = {hasil}")

tambah(1,5)

# membuat fungsi dengan list
def peserta_boyband(list_peserta):
    '''fungsi dengan list'''
    data_peserta = list_peserta.copy()
    for peserta in data_peserta:
        print(f"Anggota boyband {peserta}")


data_boyband = ["ucup","udin","otong"]

peserta_boyband(data_boyband)
