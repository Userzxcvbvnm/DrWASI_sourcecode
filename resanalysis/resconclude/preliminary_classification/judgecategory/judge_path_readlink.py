import re
import sys
sys.path.append("./bugmeta")
from bugmeta_path_readlink import BugMetaPATH_READLINK

def judge_path_readlink(items, runtime, logcontent, problemdir):
    print("Judging path_readlink bug ...")

    bugmsg = ""
    pattern = r'Enter function path_readlink_.*\nreadlinkat'
    match = re.search(pattern, logcontent)
    if match:
        bugmsg = "Fail to read link."
        
        
    if bugmsg != "":
        bugmeta = BugMetaPATH_READLINK(runtime=runtime, bugmsg=bugmsg, problemdir=problemdir)
        items.append(bugmeta)
       
