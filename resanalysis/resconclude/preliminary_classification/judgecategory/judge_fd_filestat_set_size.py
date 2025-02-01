import re
import sys
sys.path.append("./bugmeta")
from bugmeta_fd_filestat_set_size import BugMetaFD_FILESTAT_SET_SIZE

def judge_fd_filestat_set_size(items, runtime, ccontent, logcontent, snapshotbefore, snapshotafter, problemdir):
    print("Judging fd_filestat_set_size bug ...")
       
    sizebefore = ""
    sizebeforereal = ""
    sizeafter = ""
    readsizebefore = ""
    readsizeafter = ""
    setsize = ""
    openstyle = ""
    filename = ""
    sourcefile = ""
    bugmsg = ""
    
    
    pattern = r'get_fd\("(.*?)", (.*?)\);'
    match = re.search(pattern, ccontent)
    if match:
        filename = match.group(1)
        sourcefile = filename
        openstyle = match.group(2)

        
    if filename.startswith("hard") or filename.startswith("soft"):
        pattern = rf"(Hard|Soft)link file: '{filename}' -> '(.*?)'"
        match = re.search(pattern, snapshotbefore)
        if match:
            sourcefile = match.group(2)    
    print(f"filename:{filename}")
    print(f"sourcefile:{sourcefile}")
    print(f"openstyle:{openstyle}")
    
    pattern = rf"Normal file: '{sourcefile}'\s*File size: '(\d+)'\s*File content:"
    match = re.search(pattern, snapshotbefore)
    if match:
        sizebefore = int(match.group(1)) 
    if "O_TRUNC" in openstyle:
        sizebeforereal = 0
    else:
        sizebeforereal = sizebefore
    print(f"sizebefore:{sizebefore}")
    print(f"sizebeforereal:{sizebeforereal}")
        
    pattern = rf"Normal file: 'Data/{sourcefile}'\s*File size: '(\d+)'\s*File content:"
    match = re.search(pattern, snapshotafter)
    if match:
        sizeafter = int(match.group(1)) 
    print(f"sizeafter:{sizeafter}")   
        
    pattern = r'Current file size:\s*(\d+)\n'
    match = re.search(pattern, logcontent)
    if match:
        readsizebefore = int(match.group(1)) 
    print(f"readsizebefore:{readsizebefore}")


    pattern = r'New file size: (\d+)'
    match = re.search(pattern, logcontent)
    if match:
        readsizeafter = int(match.group(1))    
    print(f"readsizeafter:{readsizeafter}")  


    pattern = r'ftruncate\(fd, (\d+)\)'
    match = re.search(pattern, ccontent)
    if match:
        setsize = int(match.group(1)) 
    print(f"setsize:{setsize}")  
    
    
    tmp = f"Get file descriptor of file {filename} failed!"
    if tmp in logcontent:
        return
    
    if "Failed to adjust file size" in logcontent and openstyle == "O_RDONLY":
        return

    if "File size adjusted successfully" in logcontent and openstyle == "O_RDONLY":
        bugmsg = "open with O_RDONLY but File size adjusted successfully"
        bugmeta = BugMetaFD_FILESTAT_SET_SIZE(runtime=runtime, bugmsg=bugmsg, problemdir=problemdir, 
                                    sizebefore=sizebefore, sizeafter=sizeafter,
                                    readsizebefore=readsizebefore, readsizeafter=readsizeafter,
                                    setsize=setsize,
                                    openstyle=openstyle)
        items.append(bugmeta) 
    
    if "Failed to adjust file size" in logcontent and ("O_WRONLY" in openstyle or "O_RDWR" in openstyle):
        bugmsg = "open with O_WRONLY or O_RDWR but Failed to adjust file size"
        bugmeta = BugMetaFD_FILESTAT_SET_SIZE(runtime=runtime, bugmsg=bugmsg, problemdir=problemdir, 
                                    sizebefore=sizebefore, sizeafter=sizeafter,
                                    readsizebefore=readsizebefore, readsizeafter=readsizeafter,
                                    setsize=setsize,
                                    openstyle=openstyle)
        items.append(bugmeta) 
        
    
    if isinstance(setsize, int) and isinstance(sizeafter, int) and sizeafter != setsize:
        bugmsg = "sizeafter != setsize"
        bugmeta = BugMetaFD_FILESTAT_SET_SIZE(runtime=runtime, bugmsg=bugmsg, problemdir=problemdir, 
                                    sizebefore=sizebefore, sizeafter=sizeafter,
                                    readsizebefore=readsizebefore, readsizeafter=readsizeafter,
                                    setsize=setsize,
                                    openstyle=openstyle)
        items.append(bugmeta)   
        