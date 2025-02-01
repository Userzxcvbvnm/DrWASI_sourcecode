import sys
import re
import random
sys.path.append("../entrance")
from enum import Enum
from parmu_clock_res_get import CLOCK_ID
from temtool import readtem, gen_and_compile, replace
from parmu_fd_advise import OFFSET, LEN, OPENSTYLEFILE

FILE_NAME = "fd_allocate"




def parmu_fd_allocate(temfile=f"../../../../../executedir/testcasepool/seeds/{FILE_NAME}_00000.c"):
    index = 1 
    code = readtem(temfile)

    pattern = r'#include <sys/stat.h>'
    replacement_code = '#include <sys/stat.h>\n\nvoid print_file_size(int fd){\n    struct stat st;\n    if (fstat(fd, &st) == -1) {\n        printf("Get file size failed.\\n");\n    } else {\n        printf("Get file size: %ld bytes.\\n", st.st_size);\n    }\n}\n'
    modified_code = code.replace(pattern, replacement_code)
        
        
    pattern = r'fd_allocate_gxX49\(fd\);'
    newsens = f'print_file_size(fd);\n    fd_allocate_gxX49(fd);\n    print_file_size(fd);\n'
    res, modified_code = replace(modified_code, pattern, newsens)
    if res == -1:
        print(modified_code)
        return
            
    for offset in OFFSET.gen_ran_offset():
        par1 = offset

        for len in LEN.gen_ran_len():
            par2 = len
            pattern = r'int result = posix_fallocate\(fd, (.*), (.*)\);'
            newsens = f'int result = posix_fallocate(fd, {par1}, {par2});'
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
    parmu_fd_allocate()
