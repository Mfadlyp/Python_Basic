## glibal dan local scope

ANGKA = 0
def ubah_angka(nilai_baru):
    '''fungsi rubah angka'''
    global ANGKA # fungsi ini mendapat akses merubah ankga
    ANGKA = nilai_baru # agar ankga di local dapat diakses oleh luar

print(f"angka sebelumnya {ANGKA}")
ubah_angka(10) # gk ngaruh
print(f"angka sesudahnya {ANGKA}")
