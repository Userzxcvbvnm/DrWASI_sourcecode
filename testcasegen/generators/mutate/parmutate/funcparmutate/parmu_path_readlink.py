import sys
import re
import random
sys.path.append("../entrance")
from enum import Enum
from parmu_clock_res_get import CLOCK_ID
from temtool import readtem, gen_and_compile, replace
from parmu_fd_advise import OFFSET, LEN, OPENSTYLEDIR

FILE_NAME = "path_readlink"




def parmu_path_readlink(temfile=f"../../../../../executedir/testcasepool/seeds/{FILE_NAME}_00000.c"):
    index = 1 
    code = readtem(temfile)

    pattern = r'ssize_t numBytes = readlinkat\(fd, ".", link, 100\);'
    newsens = f'ssize_t numBytes = readlinkat(AT_FDCWD, "EXAMPLEFILE", link, 100);'
    res, modified_code = replace(code, pattern, newsens)
    if res == -1:
        print(modified_code)
        return  
     
    pattern = r'perror\("readlinkat"\);'
    newsens = f'printf("readlinkat\\\\n");'
    res, modified_code = replace(modified_code, pattern, newsens)
    if res == -1:
        print(modified_code)
        return  
    
    pattern = r'void path_readlink_xYCLW\(int fd\) {'
    newsens = f"""void path_readlink_xYCLW() {{"""
    res, modified_code = replace(modified_code, pattern, newsens)
    if res == -1:
        print(modified_code)
        return  
    
    pattern = r'path_readlink_(.*)\(fd\);'
    match = re.search(pattern, modified_code)
    if match:
        str = match.group(1) 
    res, modified_code = replace(modified_code, pattern, f"path_readlink_{str}();")
    if res == -1:
        print(modified_code)
        return    
    
    pattern = r'closebyfd\(fd\);'
    res, modified_code = replace(modified_code, pattern, "")
    if res == -1:
        print(modified_code)
        return   
       
    pattern = r'int fd = get_fd\("EXAMPLEFILE", O_RDONLY\);\n    if \(fd == -1\) {\n        return -1;\n    }'
    res, modified_code = replace(modified_code, pattern, "")
    if res == -1:
        print(modified_code)
        return     

    index = gen_and_compile(index, modified_code, FILE_NAME)


if __name__ == "__main__":
    parmu_path_readlink()
