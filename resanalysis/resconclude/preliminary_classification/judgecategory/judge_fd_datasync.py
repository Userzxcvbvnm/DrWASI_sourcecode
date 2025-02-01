import sys
import re
sys.path.append("./bugmeta")
from bugmeta_fd_datasync import BugMetaFD_DATASYNC

def judge_fd_datasyc(items, runtime, logcontent, problemdir):
    print("Judging fd_datasyc bug ...")
    
    pattern = 'Enter function fd_datasync_.*?\nFailed to synchronize data to disk'
    match = re.search(pattern, logcontent)
    if match:
        bugmeta = BugMetaFD_DATASYNC(runtime=runtime, bugmsg=match.group(0), problemdir=problemdir)
        items.append(bugmeta)


   