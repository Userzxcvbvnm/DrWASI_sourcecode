import sys
import re
import random
sys.path.append("../entrance")
from enum import Enum
from parmu_clock_res_get import CLOCK_ID
from temtool import readtem, gen_and_compile, replace
from parmu_fd_advise import OFFSET, LEN, OPENSTYLEDIR

FILE_NAME = "fd_readdir"


def parmu_fd_readdir(temfile=f"../../../../../executedir/testcasepool/seeds/{FILE_NAME}_00000.c"):
    index = 1 
    code = readtem(temfile)
    
    pattern = r'closedir\(directory\);'
    newsens = f'printf("Print dir content finished.\\\\n");'
    res, modified_code = replace(code, pattern, newsens)
    if res == -1:
        print(modified_code)
        return 
    
    
    pattern = r'printf\("%s\\n", entry->d_name\);'
    newsens = f'printf("Get dir content:%s\\\\n", entry->d_name);'
    res, modified_code = replace(modified_code, pattern, newsens)
    if res == -1:
        print(modified_code)
        return    
    
    
    for member in OPENSTYLEDIR.__members__.values():
        pattern = r'int fd = get_fd\("EXAMPLEDIR", (.*)\);'
        newsens = f'int fd = get_fd("EXAMPLEDIR", {member.value});'
        res, modified_code = replace(modified_code, pattern, newsens)
        if res == -1:
            print(modified_code)
            return
        index = gen_and_compile(index, modified_code, FILE_NAME)


if __name__ == "__main__":
    parmu_fd_readdir()
