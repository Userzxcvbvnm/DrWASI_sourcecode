import sys
import re
import random
sys.path.append("../entrance")
from enum import Enum
from parmu_clock_res_get import CLOCK_ID
from temtool import readtem, gen_and_compile, replace
from parmu_fd_advise import OFFSET, LEN, OPENSTYLEFILE, OPENSTYLEDIR

FILE_NAME = "path_open"




def parmu_path_open(temfile=f"../../../../../executedir/testcasepool/seeds/{FILE_NAME}_00000.c"):
    index = 1 
    code = readtem(temfile)
    
    pattern = r"""int fd = get_fd\("EXAMPLEDIR", O_RDONLY\);
    if \(fd == -1\) {
        return 1;
    }"""
    modified_code = re.sub(pattern, "", code)

    pattern = r'closebyfd\(fd\);'
    modified_code = re.sub(pattern, "", modified_code) 
    
    pattern = r'path_open_UuZtc\(fd\);'
    modified_code = re.sub(pattern, "path_open_UuZtc(AT_FDCWD);", modified_code) 

    pattern = r'const char \*path = "example.txt";'
    modified_code = re.sub(pattern, "", modified_code) 
    
        
    for open in OPENSTYLEFILE.__members__.values():
        pattern = r'int file_fd = openat\(fd, (.*?), (.*?)\);'
        newsens = f'int file_fd = openat(fd, "EXAMPLEFILE", {open.value});'
        res, modified_code = replace(modified_code, pattern, newsens)
        if res == -1:
            print(modified_code)
            return   
        index = gen_and_compile(index, modified_code, FILE_NAME)
        
    for open in OPENSTYLEDIR.__members__.values():
        pattern = r'int file_fd = openat\(fd, (.*?), (.*?)\);'
        newsens = f'int file_fd = openat(fd, "EXAMPLEDIR", {open.value});'
        res, modified_code = replace(modified_code, pattern, newsens)
        if res == -1:
            print(modified_code)
            return
        index = gen_and_compile(index, modified_code, FILE_NAME)


if __name__ == "__main__":
    parmu_path_open()
