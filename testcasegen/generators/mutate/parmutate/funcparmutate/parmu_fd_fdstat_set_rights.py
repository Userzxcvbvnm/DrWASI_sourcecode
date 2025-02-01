import sys
import re
import random
sys.path.append("../entrance")
from enum import Enum
from parmu_clock_res_get import CLOCK_ID
from temtool import readtem, gen_and_compile, replace
from parmu_fd_advise import OFFSET, LEN, OPENSTYLEFILE

FILE_NAME = "fd_fdstat_set_rights"

class WASI_RIGHT_PAR(Enum):
    __WASI_RIGHTS_FD_READ = "__WASI_RIGHTS_FD_READ"
    __WASI_RIGHTS_FD_WRITE = "__WASI_RIGHTS_FD_WRITE"
    __WASI_RIGHTS_FD_FDSTAT_SET_FLAGS = "__WASI_RIGHTS_FD_FDSTAT_SET_FLAGS"
    __WASI_RIGHTS_FD_SEEK = "__WASI_RIGHTS_FD_SEEK"
    __WASI_RIGHTS_FD_SYNC = "__WASI_RIGHTS_FD_SYNC"
    __WASI_RIGHTS_FD_TELL = "__WASI_RIGHTS_FD_TELL"
    __WASI_RIGHTS_FD_ADVISE = "__WASI_RIGHTS_FD_ADVISE"
    __WASI_RIGHTS_FD_ALLOCATE = "__WASI_RIGHTS_FD_ALLOCATE"
    __WASI_RIGHTS_PATH_CREATE_DIRECTORY = "__WASI_RIGHTS_PATH_CREATE_DIRECTORY"
    __WASI_RIGHTS_PATH_CREATE_FILE = "__WASI_RIGHTS_PATH_CREATE_FILE"
    __WASI_RIGHTS_PATH_LINK_SOURCE = "__WASI_RIGHTS_PATH_LINK_SOURCE"
    __WASI_RIGHTS_PATH_LINK_TARGET = "__WASI_RIGHTS_PATH_LINK_TARGET"
    __WASI_RIGHTS_PATH_OPEN = "__WASI_RIGHTS_PATH_OPEN"
    __WASI_RIGHTS_FD_READDIR = "__WASI_RIGHTS_FD_READDIR"
    __WASI_RIGHTS_PATH_READLINK = "__WASI_RIGHTS_PATH_READLINK"
    __WASI_RIGHTS_PATH_RENAME_SOURCE = "__WASI_RIGHTS_PATH_RENAME_SOURCE"
    __WASI_RIGHTS_PATH_RENAME_TARGET = "__WASI_RIGHTS_PATH_RENAME_TARGET"
    __WASI_RIGHTS_PATH_FILESTAT_GET = "__WASI_RIGHTS_PATH_FILESTAT_GET"
    __WASI_RIGHTS_PATH_FILESTAT_SET_SIZE = "__WASI_RIGHTS_PATH_FILESTAT_SET_SIZE"
    __WASI_RIGHTS_PATH_FILESTAT_SET_TIMES = "__WASI_RIGHTS_PATH_FILESTAT_SET_TIMES"
    __WASI_RIGHTS_FD_FILESTAT_GET = "__WASI_RIGHTS_FD_FILESTAT_GET"
    __WASI_RIGHTS_FD_FILESTAT_SET_SIZE = "__WASI_RIGHTS_FD_FILESTAT_SET_SIZE"
    __WASI_RIGHTS_FD_FILESTAT_SET_TIMES = "__WASI_RIGHTS_FD_FILESTAT_SET_TIMES"
    __WASI_RIGHTS_PATH_SYMLINK = "__WASI_RIGHTS_PATH_SYMLINK"
    __WASI_RIGHTS_PATH_REMOVE_DIRECTORY = "__WASI_RIGHTS_PATH_REMOVE_DIRECTORY"
    __WASI_RIGHTS_PATH_UNLINK_FILE = "__WASI_RIGHTS_PATH_UNLINK_FILE"
    __WASI_RIGHTS_POLL_FD_READWRITE = "__WASI_RIGHTS_POLL_FD_READWRITE"
    __WASI_RIGHTS_SOCK_SHUTDOWN = "__WASI_RIGHTS_SOCK_SHUTDOWN"
    __WASI_RIGHTS_SOCK_ACCEPT = "__WASI_RIGHTS_SOCK_ACCEPT"



def parmu_fd_fdstat_set_rights(temfile=f"../../../../../executedir/testcasepool/seeds/{FILE_NAME}_00000.c"):
    index = 1 
    code = readtem(temfile)

        
    for par in WASI_RIGHT_PAR.__members__.values():
        pattern = r'__wasi_rights_t new_rights = __WASI_RIGHTS_FD_READ;'
        newsens = f'__wasi_rights_t new_rights = {par.value};'
        res, modified_code = replace(code, pattern, newsens)
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
    parmu_fd_fdstat_set_rights()
