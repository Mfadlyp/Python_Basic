## lamda function

def fungsi_kuadrat(angka):
    '''fungsi kuadrat'''
    return angka**2
print(f"hasil adalaha {fungsi_kuadrat(5)}")

# kita coba dengan lamda
# output = lamda argumen:expresion

fungsi_kuadrat_lamda = lambda angka:angka**2
print(f"hasil denga lamda = {fungsi_kuadrat_lamda(5)}")

# sort menggunakan lambda
data_list = ["ucup","otong","dudung"]
data_list.sort(key = lambda nama:len(nama))
print(f"hasil data list menggunakan lamda = {data_list}")

# filter menggunakan lamda
data_angka = [1,2,3,4,5,6,7,8,9]

angka_genap = list(filter(lambda x:x<5, data_angka))
print(f"hasil nya adalah {angka_genap}")

## anonymous function

# menggunkanan currying
def pangkat(n):
    '''fungsi dengan anonymous'''
    return lambda angka:angka**n

pangkat_2 = pangkat(2)
print(f"hasil pangkat 2 {pangkat_2(5)}")
