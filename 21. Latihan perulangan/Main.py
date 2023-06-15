## Latihan menggunakan perulangan

# 1. menggunakan for
sisi =  5
count = 1

for i in range(sisi):
    print("*"*count)
    count += 1

# 2. menggunakan while
count = 1
while True:
    print("*"*count)
    count += 1
    if count > sisi:
        break

# 3. print ganjil saja
count = 1
while True: # akan terus mengulang
    # akan diprint jika ganjil
    if count%2:
        print("*"*count)
        count +=1
    else:
    # akan kemabli keatas jika genap
        count += 1
        continue
    # akan break jika count melebihi sisi
    if count > sisi:
        break

# 4. belah ketupat
count = 1
spasi = int(sisi/2)
while True:
    if (count%2):
        print(" "*spasi,"+"*count)
        spasi -= 1
        count += 1
    else:
        count += 1
        continue
    if count > sisi:
        break
while True:
    if (count%2): 
        spasi += 1
        print(" "*spasi,"+"*count)
        count -= 1
    else:
        count -= 1
    if count == 0:
        break