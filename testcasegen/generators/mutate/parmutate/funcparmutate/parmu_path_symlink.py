import sys
import re
import random
sys.path.append("../entrance")
from enum import Enum
from parmu_clock_res_get import CLOCK_ID
from temtool import readtem, gen_and_compile, replace
from parmu_fd_advise import OFFSET, LEN, OPENSTYLEDIR

FILE_NAME = "path_symlink"




def parmu_path_symlink(temfile=f"../../../../../executedir/testcasepool/seeds/{FILE_NAME}_00000.c"):
    index = 1 
    code = readtem(temfile)
    modified_code = code.replace('    char target[] = "example_target";\n    char linkpath[] = "example_link";','')
    

    pattern = r'int fd = get_fd\("EXAMPLEDIR", O_RDONLY\);\n    if \(fd == -1\) {\n        return 1;\n    }'
    res, modified_code = replace(modified_code, pattern, "")
    if res == -1:
        print(modified_code)
        return
    

    pattern = r'closebyfd\(fd\);'
    res, modified_code = replace(modified_code, pattern, "")
    if res == -1:
        print(modified_code)
        return    
    
    pattern = r'path_symlink_Hxmt0\(fd\);'
    res, modified_code = replace(modified_code, pattern, "path_symlink_Hxmt0();")
    if res == -1:
        print(modified_code)
        return 
    
    
    pattern = r'void path_symlink_Hxmt0\(int fd\)'
    res, modified_code = replace(modified_code, pattern, "void path_symlink_Hxmt0()")
    if res == -1:
        print(modified_code)
        return   
    
    
    pattern = r'if \(symlinkat\(target, fd, linkpath\) == -1\)'
    newsens = f"""if (symlinkat("EXAMPLEFILE", AT_FDCWD, "NEWFILE") == -1)"""
    res, modified_code = replace(modified_code, pattern, newsens)
    if res == -1:
        print(modified_code)
        return


    index = gen_and_compile(index, modified_code, FILE_NAME)


if __name__ == "__main__":
    parmu_path_symlink()
