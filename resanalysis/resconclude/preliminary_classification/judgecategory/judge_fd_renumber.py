import re
import sys
sys.path.append("./bugmeta")
from bugmeta_fd_renumber import BugMetaFD_RENUMBER

def judge_fd_renumber(items, file2per, runtime, ccontent, snapshotbefore, logcontent, problemdir):
    print("Judging fd_renumber bug ...")

    bugmsg = ""
    filename1 = ""
    filename2 = ""
    file1openstyle = ""
    file2openstyle = ""
    

    pattern = r'int fd = get_fd\("(.*?)", (.*?)\);'
    match = re.search(pattern, ccontent)
    if match:
        filename1 = match.group(1)
        file1openstyle = match.group(2)
    
    pattern = r'int new_fd = get_fd\("(.*?)", (.*?)\);'
    match = re.search(pattern, ccontent)
    if match:
        filename2 = match.group(1)
        file2openstyle = match.group(2)
    

    
    pattern1 = f"Get file descriptor of file {filename1} failed!"
    pattern2 = f"Get file descriptor of file {filename2} failed!"
    if (pattern1 in logcontent or pattern2 in logcontent) and "Successful file descriptors 0.\nLeave fd_renumber_" in logcontent:
        bugmsg = "Getting file descriptor fails, however, renumber succeed."
        bugmeta = BugMetaFD_RENUMBER(runtime=runtime, bugmsg=bugmsg, problemdir=problemdir, 
                                     filename1=filename1, filename2=filename2,
                                     fileper = file2per, 
                                     file1openstyle=file1openstyle, file2openstyle=file2openstyle)
        items.append(bugmeta)
    
