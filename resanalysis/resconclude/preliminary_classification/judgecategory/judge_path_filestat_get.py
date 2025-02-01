import re
import sys
sys.path.append("./bugmeta")
from bugmeta_path_filestat_get import BugMetaPATH_FILESTAT_GET

def judge_path_filestat_get(items, runtime, logcontent, problemdir):
    print("Judging path_filestat_get bug ...")

    bugmsg = ""
    
    pattern = r'Enter function path_filestat_get_.*\nError getting file status.'
    match = re.search(pattern, logcontent)
    if match:
        bugmsg = "Error getting file status."
        
    if bugmsg != "":
        bugmeta = BugMetaPATH_FILESTAT_GET(runtime=runtime, bugmsg=bugmsg, problemdir=problemdir)
        items.append(bugmeta)
       
