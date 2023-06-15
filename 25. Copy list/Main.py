## cara mengcopy list dengan benar
 
a = ["ucup","otong","asep"]
print(a)

b = a.copy() # gunakan copy untuk list
print(b)

a[0] = "michael" # ucup kita ganti menjadi michael

print(a) # jika diprint, hanya a saja yg berubah
print(b) # tidak akan berubah