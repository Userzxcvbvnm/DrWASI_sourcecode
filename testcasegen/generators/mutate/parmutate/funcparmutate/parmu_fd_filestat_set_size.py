import sys
import re
import random
sys.path.append("../entrance")
from enum import Enum
from parmu_clock_res_get import CLOCK_ID
from temtool import readtem, gen_and_compile, replace
from parmu_fd_advise import OFFSET, LEN, OPENSTYLEFILE

FILE_NAME = "fd_filestat_set_size"


def parmu_fd_filestat_set_size(temfile=f"../../../../../executedir/testcasepool/seeds/{FILE_NAME}_00000.c"):
    index = 1 
    code = readtem(temfile)

        
    for newsize in LEN.gen_ran_len():
        pattern = r'if \(ftruncate\(fd, size \+ 100\) == 0\)'
        newsens = f'if (ftruncate(fd, {newsize}) == 0)'
        res, modified_code = replace(code, pattern, newsens)
        if res == -1:
            print(modified_code)
            return

        for member in OPENSTYLEFILE.__members__.values():
            pattern = r'int fd = get_fd\("(.*)", (.*)\);'
            newsens = f'int fd = get_fd("EXAMPLEFILE", {member.value});'
            res, modified_code = replace(modified_code, pattern, newsens)
            if res == -1:
                print(modified_code)
                return
            index = gen_and_compile(index, modified_code, FILE_NAME)


if __name__ == "__main__":\
    parmu_fd_filestat_set_size()
