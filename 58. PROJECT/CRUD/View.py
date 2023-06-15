'''untuk membaca file'''

from . import Operasi

def delete_console():
    '''fungsi delete'''
    read_console()
    while(True):
        print("="*60)
        no_buku = int(input("Pilih nomor buku yg akan didelete : "))
        data_buku = Operasi.read(index=no_buku)
        if data_buku:
            data_break = data_buku.split(",")
            pk = data_break[0]
            date_add = data_break[1]
            judul = data_break[2]
            penulis = data_break[3]
            tahun = data_break[4][:-1] # mengambil enter

  
            # data yg ingin diubah
            print("="*60)
            print("Data yang akan dihapus")
            print(f"1. Judul : {judul:40}")
            print(f"2. Penulis : {penulis:40}")
            print(f"3. Tahun : {tahun:4}")

            is_done = input("Apakah yakin dihapus y/n :")
            if is_done == "y" or is_done == "Y":
                Operasi.delete(no_buku)
                break
            elif is_done == "0":
                break
        else:
            print("nomor tidak valid")
    
    print("Data berhasil dihapus")

    

def create_console():
    '''membuat funsgi create data'''
    print("\n\n"+"="*60)
    print("Silakan tambahkan buku")
    penulis = input("Penulis : ")
    judul = input("Judul : ")
    # akan mengulang terus sampai tahun benar
    while(True):
        try:
            tahun = int(input("Tahun : "))
            if len(str(tahun)) == 4:
                break
            else:
                print("Tahun harus angka (yyyy)")
        except:
            print("Tahun harus angka (yyyy)")

    Operasi.create(penulis,judul,tahun)
    print("Data anda yang baru dimasukan")
    read_console()



def read_console():
    '''fungsi menampilkan read'''
    data_file = Operasi.read()
    
    # styling
    index = "No"
    penulis = "Penulis"
    judul = "Judul"
    tahun = "Tahun"

    print("="*100+"\n")
    print(f"{index:6} | {penulis:40} | {judul:40} | {tahun:6}")
    print(f"{'-'*100}")

    for index,data in enumerate(data_file):
        data_break = data.split(",")
        pk = data_break[0]
        date_add = data_break[1]
        penulis = data_break[2]
        judul = data_break[3]
        tahun = data_break[4]
        print(f"{index:6} | {penulis:40} | {judul:40} | {tahun:5}",end="")

    print("="*100+"\n")

def update_console():
    '''fungsi update data'''
    read_console()
    while(True):
        print("="*60)
        no_buku = int(input("Pilih nomor buku yg akan diupdate : "))
        data_buku = Operasi.read(index=no_buku)
        if data_buku:
            break
        else:
            print("nomor tidak valid")

    data_break = data_buku.split(",")
    pk = data_break[0]
    date_add = data_break[1]
    judul = data_break[2]
    penulis = data_break[3]
    tahun = data_break[4][:-1] # mengambil enter

    while(True):
        # data yg ingin diubah
        print("="*60)
        print("silakan pilih data yang mau diubah")
        print(f"1. Judul : {judul:40}")
        print(f"2. Penulis : {penulis:40}")
        print(f"3. Tahun : {tahun:4}")

        # memilih mode
        user_option = input("Pilih : ")
        match user_option:
            case "1": judul = input("Masukan judul : ")
            case "2": penulis = input("Masukan Penulis : ")
            case "3": # akan mengulang terus sampai tahun benar
                    while(True):
                        try:
                            tahun = int(input("Tahun : "))
                            if len(str(tahun)) == 4:
                                break
                            else:
                                print("Tahun harus angka (yyyy)")
                        except:
                            print("Tahun harus angka (yyyy)")

            case _: print("data yg ingin anda ubah")

        print("Data baru anda")
        print(f"1. Judul : {judul:40}")
        print(f"2. Penulis : {penulis:40}")
        print(f"3. Tahun : {tahun:4}")
        is_done = input("Apakah selesai update data y/n :")
        if is_done == "y" or is_done == "Y":
            break
        elif is_done == "0":
            break
    
    Operasi.update(no_buku,pk,date_add,penulis,judul,tahun)