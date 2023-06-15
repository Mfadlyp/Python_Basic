'''util random'''
import string
import random
def random_pk(panjang:int)->str:
    '''fungsi random'''
    data_random = "".join(random.choice(string.ascii_letters) for i in range(panjang))
    return data_random