import sys
import re
import random
sys.path.append("../entrance")
from enum import Enum
from parmu_clock_res_get import CLOCK_ID
from temtool import readtem, gen_and_compile, replace
from parmu_fd_advise import OFFSET, LEN, OPENSTYLEFILE

FILE_NAME = "fd_fdstat_get"


def parmu_fd_fdstat_get(temfile=f"../../../../../executedir/testcasepool/seeds/{FILE_NAME}_00000.c"):
    index = 1 
    code = readtem(temfile)
    
    
    insert_code = """
    if (access_mode == O_RDONLY) {
        printf("Access mode: Read Only\\\\n");
    }
    if (access_mode == O_WRONLY) {
        printf("Access mode: Write Only\\\\n");
    }
    if (access_mode == O_RDWR) {
        printf("Access mode: Read/Write\\\\n");
    }

    if (flags & O_APPEND) {
        printf("Flag: O_APPEND\\\\n");
    }"""
    pattern = r'switch\(access_mode\) \{.*?\}'
    modified_code = re.sub(pattern, insert_code, code, flags=re.DOTALL)
    

    for member in OPENSTYLEFILE.__members__.values():
        pattern = r'int fd = get_fd\("EXAMPLEFILE", (.*)\);'
        newsens = f'int fd = get_fd("EXAMPLEFILE", {member.value});'
        res, modified_code = replace(modified_code, pattern, newsens)
        if res == -1:
            print(modified_code)
            return
        index = gen_and_compile(index, modified_code, FILE_NAME)



if __name__ == "__main__":
    parmu_fd_fdstat_get()
