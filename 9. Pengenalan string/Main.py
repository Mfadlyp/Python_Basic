data = "ini adalah string"
print(data)

# 1. cara membuat string

'''
    1. dengan menggunakan single quote '...'
    2. dengan menggunakan double quote "..."

'''

data = 'ini adalah single quote'
print(data)

data = "ini adalah double quote"
print(data)

print("hari ini adalah jum'at")

# 2. menggunkan tanda \

# membuat tanda ' menjadi string
print('hari ini adalah jum\'at')

# backlash
print("C:\\user\\ucup")

# tab
print("ucup \t otong, berjauj jauhan")

# backspace
print("ucup \b dan otong")

# newline
print("ucup bersama otong \n bermain bersama-sama") # LF = line feed : dipakai oleh unix, macos, linux
print("ucup bersama otong \r bermain bersama-sama") # CR = Carriage return : dipakai oleh system lama
print("ucup bersama otong \r\n bermain bersama-sama") # CRLF = Line feed : dipakai windows

# 3. String literal
# hati hati
print("C:\new\user") # akan membuat new line

# menggunakan raw string
print(r'C:\user\new')

# multiline literal
print("""
ini adalah sting multiline
""")
