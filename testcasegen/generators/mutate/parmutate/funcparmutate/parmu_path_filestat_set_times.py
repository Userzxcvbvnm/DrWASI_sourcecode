import sys
import re
import random
sys.path.append("../entrance")
from enum import Enum
from parmu_clock_res_get import CLOCK_ID
from temtool import readtem, gen_and_compile, replace
from parmu_fd_advise import OFFSET, LEN, OPENSTYLEFILE

FILE_NAME = "path_filestat_set_times"

class PATH_TIME_FLAG(Enum):
    ZERO = "0"
    AT_SYMLINK_NOFOLLOW = "AT_SYMLINK_NOFOLLOW"
    AT_SYMLINK_FOLLOW = "AT_SYMLINK_FOLLOW"


def parmu_path_filestat_set_times(temfile=f"../../../../../executedir/testcasepool/seeds/{FILE_NAME}_00000.c"):
    index = 1 
    code = readtem(temfile)
    
    
    insert_code = """
void path_filestat_set_times_WD7wr(int fd, const char *pathname) {
"""
    pattern = r'void path_filestat_set_times_WD7wr\(int fd\) {'
    modified_code = re.sub(pattern, insert_code, code)

    
    insert_code = """
    path_filestat_set_times_WD7wr(fd, "EXAMPLEFILE");
"""
    pattern = r'path_filestat_set_times_WD7wr\(fd\);'
    modified_code = re.sub(pattern, insert_code, modified_code)

    
    insert_code = """
    if (utimensat(AT_FDCWD, "EXAMPLEFILE", times, 0) == 0) {
"""
    pattern = r'if \(utimensat\(AT_FDCWD, "", times, 0\) == 0\) {'
    modified_code = re.sub(pattern, insert_code, modified_code)

        
    for flag in PATH_TIME_FLAG.__members__.values():
        pattern = r'if \(utimensat\(AT_FDCWD, "EXAMPLEFILE", times, (.*?)\) == 0\)'
        newsens = f'if (utimensat(AT_FDCWD, "EXAMPLEFILE", times, {flag.value}) == 0)'
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
    parmu_path_filestat_set_times()
