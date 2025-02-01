import re
import sys
sys.path.append("./bugmeta")
from bugmeta_fd_filestat_get import BugMetaFD_FILESTAT_GET

def judge_fd_filestat_get(items, runtime, ccontent, logcontent, snapshotbefore, problemdir):
    print("Judging fd_filestat_get bug ...")
       
    bugmsg = ""   
    filename = ""
    realhardlinknum = ""
    printhardlinknum = ""
    
    
    pattern = r'get_fd\("(.*?)", (.*?)\);'
    match = re.search(pattern, ccontent)
    if match:
        filename = match.group(1)

    pattern = r'Number of hard links to the file: (\d+)'
    match = re.search(pattern, logcontent)
    if match:
        printhardlinknum = match.group(1)
    
    sourcefile = filename
    pattern = rf"(Hard|Soft)link file: '{filename}' -> '(.*?)'"
    match = re.search(pattern, snapshotbefore)
    if match:
        sourcefile = match.group(2)

            
    pattern = rf"Hardlink file: '.*' -> {sourcefile}"
    matches = re.findall(pattern, snapshotbefore)
    realhardlinknum = len(matches)
    
    
    if printhardlinknum != "" and realhardlinknum != printhardlinknum:
        bugmeta = BugMetaFD_FILESTAT_GET(runtime=runtime, bugmsg="Hard link number error", problemdir=problemdir, 
                                    filename=filename, realhardlinknum=realhardlinknum,
                                    printhardlinknum=printhardlinknum)
        items.append(bugmeta)
        