import re
from pattern import FUNCPATTERN

def checkbycontents(fileprefix, contents):
    if len(contents) <= 1:
        return True

    oracle = contents[0]
    print(f"Oracle before replacement:\n{oracle}")
    oracle = replace_oracle(oracle, fileprefix)
    print(f"Oracle after replacement:\n{oracle}")

    i = 1
    while i < len(contents):
        if re.match(oracle, contents[i], re.DOTALL):
            i = i + 1
        else:
            return False
    return True



def replace_oracle(oracle, fileprefix):
    for p in FUNCPATTERN:
        name = p.name
        pattern = p.value[0]
        replacement = p.value[1]
        if name in fileprefix:
            oracle = re.sub(pattern, replacement, oracle)
            
    return oracle+"$"


def replace_pattern(input_string, pattern):
    modified_string = re.sub(pattern, pattern, input_string)
    return modified_string

