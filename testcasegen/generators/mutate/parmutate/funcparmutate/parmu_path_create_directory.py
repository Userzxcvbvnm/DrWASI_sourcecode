import sys
import re
import random
sys.path.append("../entrance")
from enum import Enum
from parmu_clock_res_get import CLOCK_ID
from temtool import readtem, gen_and_compile, replace
from parmu_fd_advise import OFFSET, LEN, OPENSTYLEDIR

FILE_NAME = "path_create_directory"

class RIGHT(Enum):
    R0000 = "0000"
    R0100 = "0100"
    R0200 = "0200"
    R0300 = "0300"
    R0400 = "0400"
    R0500 = "0500"
    R0600 = "0600"
    R0700 = "0700"


def parmu_path_create_directory(temfile=f"../../../../../executedir/testcasepool/seeds/{FILE_NAME}_00000.c"):
    index = 1 
    code = readtem(temfile)
    
    insert_code = """#include <sys/types.h>
#include <stdlib.h>


void print_path_permissions(const char *path) {
    struct stat path_stat;
    if (stat(path, &path_stat) < 0) {
        perror("Get directory state failed.");
        return;
    }
    mode_t permissions = path_stat.st_mode & (S_IRWXU | S_IRWXG | S_IRWXO);
    printf("Directory '%s' 's permission: %o\\\\n", path, permissions);
}
"""
    pattern = r'#include <sys/types.h>'
    modified_code = re.sub(pattern, insert_code, code)
    
        
    insert_code = """
    print_path_permissions("EXAMPLEDIR/NEWDIR"); 
    closebyfd(fd);
"""
    pattern = r'closebyfd\(fd\);'
    modified_code = re.sub(pattern, insert_code, modified_code)
        
    for right in RIGHT.__members__.values():
        pattern = r'if \(mkdirat\(fd, "NEWDIR", (.*?)\)'
        newsens = f'if (mkdirat(fd, "NEWDIR", {right.value})'
        res, modified_code = replace(modified_code, pattern, newsens)
        if res == -1:
            print(modified_code)
            return

        for member in OPENSTYLEDIR.__members__.values():
            pattern = r'int fd = get_fd\("EXAMPLEDIR", (.*)\);'
            newsens = f'int fd = get_fd("EXAMPLEDIR", {member.value});'
            res, modified_code = replace(modified_code, pattern, newsens)
            if res == -1:
                print(modified_code)
                return
            index = gen_and_compile(index, modified_code, FILE_NAME)


if __name__ == "__main__":
    parmu_path_create_directory()
