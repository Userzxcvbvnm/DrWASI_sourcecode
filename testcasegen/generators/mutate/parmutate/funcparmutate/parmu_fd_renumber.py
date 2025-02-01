import sys
import re
import random
sys.path.append("../entrance")
from enum import Enum
from parmu_clock_res_get import CLOCK_ID
from temtool import readtem, gen_and_compile, replace
from parmu_fd_advise import OFFSET, LEN, OPENSTYLEFILE

FILE_NAME = "fd_renumber"


def parmu_fd_renumber(temfile=f"../../../../../executedir/testcasepool/seeds/{FILE_NAME}_00000.c"):
    index = 1 
    code = readtem(temfile)
    
    pattern = r'closebyfd\(fd\);'
    newsens = f''
    res, modified_code = replace(code, pattern, newsens)
    if res == -1:
        print(modified_code)
        return
    
    pattern = r'printf\("Leave fd_renumber.\\n"\);\n'
    newsens = f'printf("Leave fd_renumber.\\\\n");\n        closebyfd(new_fd);\n'
    res, modified_code = replace(modified_code, pattern, newsens)
    if res == -1:
        print(modified_code)
        return
    
    for member1 in OPENSTYLEFILE.__members__.values():
        pattern = r'int fd = get_fd\("(EXAMPLEFILE1|EXAMPLEFILE)", (.*?)\);'
        newsens = f'int fd = get_fd("EXAMPLEFILE", {member1.value});'
        res, modified_code = replace(modified_code, pattern, newsens)
        if res == -1:
            print(modified_code)
            return
        for member2 in OPENSTYLEFILE.__members__.values():
            pattern = r'int new_fd = get_fd\("EXAMPLEFILE2", (.*)\); '
            newsens = f'int new_fd = get_fd("EXAMPLEFILE2", {member2.value}); '
            res, modified_code = replace(modified_code, pattern, newsens)
            if res == -1:
                print(modified_code)
                return
            index = gen_and_compile(index, modified_code, FILE_NAME)


if __name__ == "__main__":
    parmu_fd_renumber()
