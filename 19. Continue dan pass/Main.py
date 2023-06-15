## continue, pass, break

# pass => fungsi nya sebagai dummy dan tidak akan dieksekusi
angka = 1
while angka <= 5:
    angka += 1

    if angka == 3:  
        pass # tidak akan dieksekusi

    print(angka)
print("program berakhir")

# continue
angka_1 = 0
while angka_1 <= 10:
    angka_1 += 1
    print(f"Angka sekarang : {angka_1}") # aksi 1

    if angka_1 == 3:
        print("Hello gays")
        continue # loop akan loncat ke step selanjutnya, ketika nagka == 3 wassup akan dilewati

    print("wassup") # aksi 2
print("program berakhir")