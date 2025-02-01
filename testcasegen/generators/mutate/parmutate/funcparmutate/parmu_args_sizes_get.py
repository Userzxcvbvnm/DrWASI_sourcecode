import sys
sys.path.append("../entrance")
from temtool import readtem, gen_and_compile


FILE_NAME = "args_sizes_get"

def parmu_args_sizes_get(temfile=f"../../../../../executedir/testcasepool/seeds/{FILE_NAME}_00000.c"):
    index = 1 
    code = readtem(temfile)
    index = gen_and_compile(index, code, FILE_NAME)


if __name__ == "__main__":
    parmu_args_sizes_get()