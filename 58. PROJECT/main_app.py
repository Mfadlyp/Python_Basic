import os

import CRUD as CRUD


if __name__ == "__main__":
    # membuat varibael os
    SISTEM_OPERASI = os.name

    # # mengecek sistem operasi
    # match SISTEM_OPERASI:
    #     case "posix": os.system("cls") # windows
    #     case "nt": os.system("clear") # mac, linux

    # print("SELAMAT DATANG")
    # print("DI PROGRAM")
    # print("DATABASE")
    # print("="*10)

    # check database
    CRUD.init_console()

    while(True):
        # mengecek sistem operasi
        match SISTEM_OPERASI:
            case "posix": os.system("cls") # windows
            case "nt": os.system("clear") # mac, linux

        print("SELAMAT DATANG")
        print("DI PROGRAM")
        print("DATABASE")
        

        print("1. Read data")
        print("2. Create data")
        print("3. Update data")
        print("4. Delete data\n")
        print("5. 0 for exit")

        
        option = input("Masukan Opsi : ")
        
        match option:
            case "1": CRUD.read_console()
            case "2": CRUD.create_console()
            case "3": CRUD.update_console()
            case "4": CRUD.delete_console()

        is_done = input("Apakah selesai y/n :")
        if is_done == "y" or is_done == "Y":
            break
        elif is_done == "0":
            break
    
    print("program berakhir")
