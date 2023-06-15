# membuat kalkulator sederhana

option_1 = float(input("Masukan angka pertama : "))
operator = input("Operator.. *, +, -, / : ")
option_2 = float(input("Masukan angka kedua : "))

if operator == "+":
    result = option_1 + option_2
    print(f"Hasil {option_1} + {option_2} = {result}")
elif operator == "-":
    result = option_1 - option_2
    print(f"Hasil {option_1} - {option_2} = {result}")
elif operator == "*":
    result = option_1 * option_2
    print(f"Hasil {option_1} * {option_2} = {result}")
elif operator == "/":
    result = option_1 / option_2
    print(f"Hasil {option_1} / {option_2} = {result}")
else:
    print("Operator yg kamu masukan salah")

print("Program sukses dijalankan")