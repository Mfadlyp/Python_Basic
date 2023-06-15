'''**kwargs pada fungsi'''

def fungsi(**kwargs): # kwargs type nya dictionary
    '''fungsi kwargs'''
    print(kwargs["nama"])

fungsi(nama="ucup",berat=50,tinggi=170)

# studi kasus
def math(*args,**kwargs):
    '''fungsi args dan kwargs'''
    output = 0
    if kwargs["option"] == "tambah":
        for angka in args:
            output += angka
    elif kwargs["option"] == "tambah":
        output = 1 # karena akan dikali
        for angka in args:
            output *= angka
    return output

HASIL = math(1,2,3,4,5,6,7,8,option="tambah")
print(HASIL)
