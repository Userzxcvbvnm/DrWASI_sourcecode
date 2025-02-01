import re
import sys
sys.path.append("./bugmeta")
from bugmeta_path_unlink_file import BugMetaPATH_UNLINK_FILE

def judge_path_unlink_file(items, runtime, ccontent, logcontent, problemdir):
    print("Judging path_unlink_file bug ...")

    bugmsg = ""
    
    pattern = r'Enter function path_unlink_file_.*\nUnlink file failed!'
    match = re.search(pattern, logcontent)
    if match:
        bugmsg = "Unlink file fail"
        
        
    if bugmsg != "":
        bugmeta = BugMetaPATH_UNLINK_FILE(runtime=runtime, bugmsg=bugmsg, problemdir=problemdir)
        items.append(bugmeta)
       
