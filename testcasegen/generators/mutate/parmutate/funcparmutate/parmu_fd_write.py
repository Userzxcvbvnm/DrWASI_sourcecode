import sys
import re
import random
import string
sys.path.append("../entrance")
from enum import Enum
from parmu_clock_res_get import CLOCK_ID
from temtool import readtem, gen_and_compile, replace
from parmu_fd_advise import OFFSET, LEN, OPENSTYLEFILE

FILE_NAME = "fd_write"


def parmu_fd_write(temfile=f"../../../../../executedir/testcasepool/seeds/{FILE_NAME}_00000.c"):
    index = 1 
    code = readtem(temfile)

    pattern = r'char \*str1 = "Hello, ";\s*char \*str2 = "World!";'
    newsens = f''
    res, modified_code = replace(code, pattern, newsens)
    if res == -1:
        print(modified_code)
        return
    
    pattern = r'ssize_t numBytes = writev\(fd, iov, 2\);'
    newsens = f'off_t offset = lseek(fd, 0, SEEK_CUR);\n    printf("File current offset before write: %lld\\\\n", (long long)offset);\n    ssize_t numBytes = writev(fd, iov, 2);\n    offset = lseek(fd, 0, SEEK_CUR);\n    printf("File current offset after write: %lld\\\\n", (long long)offset);\n'
    res, modified_code = replace(modified_code, pattern, newsens)
    if res == -1:
        print(modified_code)
        return
            
    for content_size in LEN.gen_ran_len():
        letters = string.ascii_letters + string.digits
        content = ''.join(random.choice(letters) for _ in range(content_size))

        pattern = r'iov\[0\]\.iov_base = (.*?);'
        newsens = f'iov[0].iov_base = "{content}";'
        res, modified_code = replace(modified_code, pattern, newsens)
        if res == -1:
            print(modified_code)
            return

        pattern = r'iov\[1\]\.iov_base = (.*?);'
        newsens = f'iov[1].iov_base = "{content}";'
        res, modified_code = replace(modified_code, pattern, newsens)
        if res == -1:
            print(modified_code)
            return

        pattern = r'iov\[0\]\.iov_len = (.*?);'
        newsens = f'iov[0].iov_len = {content_size};'
        res, modified_code = replace(modified_code, pattern, newsens)
        if res == -1:
            print(modified_code)
            return

        pattern = r'iov\[1\]\.iov_len = (.*?);'
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
    parmu_fd_write()
