## type hints pada fungsi

import string
def hello_world(argument:string) -> string: # argument bentuk string dan output string
    '''fungsi hello world'''
    return argument
HASIL = hello_world("ucup")
print(HASIL)
