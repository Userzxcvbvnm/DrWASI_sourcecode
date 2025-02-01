import re
import sys
sys.path.append("./bugmeta")
from bugmeta_path_symlink import BugMetaPATH_SYMLINK

def judge_path_symlink(items, runtime, ccontent, snapshotafter, logcontent, problemdir):
    print("Judging path_symlink bug ...")

    bugmsg = ""
    
    if "Softlink file: 'Data/NEWFILE'" in snapshotafter:
        pass
    else:
        bugmsg = "Fail to create link, although print succcess."
        
    if bugmsg != "":
        bugmeta = BugMetaPATH_SYMLINK(runtime=runtime, bugmsg=bugmsg, problemdir=problemdir)
        items.append(bugmeta)
       