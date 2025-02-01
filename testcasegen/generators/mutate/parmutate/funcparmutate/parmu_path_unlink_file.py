import sys
import re
import random
sys.path.append("../entrance")
from enum import Enum
from parmu_clock_res_get import CLOCK_ID
from temtool import readtem, gen_and_compile, replace
from parmu_fd_advise import OFFSET, LEN, OPENSTYLEDIR

FILE_NAME = "path_unlink_file"




def parmu_path_unlink_file(temfile=f"../../../../../executedir/testcasepool/seeds/{FILE_NAME}_00000.c"):
    index = 1 
    code = readtem(temfile)
    

    pattern = r'int fd = get_fd\("example.txt", O_RDONLY\);\n    if \(fd == -1\) {\n        return -1;\n    }'
    res, modified_code = replace(code, pattern, "")
    if res == -1:
        print(modified_code)
        return
    
    pattern = r'closebyfd\(fd\);'
    res, modified_code = replace(modified_code, pattern, "")
    if res == -1:
        print(modified_code)
        return  
 
 
    pattern = r'path_unlink_file_ggOQt\(fd\);'
    res, modified_code = replace(modified_code, pattern, "path_unlink_file_ggOQt();")
    if res == -1:
        print(modified_code)
        return    
    
    pattern = r'void path_unlink_file_ggOQt\(int fd\)'
    res, modified_code = replace(modified_code, pattern, "void path_unlink_file_ggOQt()")
    if res == -1:
        print(modified_code)
        return 
    
    pattern = r'const char\* path = "example.txt";'
    res, modified_code = replace(modified_code, pattern, "")
    if res == -1:
        print(modified_code)
        return 
    
    pattern = r'if \(unlinkat\(fd, path, 0\) == -1\)'
    res, modified_code = replace(modified_code, pattern, """if (unlinkat(AT_FDCWD, "EXAMPLEFILE", 0) == -1)""")
    if res == -1:
        print(modified_code)
        return 
    
    index = gen_and_compile(index, modified_code, FILE_NAME)


if __name__ == "__main__":
    parmu_path_unlink_file()
