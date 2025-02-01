import re
import sys
sys.path.append("./bugmeta")
from bugmeta_fd_seek import BugMetaFD_SEEK

def judge_fd_seek(items, file2per, runtime, ccontent, snapshotbefore, snapshotafter, logcontent, problemdir):
    print("Judging fd_seek bug ...")

    filename = file2per.split("->")[0] 
    sourcefile = filename
    per = file2per.split("->")[1]
    openstyle = ""
    filesizebefore = ""
    filesizeafter = "" 
    readoffset = ""
    expectoffset = ""
    seekpar = ""
    seeknum = ""
    bugmsg = ""
    
    print(f"filename:{filename}")
    print(f"per:{per}")
    pattern = r'int fd = get_fd\("(.*?)", (.*?)\);'
    match = re.search(pattern, ccontent)
    if match and filename == match.group(1):
        openstyle = match.group(2)
    print(f"openstyle:{openstyle}")   
    
    if filename.startswith("hard") or filename.startswith("soft"):
        pattern = rf"(Hard|Soft)link file: '{filename}' -> '(.*?)'"
        match = re.search(pattern, snapshotbefore)
        if match:
            sourcefile = match.group(2)   
    print(f"sourcefile:{sourcefile}")   
            
    pattern = rf"Normal file: '{sourcefile}'\s*File size: '(\d+)'\s*File content:"
    match = re.search(pattern, snapshotbefore)
    if match:
        filesizebefore = int(match.group(1)) 
    if "O_TRUNC" in openstyle and runtime!="wasmer" and f"Get file descriptor of file {filename} succeed!" in logcontent:
        filesizebefore = 0
    print(f"filesizebefore:{filesizebefore}")
    
    pattern = rf"Normal file: 'Data/{sourcefile}'\s*File size: '(\d+)'\s*File content:"
    match = re.search(pattern, snapshotafter)
    if match:
        filesizeafter = int(match.group(1)) 
    print(f"filesizeafter:{filesizeafter}")

    pattern = r'off_t offset = lseek\(fd, (\d+), (.*?)\);'
    match = re.search(pattern, ccontent)
    if match:
        seeknum = int(match.group(1))
        seekpar = match.group(2)
    print(f"seeknum:{seeknum}")
    print(f"seekpar:{seekpar}")
    
    pattern = r'Enter function fd_seek_.*\nlseek success, new offset is: (\d+)'
    match = re.search(pattern, logcontent)
    if match:
        readoffset = int(match.group(1))
    print(f"readoffset:{readoffset}")
    
    
    if isinstance(seeknum, int) and isinstance(filesizebefore, int) and isinstance(filesizeafter, int):
        if seekpar == "SEEK_SET":
            expectoffset = seeknum
        elif seekpar == "SEEK_CUR":
            expectoffset = seeknum
        elif seekpar == "SEEK_END":
            expectoffset = filesizebefore + seeknum
    print(f"expectoffset:{expectoffset}")
    
    
    if isinstance(readoffset, int) and isinstance(expectoffset, int) and readoffset != expectoffset:
        bugmsg = f"Expected offset is {expectoffset}, but the offset is {readoffset}."
        bugmeta = BugMetaFD_SEEK(runtime=runtime, bugmsg=bugmsg, problemdir=problemdir, 
                                     filename=filename, per=per, openstyle=openstyle,
                                     filesizebefore=filesizebefore, filesizeafter=filesizeafter,
                                     readoffset=readoffset, expectoffset=expectoffset,
                                     seekpar=seekpar, seeknum=seeknum)
        items.append(bugmeta)
    
