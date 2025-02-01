import sys
import re
sys.path.append("../entrance")
from enum import Enum
from temtool import readtem, gen_and_compile, replace

FILE_NAME = "poll_oneoff"

class TIMEOUT_TIME(Enum):
    FIVE = "5000"
    THREE = "3000"
    ONE = "1000"

def parmu_poll_oneoff(temfile=f"../../../../../executedir/testcasepool/seeds/{FILE_NAME}_00000.c"):
    index = 1 
    code = readtem(temfile)

    for time in TIMEOUT_TIME.__members__.values():
        pattern = r'ret = poll\(fds, 1, -1\);'
        newsens = f'ret = poll(fds, 1, {time.value});'
        res, modified_code = replace(code, pattern, newsens)
        if res == -1:
            print(modified_code)
            return
        index = gen_and_compile(index, modified_code, FILE_NAME)


if __name__ == "__main__":
    parmu_poll_oneoff()