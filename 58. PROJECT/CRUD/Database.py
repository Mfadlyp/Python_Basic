'''untuk database'''
from . import Operasi

DB_NAME = "data.txt"

# membuat template
TEMPLATE = {
    "pk":"XXXXXX",
    "date_add":"yyyy-mm-dd",
    "penulis":255*" ",
    "judul":255*" ",
    "tahun":"yyyy"
}

def init_console():
    '''fungsi cek database'''
    try:
        # membaca database
        with open(DB_NAME,"r") as file:
            print("Database tersedia")
    except:
        print(f"Database tidak tersedia, buat terlebih dahulu")
        # membuat database baru
        Operasi.first_data()
