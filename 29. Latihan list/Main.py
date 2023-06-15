# latihan list
# membuat data buku menggukan list

list_buku = []


while True:
    
    judul = input("Judul buku\t : ")
    penulis = input("Nama penulis\t : ")

    data_buku = [judul,penulis]
    list_buku.append(data_buku)
    
    
    print(f"| NO\t | Judul\t\t | Penulis\t\t |")
    for index,buku in enumerate(list_buku):
            print(f" {index}\t | {buku[0]}\t\t | {buku[1]}\t\t ")


    
        