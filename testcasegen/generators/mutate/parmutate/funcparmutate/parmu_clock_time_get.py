import sys
sys.path.append("../entrance")
from enum import Enum
from parmu_clock_res_get import CLOCK_ID
from temtool import readtem, replace, gen_and_compile

FILE_NAME = "clock_time_get"


def parmu_clock_time_get(temfile=f"../../../../../executedir/testcasepool/seeds/{FILE_NAME}_00000.c"):
    index = 1 
    code = readtem(temfile)
    
    pattern = r"""printf\("Current time: %ld seconds, %ld nanoseconds\\n", ts.tv_sec, ts.tv_nsec\);""";
    newsens = f"""printf("Current time: %lld seconds, %ld nanoseconds\\\\n", ts.tv_sec, ts.tv_nsec);"""
    res, modified_code = replace(code, pattern, newsens)
    if res == -1:
        print(modified_code)
        return
    


    for member in CLOCK_ID.__members__.values():
        pattern = r'if\(clock_gettime\(CLOCK_REALTIME, &ts\) == -1\)'
        newsens = f'if(clock_gettime({member.value}, &ts) == -1)'
        res, modified_code = replace(modified_code, pattern, newsens)
        if res == -1:
            print(modified_code)
            return
        index = gen_and_compile(index, modified_code, FILE_NAME)


if __name__ == "__main__":
    parmu_clock_time_get()