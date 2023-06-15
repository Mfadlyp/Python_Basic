'''module matematika'''

def tambah(*args):
    '''fungsi tambah'''
    hasil = 0
    for data in args:
        hasil += data
    return hasil

def kali(*args):
    '''fungsi kali'''
    hasil = 1
    for data in args:
        hasil *= data
    return hasil

