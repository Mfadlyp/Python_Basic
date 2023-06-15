## looping dictionary

teman_teman = {
    "cp":"ucup surucup",
    "tg":"otong surotong",
    "di":"udin surudin",
    "ko":"eko sureko"
}

## cara untuk mengambil item dict

# mengambil key
for key in teman_teman.keys():
    print(teman_teman.get(key))

# mengambil value
for value in teman_teman.values():
    print(value)

# menggunkan item
for item in teman_teman.items():
    print(item)

for key,value in teman_teman.items():
    print(f"key = {key} | value = {value}")
