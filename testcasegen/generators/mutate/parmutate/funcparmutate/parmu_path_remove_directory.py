import sys
import re
import random
sys.path.append("../entrance")
from enum import Enum
from parmu_clock_res_get import CLOCK_ID
from temtool import readtem, gen_and_compile, replace
from parmu_fd_advise import OFFSET, LEN, OPENSTYLEDIR

FILE_NAME = "path_remove_directory"




def parmu_path_remove_directory(temfile=f"../../../../../executedir/testcasepool/seeds/{FILE_NAME}_00000.c"):
    index = 1 
    code = readtem(temfile)

    pattern = r'int fd = get_fd\("EXAMPLEDIR", O_RDONLY\);\n    if \(fd == -1\) {\n        return -1;\n    }'
    res, modified_code = replace(code, pattern, "")
    if res == -1:
        print(modified_code)
        return  
    
    pattern = r'char \*path = ".";'
    res, modified_code = replace(modified_code, pattern, "")
    if res == -1:
        print(modified_code)
        return  

    
    pattern = r'closebyfd\(fd\);'
    res, modified_code = replace(modified_code, pattern, "")
    if res == -1:
        print(modified_code)
        return   

    
    pattern = r'path_remove_directory_(.*)\(fd\);'
    match = re.search(pattern, modified_code)
    if match:
        str = match.group(1) 
    res, modified_code = replace(modified_code, pattern, f"path_remove_directory_{str}();")
    if res == -1:
        print(modified_code)
        return  

    
    pattern = r'void path_remove_directory_k8mfw\(int fd\) {'
    newsens = f"""void path_remove_directory_k8mfw() {{"""
    res, modified_code = replace(modified_code, pattern, newsens)
    if res == -1:
        print(modified_code)
        return    

    
    pattern = r'if \(unlinkat\(fd, path, AT_REMOVEDIR\) == 0\)'
    newsens = f'if (unlinkat(AT_FDCWD, "EXAMPLEDIR", AT_REMOVEDIR) == 0)'
    res, modified_code = replace(modified_code, pattern, newsens)
    if res == -1:
        print(modified_code)
        return

    
    index = gen_and_compile(index, modified_code, FILE_NAME)


if __name__ == "__main__":
    parmu_path_remove_directory()
