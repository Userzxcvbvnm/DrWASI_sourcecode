import random
import string

def gen_ran_com_par(count=3, len=5):
    if count < 1:
        return ""
    elif count == 1:
        return ''.join(random.choices(string.ascii_letters + string.digits, k=len))
    else :
        res = ""
        for i in range(count - 1):
            ran = ''.join(random.choices(string.ascii_letters + string.digits, k=len))
            res = f"{res}{ran} "
        ran = ''.join(random.choices(string.ascii_letters + string.digits, k=len))
        res = f"{res}{ran}"
        return res
