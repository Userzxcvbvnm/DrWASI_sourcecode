import sys
import re
import random
sys.path.append("../entrance")
from enum import Enum
from parmu_clock_res_get import CLOCK_ID
from temtool import readtem, gen_and_compile, replace
from parmu_fd_advise import OFFSET, LEN, OPENSTYLEDIR, OPENSTYLEFILE

FILE_NAME = "path_rename"




def parmu_path_rename(temfile=f"../../../../../executedir/testcasepool/seeds/{FILE_NAME}_00000.c"):
    index = 1 
    code = readtem(temfile)


    pattern = r'int fd = get_fd\("EXAMPLEFILE", O_RDONLY\);\n    if \(fd == -1\) {\n        return -1;\n    }'
    res, modified_code = replace(code, pattern, "")
    if res == -1:
        print(modified_code)
        return

    pattern = r'closebyfd\(fd\);'
    res, modified_code = replace(modified_code, pattern, "")
    if res == -1:
        print(modified_code)
        return
    
    pattern = r'path_rename_gApN2\(fd\);'
    res, modified_code = replace(modified_code, pattern, "path_rename_gApN2();")
    if res == -1:
        print(modified_code)
        return

    pattern = r'void path_rename_gApN2\(int fd\)'
    res, modified_code = replace(modified_code, pattern, "void path_rename_gApN2()")
    if res == -1:
        print(modified_code)
        return
    
    pattern = r'char old_path\[\] = "old_file.txt";\n    char new_path\[\] = "new_file.txt";'
    res, modified_code = replace(modified_code, pattern, "")
    if res == -1:
        print(modified_code)
        return
    
    pattern = r'renameat\(fd, old_path, fd, new_path\) == 0'
    res, modified_code = replace(modified_code, pattern, """renameat(AT_FDCWD, "EXAMPLEFILE", AT_FDCWD, "NEWNAME") == 0""")
    if res == -1:
        print(modified_code)
        return
    index = gen_and_compile(index, modified_code, FILE_NAME)
    
    
if __name__ == "__main__":
    parmu_path_rename()
