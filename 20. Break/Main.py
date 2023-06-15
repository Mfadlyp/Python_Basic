# break statement

input = int(input("Masukan angka sampai = "))

count_up = 0

while True:
    count_up += 1
    if count_up == input:
        print(f"Nice ke {count_up}")
        break
print("program berakhir")