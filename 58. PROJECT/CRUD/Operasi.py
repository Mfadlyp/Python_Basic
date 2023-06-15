'''operasi buat data pertama'''
from . import Database
from . import Util
import time
import os

def delete(no_buku):
    '''delt'''
    try:
        with open(Database.DB_NAME,"r") as file:
            counter = 0
            while(True):
                content = file.readline()
                if len(content) == 0:
                    break
                elif counter == no_buku - 1:
                    pass
                else:
                    with(open("data_temp.txt","a",encoding="utf-8")) as temp_file:
                        temp_file.write(content)
                counter +=1
    except:
        print("Gagal menghapus file")

    os.rename("data_temp.txt",Database.DB_NAME)



def update(no_buku,pk,date_add,judul,penulis,tahun):
    '''update'''
    data_str = Database.TEMPLATE.copy()
    data_str["pk"] = pk
    data_str["date_add"] = date_add
    data_str["penulis"] = penulis + Database.TEMPLATE["penulis"][len(penulis)]
    data_str["judul"] = judul + Database.TEMPLATE["judul"][len(judul)]
    data_str["tahun"] = str(tahun)

    data = f"{data_str['pk']},{data_str['date_add']},{data_str['judul'],{data_str['penulis']},{data_str['tahun']}}\n"

    data_length = len(data)
    try:
        with(open(Database.DB_NAME,"r+",encoding="utf-8")) as file:
            file.seek(data_length*(no_buku)-1)
            file.write(data)
    except:
        print("data salah")


def first_data():
    '''fungsi pembuatan data pertama kali'''
    data_str = Database.TEMPLATE.copy()
    penulis = input("Pneulis : ")
    judul = input("Judul : ")
    while(True):
        try:
            tahun = int(input("Tahun : "))
            if len(str(tahun)) == 4:
                break
            else:
                print("Tahun harus angka (yyyy)")
        except:
            print("Tahun harus angka (yyyy)")

    data_str["pk"] = Util.random_pk(6)
    data_str["date_add"] = time.strftime("%Y-%m-%d-%H-%M-%S%z",time.gmtime()) # Y=taun, m=bulan, d=hari, H=jam, M=menit, S=detik, z=gmt
    data_str["penulis"] = penulis + Database.TEMPLATE["penulis"][len(penulis)]
    data_str["judul"] = judul + Database.TEMPLATE["judul"][len(judul)]
    data_str["tahun"] = str(tahun)

    data = f"{data_str['pk']},{data_str['date_add']},{data_str['judul'],{data_str['penulis']},{data_str['tahun']}}\n"

    # kita tulis ke database
    try:
        with open(Database.DB_NAME,"w",encoding="utf-8") as file:
            file.write(data)
    except:
        print("Gagal menyimpan ke dalam database")

def read(**kwargs):
    '''fungsi membaca file database'''
    try:
        with open(Database.DB_NAME,"r") as file:
            content = file.readlines()
            jumlah_buku = len(content)
            if "index" in kwargs:
                index_buku = kwargs[content]-1
                if index_buku < 0 or index_buku > jumlah_buku:
                    return False
                else:
                   return index_buku
            else:
                return content
    except:
        print("membaca file error")
        return False
    
def create(penulis,judul,tahun):
    '''membuat fungsi create data'''
    data_str = Database.TEMPLATE.copy()
    data_str["pk"] = Util.random_pk(6)
    data_str["date_add"] = time.strftime("%Y-%m-%d-%H-%M-%S%z",time.gmtime()) # Y=taun, m=bulan, d=hari, H=jam, M=menit, S=detik, z=gmt
    data_str["penulis"] = penulis + Database.TEMPLATE["penulis"][len(penulis)]
    data_str["judul"] = judul + Database.TEMPLATE["judul"][len(judul)]
    data_str["tahun"] = tahun

    data = f"{data_str['pk']},{data_str['date_add']},{data_str['judul'],{data_str['penulis']},{data_str['tahun']}}\n"

    # kita tulis ke database
    try:
        with open(Database.DB_NAME,"a",encoding="utf-8") as file:
            file.write(data)
    except:
        print("Gagal menyimpan ke dalam database")