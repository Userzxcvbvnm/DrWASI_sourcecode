import re
import sys
sys.path.append("./bugmeta")
from bugmeta_fd_fdstat_set_rights import BugMetaFD_FDSTAT_SET_RIGHTS

def judge_fd_fdstat_set_rights(items, runtime, ccontent, logcontent, problemdir):
    print("Judging fd_fdstat_set_rights bug ...")
          
    bugmsg = "Setting function right error."
    rightbefore = ""
    setright = ""
    rightafter = ""
    
    pattern = r'Get file descriptor of file (.*?) failed!'
    match = re.search(pattern, logcontent)
    if match:
        return
    
    pattern = r'Current file rights:\s*\n([\s\S]*?)\n\n'
    match = re.search(pattern, logcontent)
    if match:
        rightbefore = match.group(1)

    pattern = r'__wasi_rights_t new_rights = (.*?);'
    match = re.search(pattern, ccontent)
    if match:
        setright = match.group(1)
    

    pattern = re.compile(r"New file rights:\s+(\S+)")
    match = pattern.search(logcontent)
    if match:
        rightafter = match.group(1)
        
    pattern = r'Failed to set fd rights.'
    match = re.search(pattern, logcontent)
    if match:
        bugmsg = f"Failed to set fd rights."
    
    if setright != "" and setright != rightafter:
        bugmeta = BugMetaFD_FDSTAT_SET_RIGHTS(runtime=runtime, bugmsg=bugmsg, problemdir=problemdir, 
                                    rightbefore=rightbefore, setright=setright,
                                    rightafter=rightafter)
        items.append(bugmeta)
        
       