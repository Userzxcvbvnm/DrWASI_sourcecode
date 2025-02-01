import os
import sys
import re
from pathlib import Path
sys.path.append("../../../executor/envbuild/permission")
from bugitem import judge
from permission import FilePer, DirPer, Type


PLATFORM = "Linux"
NUMBER = 0

def judge_all():
    PROBLEMDIR = f"../../../executedir/linuxdir/problem"
    if version == "new":
        PROBLEMDIR = f"../../../executedir/linuxdir/problem/new_version/"
        base_path = Path(PROBLEMDIR)
        subdirectories = [sub_path for sub_path in base_path.iterdir() if sub_path.is_dir()]
        for subdir in subdirectories:
            judge_wasifunc(curwasifunc=subdir, version="new")
        
    elif version == "old":
        PROBLEMDIR = f"../../../executedir/linuxdir/problem/old_version/"
        base_path = Path(PROBLEMDIR)
        subdirectories = [sub_path for sub_path in base_path.iterdir() if sub_path.is_dir()]
        for subdir in subdirectories:
            judge_wasifunc(curwasifunc=subdir, version="old")


def judge_wasifunc(curwasifunc, version = "None", maxindex=1, minindex=5000):
    PROBLEMDIR = f"../../../executedir/linuxdir/problem/{curwasifunc}"
    if version == "new":
        PROBLEMDIR = f"../../../executedir/linuxdir/problem/new_version/{curwasifunc}"
    elif version == "old":
        PROBLEMDIR = f"../../../executedir/linuxdir/problem/old_version/{curwasifunc}"
        
    
    if "windows" in PROBLEMDIR:
        PLATFORM = "Windows"
        PROBLEMDIR = f"../../../executedir/windows/problem/{curwasifunc}"
    elif "linux" in PROBLEMDIR:
        PLATFORM = "Linux"
        
    if maxindex == -1:
        for _, dirnames, _ in os.walk(PROBLEMDIR):
            for dirname in dirnames:
                judge_bug_category(os.path.join(PROBLEMDIR, dirname), version=version) 
    else:
        for _, dirnames, _ in os.walk(PROBLEMDIR):
            for i in range(minindex, maxindex):
                formatted_num = "{:05d}".format(i)
                prefix = f"{curwasifunc}_{formatted_num}"
                for dirname in dirnames:
                    if dirname.startswith(prefix):
                        judge_bug_category(os.path.join(PROBLEMDIR, dirname), version=version) 
        

                    
def judge_bug_category(problemdir, version="None"):
    print(f"\n\n\n\n\n~~~~~~~~~Processing problem {problemdir} ...~~~~~~~~~")

    bugmetas = []
    
    shortfilename = problemdir.split("/")[-1]
    name = shortfilename.split("-", 1)[0]
    logfile = f"{problemdir}/{name}.log"
    cfile = f"{problemdir}/{name}.c"
        
    with open(cfile, "r") as file:
        ccontent = file.read()
        

    with open(logfile, "r") as file:
        logcontent = file.read()
        
        
    snapshotbefore = None
    pattern = re.compile(r"----- Contructed pre directory: -----\n(.*?)\n----- End pre directory -----", re.DOTALL)
    match = pattern.search(logcontent)
    if match:
        snapshotbefore = match.group(1)
        
    snapshotafter = None
    pattern = re.compile(r"----- Check static info: True-----\n---Dump dir: ../../executedir/linuxdir/wasmtime---(.*)\n----- End dump dir -----", re.DOTALL)
    match = pattern.search(logcontent)
    if match:
        snapshotafter = match.group(1)
        

    file2perstr = ""
    fileordir2per = FilePer("", "", Type.FILE)
    pattern = re.compile(r"----- Change permission: (.*?)-----", re.DOTALL)
    match = pattern.search(logcontent)
    if match:
        strs = match.group(1).split()
        if file2perstr == "":
            file2perstr = f"{strs[0]}->{strs[1]}"
        else:
            file2perstr = f"{file2perstr}   {strs[0]}->{strs[1]}"


    pattern = re.compile(
        r'--- (native|wasmer|wasmtime|wamr|wasmedge) start execute ---.*?<stdout>:\s*\n(.*?)\n\s*<stderr>:\s*\n.*?--- (native|wasmer|wasmtime|wamr|wasmedge) finish execute ---',
        re.DOTALL
    )
    matches = pattern.findall(logcontent)


    TESTFLAG = False
    for match in matches:
        runtimename = match[0]
        out = match[1]       
        
        pattern = re.compile(rf"---Dump dir: ../../executedir/linuxdir/{runtimename}---(.*?)\n----- End dump dir -----", re.DOTALL)
        match = pattern.search(logcontent)
        if match:
            snapshotafter = match.group(1)
        
        print(f"Judging {runtimename}'s bug item ...")
        

        
        item_msg = judge(runtimename=runtimename, platform=PLATFORM, problemdir=problemdir,
                                 file2per = file2perstr,
                                 snapshotbefore=snapshotbefore, snapshotafter=snapshotafter,
                                 logcontent=out, ccontent=ccontent)
        if len(item_msg) > 0:
            TESTFLAG = True
            for item in item_msg:
                print(f"\n\n-------- Writing the classified bug --------\n")
                item.print()
                write_res(item, version=version)
    
def write_res(bugmeta, version = "None"):
    global NUMBER
    NUMBER = NUMBER + 1
    RESFILE = f"./classificationresult/{bugmeta.item}_result.txt"
    if version == "new":
        RESFILE = f"./classificationresult/new_version/{bugmeta.item}_result.txt"
    elif version == "old":
        RESFILE = f"./classificationresult/old_version/{bugmeta.item}_result.txt"
    with open(RESFILE, 'a+') as file:
        file.write("--------------------------------------------------\n")
        file.write(bugmeta.get())
        file.write("--------------------------------------------------\n\n\n")



if __name__ == "__main__":
    judge_all()
    print(f"\n\n\n============= Totally {NUMBER} bug records. =============") 
