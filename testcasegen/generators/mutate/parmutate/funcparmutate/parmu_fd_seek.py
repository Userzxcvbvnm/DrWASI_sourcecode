import sys
import re
import random
import string
sys.path.append("../entrance")
from enum import Enum
from parmu_clock_res_get import CLOCK_ID
from temtool import readtem, gen_and_compile, replace
from parmu_fd_advise import OFFSET, LEN, OPENSTYLEFILE

FILE_NAME = "fd_seek"

class SEEK_PAR(Enum):
    SEEK_SET = "SEEK_SET"
    SEEK_CUR = "SEEK_CUR"
    SEEK_END = "SEEK_END"


def parmu_fd_seek(temfile=f"../../../../../executedir/testcasepool/seeds/{FILE_NAME}_00000.c"):
    index = 1 
    code = readtem(temfile)

    for offset in OFFSET.gen_ran_offset():

        for member in SEEK_PAR.__members__.values():
            pattern = r'off_t offset = lseek\(fd, 0, SEEK_SET\);'
            newsens = f'off_t offset = lseek(fd, {offset}, {member.value});'
            res, modified_code = replace(code, pattern, newsens)
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
    parmu_fd_seek()
