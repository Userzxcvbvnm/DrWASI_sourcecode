import sys
import re
import random
import string
sys.path.append("../entrance")
from enum import Enum
from parmu_clock_res_get import CLOCK_ID
from temtool import readtem, gen_and_compile, replace
from parmu_fd_advise import OFFSET, LEN, OPENSTYLEFILE

FILE_NAME = "fd_read"


def parmu_fd_read(temfile=f"../../../../../executedir/testcasepool/seeds/{FILE_NAME}_00000.c"):
    index = 1 
    code = readtem(temfile)

            
    for content_size in LEN.gen_ran_len():
        letters = string.ascii_letters + string.digits
        content = ''.join(random.choice(letters) for _ in range(content_size))

        pattern = r'char buf1\[10\];'
        newsens = f'char buf1[{content_size}];'
        res, modified_code = replace(code, pattern, newsens)
        if res == -1:
            print(modified_code)
            return

        pattern = r'char buf2\[10\];'
        newsens = f'char buf2[{content_size}];'
        res, modified_code = replace(modified_code, pattern, newsens)
        if res == -1:
            print(modified_code)
            return

        pattern = r'iov\[0\]\.iov_len = 10;'
        newsens = f'iov[0].iov_len = {content_size};'
        res, modified_code = replace(modified_code, pattern, newsens)
        if res == -1:
            print(modified_code)
            return

        pattern = r'iov\[1\]\.iov_len = 10;'
        newsens = f'iov[1].iov_len = {content_size};'
        res, modified_code = replace(modified_code, pattern, newsens)
        if res == -1:
            print(modified_code)
            return

        for member in OPENSTYLEFILE.__members__.values():
            pattern = r'int fd = get_fd\("EXAMPLEFILE", (.*)\);'
            newsens = f'int fd = get_fd("EXAMPLEFILE", {member.value});'
            res, modified_code = replace(modified_code, pattern, newsens)
            if res == -1:
                print(modified_code)
                return
            index = gen_and_compile(index, modified_code, FILE_NAME)


if __name__ == "__main__":
    parmu_fd_read()
