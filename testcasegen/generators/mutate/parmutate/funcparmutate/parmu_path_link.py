import sys
import re
import random
sys.path.append("../entrance")
from enum import Enum
from parmu_clock_res_get import CLOCK_ID
from temtool import readtem, gen_and_compile, replace
from parmu_fd_advise import OFFSET, LEN

FILE_NAME = "path_link"

class LINK_PAR(Enum):
    AT_SYMLINK_FOLLOW = "AT_SYMLINK_FOLLOW"
    AT_SYMLINK_NOFOLLOW = "AT_SYMLINK_NOFOLLOW"


def parmu_path_link(temfile=f"../../../../../executedir/testcasepool/seeds/{FILE_NAME}_00000.c"):
    index = 1 
    code = readtem(temfile)

    insert_code = """
void path_link_Nan21() {
"""
    pattern = r'void path_link_Nan21\(int fd\) {'
    modified_code = re.sub(pattern, insert_code, code)
 
 
    insert_code = """
    path_link_Nan21();
"""
    pattern = r'path_link_Nan21\(fd\);'
    modified_code = re.sub(pattern, insert_code, modified_code)

    
    pattern = r"""int dir_fd = get_fd\("exampledir", O_RDONLY\);
    if \(dir_fd == -1\) {
        return;
    }
    
    char target_path\[\] = "path/to/targetfile";
    char link_path\[\] = "path/to/linkfile";"""
    modified_code = re.sub(pattern, "", modified_code)     

    
    pattern = r"""int fd = get_fd\("examplefile", O_RDONLY\);
    if \(fd == -1\) {
        return 1;
    }"""
    modified_code = re.sub(pattern, "", modified_code)
    
        
    pattern = r'closebyfd\(dir_fd\);'
    modified_code = re.sub(pattern, "", modified_code)

    pattern = r'closebyfd\(fd\);'
    modified_code = re.sub(pattern, "", modified_code)   
    
    pattern = r'perror\("linkat failed"\);'
    modified_code = re.sub(pattern, 'printf("linkat failed");', modified_code)   
    
    for par in LINK_PAR.__members__.values():
        pattern = r'int result = linkat\((.*?), (.*?), (.*?), (.*?), (.*?)\);'
        newsens = f'int result = linkat(AT_FDCWD, "EXAMPLEFILE", AT_FDCWD, "HARDLINKFILE", {par.value});'
        res, modified_code = replace(modified_code, pattern, newsens)
        if res == -1:
            print(modified_code)
            return

        index = gen_and_compile(index, modified_code, FILE_NAME)
        
if __name__ == "__main__":
    parmu_path_link()
