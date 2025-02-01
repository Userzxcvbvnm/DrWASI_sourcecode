import sys
import re
import random
sys.path.append("../entrance")
from enum import Enum
from parmu_clock_res_get import CLOCK_ID
from temtool import readtem, gen_and_compile, replace
from parmu_fd_advise import OFFSET, LEN, OPENSTYLEFILE

FILE_NAME = "fd_fdstat_set_flags"



class SET_FLAGS_PAR(Enum):
    O_APPEND = "O_APPEND"
    O_NONBLOCK = "O_NONBLOCK"



def parmu_fd_fdstat_set_flags(temfile=f"../../../../../executedir/testcasepool/seeds/{FILE_NAME}_00000.c"):
    index = 1 
    code = readtem(temfile)

    pattern = r'int main\(\) {'
    newsens = f'''
    
void print_flags(int fd){{
    int flags1 = fcntl(fd, F_GETFL);
    int access_mode1 = flags1 & O_ACCMODE;
    if (access_mode1 == O_RDONLY) {{
        printf("Access mode: Read Only\\\\n");
    }}
    if (access_mode1 == O_WRONLY) {{
        printf("Access mode: Write Only\\\\n");
    }}
    if (access_mode1 == O_RDWR) {{
        printf("Access mode: Read/Write\\\\n");
    }}
    
    
    if (flags1 & O_APPEND) {{
        printf("Access mode: O_APPEND\\\\n");
    }}
    
    if (flags1 & O_NONBLOCK) {{
        printf("Access mode: Non-blocking\\\\n");
    }}    
}}
    
int main() {{
    '''
    res, modified_code = replace(code, pattern, newsens)
    if res == -1:
        print(modified_code)
        return
    
    
    pattern = r'fd_fdstat_set_flags_(.*?)\(fd\);'
    match = re.search(pattern, modified_code)
    if match:
        id = match.group(1)
    newsens = f'''
    print_flags(fd);\n\
    fd_fdstat_set_flags_{id}(fd);\n\
    printf("After setting flags\\\\n");
    print_flags(fd);\n'''
    res, modified_code = replace(modified_code, pattern, newsens)
    if res == -1:
        print(modified_code)
        return
    
    
    pattern = r'printf\("Setting flags failed!\\n", fd\);'
    newsens = f'printf("Setting flags failed!\\\\n");'
    res, modified_code = replace(modified_code, pattern, newsens)
    if res == -1:
        print(modified_code)
        return
    
    pattern = r'printf\("Setting flags succeed!\\n", fd\);'
    newsens = f'printf("Setting flags succeed!\\\\n");'
    res, modified_code = replace(modified_code, pattern, newsens)
    if res == -1:
        print(modified_code)
        return
    
        
    for par in SET_FLAGS_PAR.__members__.values():
        pattern = r'int flags = fcntl\(fd, F_GETFL\);\n    flags = flags (.*?);\n'
        newsens = f'int flags = fcntl(fd, F_GETFL);\n    flags = flags | {par.value};\n'
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
    parmu_fd_fdstat_set_flags()
