'''write external file'''

# 1. mode write
# dia akan membuat file baru jika tidak ada file
# lalu akan memnimpa isi file atau overwrite

with open("data_txt.txt",mode="w",encoding="utf-8") as file:
    file.write("Otong surotong")

# 2, mode append = menambah file

with open("data_txt.txt",mode="a",encoding="utf-8") as file:
    file.write("Asep si kasep")