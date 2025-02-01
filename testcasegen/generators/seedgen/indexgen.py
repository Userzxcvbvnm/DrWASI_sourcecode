import random
import string


# generate function index
def gen_random_string(length):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))
