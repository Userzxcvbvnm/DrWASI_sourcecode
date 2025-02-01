import sys
import re
sys.path.append("../../../compiler")
sys.path.append("../../../seedgen")
from handwritten import HandWritten, WASIfunc
from ccompiler import CCompiler
from wasmcompiler import WasmCompiler

def readtem(temfile):
    with open(temfile, 'r') as file:
        file_contents = file.read()
    return file_contents
def replace(code, pattern, newsens, matchindex=0):
    match = re.search(pattern, code)
    if match:
        replaced_string = re.sub(pattern, newsens, match.group(matchindex))
        modified_code = code[:match.start()] + replaced_string + code[match.end():]
        return 0, modified_code
    else:
        return -1, "No much pattern, replace error!"

def replace_name(code, old, new):
    return code.replace(old, new)

def gen_and_compile(index, filecontent, filename, seeddir="../../../../../executedir/testcasepool/testcases"):
    formatted_index = str(index).zfill(5)
    formatted_file = f"{filename}_{formatted_index}"
    filecontent = replace_name(filecontent, f'{filename}', f'{filename}_{formatted_index}')

    
    if filename == "fd_fdstat_set_rights" or filename == "fd_filestat_get" or filename == "fd_renumber" or filename == "random_get":
        filecontent = replace_name(filecontent, f'__wasi_{filename}_{formatted_index}', f'__wasi_{filename}')
    if filename == "sched_yield":
        filecontent = replace_name(filecontent, f'sched_yield_{formatted_index}();', f'sched_yield();')
    
    seedpath = f"{seeddir}/{formatted_file}.c"
    with open(seedpath, 'w') as file:
        file.write(filecontent)

    return index + 1