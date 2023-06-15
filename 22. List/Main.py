## list adadlah sekumpulan data []

# alternatif membuat list
range_list = range(0,10,2) # start, finish, step
print(range_list) # di print tapi bukan list

data_list = list(range_list) # merubah ke list
print(data_list) # di print akan menjadi list

# membuat  list menggunakan for loop, list compeherison
list_for = [i for i in range(0,10)] # i yg awal bisa menggunakan i**2 untuk pangkat
print(list_for)

# membuat list menggunakan for dan if
list_if = [i for i in range(0,10) if i !=5] # maka 5 tidak akan di print
print(list_if)