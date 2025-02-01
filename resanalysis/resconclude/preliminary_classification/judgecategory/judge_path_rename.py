import re
import sys
sys.path.append("./bugmeta")
from bugmeta_path_rename import BugMetaPATH_RENAME

def judge_path_rename(items, runtime, ccontent, logcontent, problemdir):
    print("Judging path_rename bug ...")

    bugmsg = ""
    file2openstyle = ""
    
    
    pattern = r'Enter function path_rename_.*\nError renaming file or directory.'
    match = re.search(pattern, logcontent)
    if match:
        bugmsg = "Fail to rename."
        

        
    if bugmsg != "":
        bugmeta = BugMetaPATH_RENAME(runtime=runtime, bugmsg=bugmsg, problemdir=problemdir)
        items.append(bugmeta)
       
