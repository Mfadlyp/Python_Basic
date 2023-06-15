import datetime as dt

# multi key
mahasiswa1 = {
    "nama":"ucup surucup",
    "nim":201743500554,
    "sks_lulus":130,
    "beasiswa":True,
    "lahir":dt.datetime(2000,5,11)
}

mahasiswa2 = {
    "nama":"saepudin",
    "nim":201743500534,
    "sks_lulus":110,
    "beasiswa":False,
    "lahir":dt.datetime(2002,2,21)
}

mahasiswa3 = {
    "nama":"otong surotong",
    "nim":201743500154,
    "sks_lulus":100,
    "beasiswa":False,
    "lahir":dt.datetime(2001,10,11)
}

data_mahasiswa = {
    "MAH001":mahasiswa1,
    "MAH002":mahasiswa2,
    "MAH003":mahasiswa3
}

print(f"{'KEY':<8} | {'NAMA':<20} | {'NIM':<15} | {'SKS':<5} | {'BEASISWA':<10} | {'LAHIR':<15}")
print("="*50)

# Nesting dictionary
for mahasiswa in data_mahasiswa:
    KEY = mahasiswa
    NAMA = data_mahasiswa[KEY]["nama"]
    NIM = data_mahasiswa[KEY]["nim"]
    SKS = data_mahasiswa[KEY]["sks_lulus"]
    BEASISWA = data_mahasiswa[KEY]["beasiswa"]
    LAHIR = data_mahasiswa[KEY]["lahir"].strftime("%x")

    print(f"{KEY:<8} | {NAMA:<20} | {NIM:<15} | {SKS:<5} | {BEASISWA:<10} | {LAHIR:<15}")
    