import re
import sys
sys.path.append("./bugmeta")
from bugmeta_path_link import BugMetaPATH_LINK

def judge_path_link(items, runtime, logcontent, snapshotafter, problemdir):
    print("Judging path_link bug ...")

    bugmsg = ""
        
    pattern = r"Normal file: 'Data/HARDLINKFILE'"
    match = re.search(pattern, snapshotafter)
    if match:
        pass
    else:
        bugmsg = "HARDLINKFILE do not exist"
        
    pattern = r'Enter function path_link_.*\s*linkat failed'
    match = re.search(pattern, logcontent)
    if match:
        bugmsg = "linkat failed"
        
    if bugmsg != "":
        bugmeta = BugMetaPATH_LINK(runtime=runtime, bugmsg=bugmsg, problemdir=problemdir)
        items.append(bugmeta)
       
