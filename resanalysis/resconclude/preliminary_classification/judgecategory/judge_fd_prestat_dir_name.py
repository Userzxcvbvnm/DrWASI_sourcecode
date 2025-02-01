import re
import sys
sys.path.append("./bugmeta")
from bugmeta_fd_prestat_dir_name import BugMetaFD_PRESTAT_DIR_NAME

def judge_fd_prestat_dir_name(items, runtime, ccontent, logcontent, problemdir):
    print("Judging fd_prestat_dir_name bug ...")

    bugmsg = ""  
    opestyle = ""
    modevalue = ""
    modemsg = []
        
    pattern = r'int fd = get_fd\(".*", (.*?)\);'
    match = re.search(pattern, ccontent)
    if match:
        openstyle = match.group(1)
    print(f"openstyle:{openstyle}")
    
    pattern = r'Enter function fd_prestat_dir_name_.*\nc (\d+)\n'
    match = re.search(pattern, logcontent)
    if match:
        modevalue = match.group(1)
    print(f"modevalue:{modevalue}")
        
    pattern = r'((.*?) access)'
    matches = re.findall(pattern, logcontent)
    for match in matches:
        modemsg.append(match[1])
    print(f"modemsg:{modemsg}")   
    
    
    if "O_WRONLY" in openstyle and ("Read-only" in modemsg or "Read and write" in modemsg):
        bugmsg = "Open without READ, but print write."
        bugmeta = BugMetaFD_PRESTAT_DIR_NAME(runtime=runtime, bugmsg=bugmsg, problemdir=problemdir, 
                                    openstyle=openstyle, modevalue=modevalue, modemsg=modemsg)
        items.append(bugmeta)
        
    if "O_RDONLY" in openstyle and "Read and write" in modemsg:
        bugmsg = "Open without WRITE, but print read."
        bugmeta = BugMetaFD_PRESTAT_DIR_NAME(runtime=runtime, bugmsg=bugmsg, problemdir=problemdir, 
                                    openstyle=openstyle, modevalue=modevalue, modemsg=modemsg)
        items.append(bugmeta)