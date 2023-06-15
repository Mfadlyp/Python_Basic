# operasi bitwise, operasi biner, binary

a = 10
b = 5

# operasi OR (|) 
hasil = a | b
print(a,"|",b,"=",hasil, "binary format = ",format(a,'08b'))

# oeprasi bitwise AND (&)
hasil = a & b
print(a,"&",b,"=",hasil, "binary format = ",format(a,'08b'))

# operasi bitwise XOR (^)
hasil = a ^ b
print(a,"^",b,"=",hasil, "binary format = ",format(a,'08b'))

# operasi bitwise NOT (~)
hasil = ~a
print("~",a, "binary format = ",format(a,'08b'))