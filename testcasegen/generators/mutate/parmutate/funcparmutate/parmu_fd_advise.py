import sys
import re
import random
sys.path.append("../entrance")
from enum import Enum
from parmu_clock_res_get import CLOCK_ID
from temtool import readtem, gen_and_compile, replace, replace_name

FILE_NAME = "fd_advise"

class FD_ADVISE_PAR(Enum):
    POSIX_FADV_NORMAL = "POSIX_FADV_NORMAL"
    POSIX_FADV_SEQUENTIAL = "POSIX_FADV_SEQUENTIAL"
    POSIX_FADV_RANDOM = "POSIX_FADV_RANDOM"
    POSIX_FADV_WILLNEED = "POSIX_FADV_WILLNEED"
    POSIX_FADV_DONTNEED = "POSIX_FADV_DONTNEED"
    POSIX_FADV_NOREUSE = "POSIX_FADV_NOREUSE"


class OPENSTYLEFILE(Enum):
    c = "O_RDONLY"     
    O_WRONLY = "O_WRONLY"
    O_RDWR = "O_RDWR"
    
    O_WRONLY_or_O_CREAT = "O_WRONLY | O_CREAT"
    O_RDWR_or_O_CREAT = "O_RDWR | O_CREAT"
    
    O_WRONLY_or_O_TRUNC = "O_WRONLY | O_TRUNC"
    O_RDWR_or_O_TRUNC = "O_RDWR | O_TRUNC"
    
    O_WRONLY_or_O_APPEND = "O_WRONLY | O_APPEND"
    O_RDWR_or_O_APPEND = "O_RDWR | O_APPEND"
    
    O_WRONLY_or_O_TRUNC_or_O_CREAT = "O_WRONLY | O_TRUNC | O_CREAT" 
    O_RDWR_or_O_TRUNC_or_O_CREAT = "O_RDWR | O_TRUNC | O_CREAT" 
   

class OPENSTYLEDIR(Enum):
    O_RDONLY = "O_RDONLY | O_DIRECTORY"     
   

class OFFSET():
    @classmethod
    def gen_ran_offset(cls, count=6, min=10, max=500):
        offs = [0]
        for i in range(1, (count-1)//2):
            offs.append(random.randint(1, min))
        for i in range((count-1)//2 ,count):
            offs.append(random.randint(min, max))
        return offs


class LEN():
    @classmethod
    def gen_ran_len(cls, count=6, min=200, max=500):
        return OFFSET.gen_ran_offset()


def parmu_fd_advise(temfile=f"../../../../../executedir/testcasepool/seeds/{FILE_NAME}_00000.c"):
    index = 1 
    code = readtem(temfile)

    for member in FD_ADVISE_PAR.__members__.values():
        par3 = member.value
        
        for offset in OFFSET.gen_ran_offset():
            par1 = offset

            for len in LEN.gen_ran_len():
                par2 = len
                pattern = r'if \(posix_fadvise\(fd, 0, 0, POSIX_FADV_SEQUENTIAL\) == 0\)'
                newsens = f'if (posix_fadvise(fd, {par1}, {par2}, {par3}) == 0)'
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
    parmu_fd_advise()
