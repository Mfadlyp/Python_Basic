'''module matematika'''

def tambah(*args):
    '''fungsi tambah'''
    hasil = 0
    for data in args:
        hasil += data

    return hasil

def kali(*args):
    '''fungsi tambah'''
    hasil = 1
    for data in args:
        hasil *= data
    return hasil

def pangkat(data:int):
    '''fungsi pangkat dengan lambda'''
    return lambda angka:angka**data