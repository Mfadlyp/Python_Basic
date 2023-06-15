## lopping dari list

# for loop
angka = [1,3,4,5,6,7,8,10,9]
for i in angka:
    print(f"Angka ke- {i}")

huruf = ["asep","otong","ucup"]
for i in huruf:
    print(f"Nama ke- {i}")

# for loop dengan range
# cara standar
angka_baru = [1,4,5,6,7,9,10,0,3,5]
panjang = len(angka_baru)
for i in range(panjang):
    print(f"Angka baru ke- {angka_baru[i]}")

for i in range(1,10):
    print(f"Angka ke- {i}")

# while loop
angka_baru = [1,4,5,6,7,9,10,0,3,5]
panjang = len(angka_baru)
i = 0
while i < panjang:
    print(f"angka ke- {angka_baru[i]}")
    i += 1

# list comprehesion
data = ["ucup",25,"otong",4,5]
[print(f"data ke - {data}") for i in data]

# enumerate
data_anggota = ["ucup",25,"otong",4,5]
for index,data in enumerate(data_anggota):
    print(f"data ke- {index}, data = {data}")
