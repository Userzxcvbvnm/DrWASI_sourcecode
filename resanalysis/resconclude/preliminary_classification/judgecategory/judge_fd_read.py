import re
import sys
sys.path.append("./bugmeta")
from bugmeta_fd_read import BugMetaFD_READ

def judge_fd_read(items, runtime, ccontent, snapshotafter, snapshotbefore, logcontent, problemdir):
    print("Judging fd_read bug ...")

    filesize = ""
    buffersize = ""
    readsize = ""
    filename = ""
    sourcefile = ""
    
    pattern = r'get_fd\("(.*?)", (.*?)\);'
    match = re.search(pattern, ccontent)
    if match:
        filename = match.group(1) 
        sourcefile = filename
    print(f"filename:{filename}")
        
        
    if filename.startswith("hard") or filename.startswith("soft"):
        pattern = rf"(Hard|Soft)link file: '{filename}' -> '(.*?)'"
        match = re.search(pattern, snapshotbefore)
        if match:
            sourcefile = match.group(2)
    print(f"sourcefile:{sourcefile}")
    
    pattern = rf"Normal file: 'Data/{sourcefile}'\s*File size: '(\d+)'\s*File content:"
    match = re.search(pattern, snapshotafter)
    if match:
        filesize = int(match.group(1))
    print(f"filesize:{filesize}")
    

    pattern = r'Enter function fd_read_(.*?)\s*Read (\d+) bytes using readv'
    match = re.search(pattern, logcontent, re.DOTALL)
    if match:
        readsize = int(match.group(2)) 
    print(f"readsize:{readsize}") 

    buffersize1 = ""
    pattern = r'iov\[0\].iov_len = (\d+);'
    match = re.search(pattern, ccontent)
    if match:
        buffersize1 = int(match.group(1)) 
    print(f"buffersize1:{buffersize1}")
    
    buffersize2 = ""
    pattern = r'iov\[1\].iov_len = (\d+);'
    match = re.search(pattern, ccontent)
    if match:
        buffersize2 = int(match.group(1))
    print(f"buffersize2:{buffersize2}")
    
    if isinstance(buffersize1, int) and isinstance(buffersize2, int):
        buffersize = buffersize1 + buffersize2
    print(f"buffersize:{buffersize}")  
    
        
    if isinstance(filesize, int) and isinstance(buffersize, int) and isinstance(readsize, int):
        if buffersize > filesize and readsize != filesize:
            bugmsg = "buffersize > filesize and readsize != filesize"
            bugmeta = BugMetaFD_READ(runtime=runtime, bugmsg=bugmsg, problemdir=problemdir, 
                                    buffersize=buffersize, filesize=filesize, readsize=readsize)
            items.append(bugmeta)
        if buffersize <= filesize and readsize != buffersize:
            bugmsg = "buffersize <= filesize and readsize != buffersize"
            bugmeta = BugMetaFD_READ(runtime=runtime, bugmsg=bugmsg, problemdir=problemdir, 
                                    buffersize=buffersize, filesize=filesize, readsize=readsize)
            items.append(bugmeta)


        