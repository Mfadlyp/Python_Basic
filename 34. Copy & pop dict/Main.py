## copy dan pop dictionary

# copy dictionary
teman_teman = {
    "cp":"Ucup surucup",
    "dn":"udin saepudin",
    "se":"saep usep",
    "tg":"otong surotong"
}

friends = teman_teman.copy() # copy dictionary

print(f"ini teman : {teman_teman}")
print(f"ini friends : {friends}")
# kita rubah data dictionary, apakah masih dialamat yg sama
teman_teman["cp"] = "ucup ganteng"
print(f"ini teman : {teman_teman}")
print(f"ini friends : {friends}")

# pop dictionary
# pop untuk mengambil data dari dictionary
data_asep = teman_teman.pop()   # ambil data asep
print(f"data asep : {data_asep}")
print(f"ini friends : {friends}")

# popitem dictionary mengambil data terakhir
# pop item mengambil data berpasangan 
data_terakhir = teman_teman.popitem()
print(f"data terakhir : {data_terakhir}")
print(f"ini friends : {friends}")


