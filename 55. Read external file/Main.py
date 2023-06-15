'''tutorial membaca file external'''

file = open("data.txt",mode="r")
print(file.read())

## teknik membaca file external

with open("data.txt",mode="r") as file:
    content = file.readline()
    print(content)
