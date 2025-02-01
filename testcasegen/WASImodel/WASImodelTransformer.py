import re
import os
from WASImodel import Function, WASIModel

def read_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    return content


def write_file(model, file_path):
    with open(file_path, 'w') as file:
        file.write(model.get())




def func_unit(funcontent, model):
    func = Function()
    funcontent = funcontent.lstrip()
    funcontent = funcontent.replace(";;;", "")

    prefix = funcontent.split("(@interface func")[0]
    prefix = prefix.replace("\n","")
    prefix = prefix.lstrip()

    sens = re.split(r'\.\s*', prefix)
    func.functionality = sens[0]

    k = 1
    while k < len(sens):
        match = re.match(r"(.*)Note: This (.*) similar (.*) `(.*)` in (POSIX|Linux)", sens[k])
        if match:
            func.posix = match.group(4)
            break
        k = k + 1

    i = 0
    while i < len(funcontent):
        if (i + 26) < len(funcontent) and funcontent[i:i+26] == '(@interface func (export "':
            j = i + 26
            while funcontent[j] != "\"":
                j = j + 1
            func.name = funcontent[i+26:j]
            i = j
        elif (i + 8) < len(funcontent) and funcontent[i:i+8] == '(param $':
            j = i + 8
            while funcontent[j] != " ":
                j = j + 1
            par = funcontent[i+8:j]
            func.par.add(par)
            if par.__contains__("fd"):
                func.needfd =True
            i = j
        else:
            i = i + 1


    for p in func.par:
        model.par.add(p)
    model.func.append(func)


def extract_model(content):
    model = WASIModel()
    
    i = 0
    while i < len(content):
        if (i + 16) < len(content) and content[i:i+16] == '(@interface func':
            stack = []
            stack.append("(")
            j = i + 16
            while len(stack) > 0:
                if content[j] == '(':
                    stack.append("(")
                elif content[j] == ')':
                    stack.pop()
                j = j + 1
            funcontent = content[i:j-1]

            start_index = i
            while True:
                if (content[start_index-1] == ")" and content[start_index-2] == "\n") or (content[start_index-1] == "\n" and content[start_index-2] == ")" and (content[start_index-7] != "w" and content[start_index-6] != "r" and content[start_index-5] != "i" and content[start_index-4] != "t" and content[start_index-3] != "e")):
                    break
                else:
                    start_index -= 1
            funcontent = f"{content[start_index:i]}{funcontent}"

            func_unit(funcontent, model)
            i = j
        else:
            i = i + 1
    return model


def gen_model(file="./modelfiles/wasi_snapshot_preview1.witx", output="./modelfiles/wasimodel"):
    file_content = read_file(file)
    model = extract_model(file_content)
    model.print()
    write_file(model, output)
    return model

