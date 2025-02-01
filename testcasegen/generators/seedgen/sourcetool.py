def get_head(filepath):
    res = ""
    with open(filepath, "r") as file:
        lines = file.readlines()
    for l in lines:
        if l.startswith("#include"):
            res += l
    return res


def get_func(filepath, funcname):
    with open(filepath, "r") as file:
        lines = file.readlines()

    content = ""
    in_function = False
    stack = []

    for l in lines:
        if l.startswith(f"void {funcname}") or l.startswith(f"int {funcname}"):
            in_function = True
            content += l 
            stack.append("{")
        elif in_function:
            content += l
            for c in l:
                if c == "{":
                    stack.append("{")
                elif c == "}":
                    stack.pop()
            if len(stack) == 0:
                break
    return content


if __name__ == "__main__":
    print(get_func("../../../executedir/testcasepool/basicoper/get_fd.c", "get_fd"))
