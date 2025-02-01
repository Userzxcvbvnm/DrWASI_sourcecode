import sys
import re
sys.path.append("../entrance")
from enum import Enum
from temtool import readtem, gen_and_compile, replace

FILE_NAME = "clock_res_get"

class CLOCK_ID(Enum):
    CLOCK_REALTIME = "CLOCK_REALTIME"
    CLOCK_MONOTONIC = "CLOCK_MONOTONIC"
  


def parmu_clock_res_get(temfile=f"../../../../../executedir/testcasepool/seeds/{FILE_NAME}_00000.c"):
    index = 1 
    code = readtem(temfile)

    for member in CLOCK_ID.__members__.values():
        pattern = r'clock_getres\(CLOCK_MONOTONIC, &res\);'
        newsens = f'clock_getres({member.value}, &res);'
        res, modified_code = replace(code, pattern, newsens)
        if res == -1:
            print(modified_code)
            return
        index = gen_and_compile(index, modified_code, FILE_NAME)


if __name__ == "__main__":
    parmu_clock_res_get()