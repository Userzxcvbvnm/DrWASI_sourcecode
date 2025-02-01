import re
import sys
sys.path.append("./bugmeta")
from bugmeta_fd_fdstat_get import BugMetaFD_FDSTAT_GET

def judge_fd_fdstat_get(items, runtime, logcontent, ccontent, problemdir):
    print("Judging fd_fdstat_get bug ...")
    
    openstyle = ""
    pattern = r'get_fd\("(.*?)", (.*?)\);'
    match = re.search(pattern, ccontent)
    if match:
        openstyle = match.group(2)
    print(f"openstyle:{openstyle}")
        
    getopenstyle = ""
    pattern = r'Access mode:\s*(Read Only|Write Only|Read/Write)'
    match = re.search(pattern, logcontent)
    if match:
        getopenstyle = match.group(1)
    print(f"getopenstyle:{getopenstyle}")
        
    if openstyle != "" and getopenstyle != "":
        if ("O_RDONLY" in openstyle and getopenstyle != "Read Only") or ("O_WRONLY" in openstyle and getopenstyle != "Write Only") or ("O_RDWR" in openstyle and getopenstyle != "Read/Write"):
            bugmeta = BugMetaFD_FDSTAT_GET(runtime=runtime, bugmsg=f"Open with {openstyle}, bug get with {getopenstyle}", problemdir=problemdir, 
                                     openstyle=openstyle, getopenstyle=getopenstyle)
            items.append(bugmeta)
        
       