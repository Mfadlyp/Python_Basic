## format string

# generic string
nama = "ucup"
str_nama = f"Hello, {nama}"
print(str_nama)

# bilangan ribuan
angka = 2000000
str_format = f"Format ke ribuan = {angka:,}"
print(str_format) # hasilnya akan ada koma nya

# bilangan decimal
angka = 2005.4321
format_str = f"Decimal = {angka:.2f}" # . untuk letak titik, 2 untuk berapa angka yg diambil, f float
print(format_str)

# menampilkan leading zero
angka = 2005.4321
format_str = f"Decimal = {angka:010.2f}"
# . untuk letak titik, 2 untuk berapa angka yg diambil, f float
# 0 itu untuk mengisi kekosongan depan nya, 10 itu jumlah angka nya
print(format_str)

# menampilkan tanda - dan +
angka_plus = 10
angka_minus = - 10

format_plus = f"Plus = {angka_plus:+d}" # d untuk decimal, sesuaikan
format_minus = f"Minus = {angka_minus:-d}"

print(format_plus)
print(format_minus)

# memformat persen
persen = 0.045
format_persen = f"Persen = {persen:.2%}"
print(format_persen)

# fomart angka binary, oktal, hexa
angka = 255
format_binary = f"Binary = {bin(angka)}"
format_oktal = f"Oktal = {oct(angka)}"
format_hexa = f"Hexa = {hex(angka)}"

print(format_binary)
print(format_oktal)
print(format_hexa)