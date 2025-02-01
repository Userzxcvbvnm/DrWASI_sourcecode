import sys
import re
sys.path.append("../entrance")
from enum import Enum
from temtool import readtem, gen_and_compile, replace

FILE_NAME = "proc_exit"


def parmu_proc_exit(temfile=f"../../../../../executedir/testcasepool/seeds/{FILE_NAME}_00000.c"):
    index = 1 
    code = readtem(temfile)

    pattern = r'exit\(0\);'
    newsens = f''
    res, modified_code = replace(code, pattern, newsens)
    if res == -1:
        print(modified_code)
        return
    index = gen_and_compile(index, modified_code, FILE_NAME)


if __name__ == "__main__":
    parmu_proc_exit()