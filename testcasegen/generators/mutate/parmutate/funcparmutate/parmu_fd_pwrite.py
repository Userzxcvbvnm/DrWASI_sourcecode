import sys
import re
import random
import string
sys.path.append("../entrance")
from enum import Enum
from parmu_clock_res_get import CLOCK_ID
from temtool import readtem, gen_and_compile, replace
from parmu_fd_advise import OFFSET, LEN, OPENSTYLEFILE

FILE_NAME = "fd_pwrite"


def parmu_fd_pwrite(temfile=f"../../../../../executedir/testcasepool/seeds/{FILE_NAME}_00000.c"):
    index = 1 
    code = readtem(temfile)
    
    insert_code = """
    off_t size = lseek(fd, 0, SEEK_END); 
    printf("Current file size before: %ld\\\\n", size);
"""
    pattern = r'(printf\("Enter function fd_pwrite_.*?\\n"\);)'
    modified_code = re.sub(pattern, r'\1' + insert_code, code)
    
    
    insert_code = """
    size = lseek(fd, 0, SEEK_END); 
    printf("Current file size after: %ld\\\\n", size);
"""
    fixed_if_else = """

"""
    pattern = r'(if \(bytes_written == -1\) {\n        printf\("pwritev failed\\n"\);\n    } else {\n        printf\("pwritev successful. %zd bytes written\\n", bytes_written\);\n    })'
    modified_code = re.sub(pattern, r'\1' + insert_code, modified_code)


    for start_value in OFFSET.gen_ran_offset():
        pattern = r'ssize_t bytes_written = pwritev\(fd, iov, 1, (.*)\);'
        newsens = f'ssize_t bytes_written = pwritev(fd, iov, 1, {start_value});'
        res, modified_code = replace(modified_code, pattern, newsens)
        if res == -1:
            print(modified_code)
            return
            
        for content_size in LEN.gen_ran_len():
            letters = string.ascii_letters + string.digits
            content = ''.join(random.choice(letters) for _ in range(content_size))

            pattern = r'iov\[0\]\.iov_base = "(.*)";'
            newsens = f'iov[0].iov_base = "{content}";'
            res, modified_code = replace(modified_code, pattern, newsens)
            if res == -1:
                print(modified_code)
                return

            pattern = r'iov\[0\]\.iov_len = (.*);'
            newsens = f'iov[0].iov_len = {content_size};'
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
    parmu_fd_pwrite()
