## operasi deep copy nested list

data_0 = [1,2]
data_1 = [3,4]

data_2D = [data_0,data_1] # nested list
print(f"ini adalah data list = {data_2D}")

# cara mengambil angka
data = data_2D[0] # untuk ambil angka [1,2]
print(data)
data = data_2D[0][1] # untuk ambil angka 1
data = data_2D[1][0] # untuk ambil angka 3

# cara melakukan deep copy
from copy import deepcopy
data_2D = [data_0,data_1,9,10] # nested list
data_2D_deepcopy = deepcopy(data_2D)