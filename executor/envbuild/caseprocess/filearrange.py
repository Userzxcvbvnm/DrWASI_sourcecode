import random
import re
import sys
sys.path.append("../../testcasegen/generators/compiler")
from ccompiler import CCompiler
from wasmcompiler import WasmCompiler
import os


def arrage(unitdir, casename, repeatfile=False, repeatdir = False):
    seedsdir = "../../executedir/testcasepool/testcases"
    filenames, dirnames, code = get_names(f"{seedsdir}/{casename}.c")
    print(f"Files to be replaced:")
    for f in filenames:
        print(f)
    print(f"Dirs to be replaced:")
    for d in dirnames:
        print(d)
    

    codenew, arragefiles = arragefile(unitdir, code, filenames, repeatfile)
    codenew, arragedirs = arragedir(unitdir, codenew, dirnames, repeatfile)

    print(f"Code after replacement:\n{codenew}")
    with open(f"{seedsdir}/{casename}_tmp.c", 'w') as file:
        file.write(codenew)

   
    wasmcompiler = WasmCompiler()
    wasmcompiler.compile(f"{seedsdir}/{casename}_tmp.c", f"{wasmcompiler.wasmdir}/{casename}_tmp.wasm")
    wasmcompiler.wasm2wat(f"{wasmcompiler.wasmdir}/{casename}_tmp.wasm", f"{wasmcompiler.watdir}/{casename}_tmp.wat")
    
    return f"{casename}_tmp", arragefiles, arragedirs


def get_names(filepath):
    with open(filepath, 'r') as file:
        code = file.read()
    filenames = list(set(re.findall(r'"(EXAMPLEFILE[^"]*)"', code)))
    dirnames = list(set(re.findall(r'"(EXAMPLEDIR[^"]*)"', code)))
    
    if "EXAMPLEDIR/NEWDIR" in dirnames:
        dirnames.remove("EXAMPLEDIR/NEWDIR")
    
    return filenames, dirnames, code


def arragefile(unitdir, code, filenames, repeat=False):
    if len(filenames) == 0:
        return code, []

    arragedfiles = []

    if repeat:
        for f in filenames:
            selected_array = random.choice([unitdir.normalfiles, unitdir.softlinkfiles, unitdir.hardlinkfiles]) 
            arragedfiles.append(random.choice(selected_array))
    else:
        merged_array = unitdir.normalfiles + unitdir.softlinkfiles + unitdir.hardlinkfiles
        arragedfiles = random.sample(merged_array, len(filenames))

    newnamefiles = []
    for f in arragedfiles:
        newnamefiles.append(f.name) 
      
    for i in range(len(filenames)):
        print(f"Replace {filenames[i]} with {newnamefiles[i]}")
        code = code.replace(f"\"{filenames[i]}\"", f"\"{newnamefiles[i]}\"") 
    
    return code, newnamefiles


def arragedir(unitdir, code, dirnames, repeat=False):
    if len(dirnames) == 0:
        return code, []

    arrageddirs = []

    if repeat:
        for f in dirnames:
            arragedfiles.append(random.choice(unitdir.dirs))
    else:
        arrageddirs = random.sample(unitdir.dirs, len(dirnames))
    index = -1
    for i in range(len(arrageddirs)):
        if arrageddirs[i].name == ".":
            index = i
            break
    if index >= 0:
        arrageddirs.pop(index)

    while len(arrageddirs) == 0:
        if repeat:
            for f in dirnames:
                arragedfiles.append(random.choice(unitdir.dirs))
        else:
            arrageddirs = random.sample(unitdir.dirs, len(dirnames))
        index = -1
        for i in range(len(arrageddirs)):
            if arrageddirs[i].name == ".":
                index = i
                break
        if index >= 0:
            arrageddirs.pop(index)  
         
    newnamedirs = []
    for d in arrageddirs:
        newnamedirs.append(d.name.replace("Data", ".", 1))


    for i in range(len(dirnames)):
        print(f"Replace {dirnames[i]} with {newnamedirs[i]}")
        code = code.replace(dirnames[i], newnamedirs[i])  
        

    return code, newnamedirs
     