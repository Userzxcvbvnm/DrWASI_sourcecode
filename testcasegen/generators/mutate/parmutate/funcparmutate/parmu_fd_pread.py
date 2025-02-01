import sys
import re
import random
sys.path.append("../entrance")
from enum import Enum
from parmu_clock_res_get import CLOCK_ID
from temtool import readtem, gen_and_compile, replace
from parmu_fd_advise import OFFSET, LEN, OPENSTYLEFILE

FILE_NAME = "fd_pread"

  

def parmu_fd_pread(temfile=f"../../../../../executedir/testcasepool/seeds/{FILE_NAME}_00000.c"):
    index = 1 
    code = readtem(temfile)
    
    insert_code = """
    __wasi_filestat_t filestat;
    __wasi_errno_t result = __wasi_fd_filestat_get(fd, &filestat);
    if (result != 0) {
        printf("Error %d while getting file stat\\\\n", result);
    } else{
        printf("File Size: %llu bytes\\\\n", filestat.size);
    }
"""
    pattern = r'(printf\("Enter function fd_pread_[^\\n]*?\\n"\);)' 
    modified_code = re.sub(pattern, r'\1\n' + insert_code, code)


    pattern = r'perror\("preadv"\);'
    newsens = f'printf("preadv error.\\\\n");'
    res, modified_code = replace(modified_code, pattern, newsens)
    if res == -1:
        print(modified_code)
        return  
    
    for buffersize in LEN.gen_ran_len():
        pattern = r'char buffer\[\d+\];'
        newsens = f'char buffer[{buffersize}];'
        res, modified_code = replace(modified_code, pattern, newsens)
        if res == -1:
            print(modified_code)
            return  

        for start_value in OFFSET.gen_ran_offset():
            pattern = r'ssize_t bytes_read = preadv\(fd, &iov, 1, (.*)\);'
            newsens = f'ssize_t bytes_read = preadv(fd, &iov, 1, {start_value});'
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
    parmu_fd_pread()
