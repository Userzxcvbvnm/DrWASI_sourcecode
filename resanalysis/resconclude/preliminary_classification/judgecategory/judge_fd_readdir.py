import re
import sys
sys.path.append("./bugmeta")
from bugmeta_fd_readdir import BugMetaFD_READDIR

def judge_fd_readdir(items, file2per, runtime, ccontent, snapshotbefore, logcontent, problemdir):
    print("Judging fd_readdir bug ...")

    bugmsg = ""
    filename = ""
    openstyle = ""
    per = file2per.split("->")[1]
    readcontent = []
    realcontent = [".", ".."]
    
    print(f"per:{per}")
    pattern = r'get_fd\("(.*?)", (.*?)\);'
    match = re.search(pattern, ccontent)
    if match:
        filename = match.group(1)
        openstyle = match.group(2)
    print(f"filename:{filename}")
    print(f"openstyle:{openstyle}") 
        
    pattern = f"Get file descriptor of file {filename} failed!"
    if pattern in logcontent:
        return
    
    if "fdopendir failed." in logcontent:
        bugmsg = "fdopendir failed."
        bugmeta = BugMetaFD_READDIR(runtime=runtime, bugmsg=bugmsg, problemdir=problemdir, 
                                    openstyle=openstyle, per=per, readcontent=readcontent, realcontent=realcontent)
        items.append(bugmeta)
        return     
    
    
    readstr = ""
    pattern = r'Enter function fd_readdir_.*?\n(.*?)\nPrint dir content finished\.'
    match = re.search(pattern, logcontent, re.DOTALL)
    if match:
        readstr = match.group(1)
        readstrs = readstr.split("\n")
        for str in readstrs:
            readcontent.append(str[len("Get dir content:"):])
    print(f"readcontent:{readcontent}")
            
    if len(readcontent) == 0:
        readstr = ""
        pattern = r'Enter function fd_readdir_.*?(fdopendir failed\.)'
        match = re.search(pattern, logcontent, re.DOTALL)
        if match:
            readstr = match.group(1)
            readcontent.append(readstr)
            bugmsg = readstr

    
    pattern = rf"Dir: '{filename}/(.*)'\n"
    matches = re.findall(pattern, snapshotbefore)
    for match in matches:
        length = len(match.split("/"))
        if length > 1:
            continue
        realcontent.append(match)
    print(f"realcontent:{realcontent}")
    
    pattern = rf"Normal file: '{filename}/(.*?)'\s*\nFile size:"
    matches = re.findall(pattern, snapshotbefore)
    for match in matches:
        length = len(match.split("/"))
        if length > 1:
            continue
        realcontent.append(match)
    
   
    
    if len(readcontent) != len(realcontent):
        if bugmsg == "":
            bugmsg = "Read dir content differ from real."
        bugmeta = BugMetaFD_READDIR(runtime=runtime, bugmsg=bugmsg, problemdir=problemdir, 
                                    openstyle=openstyle, per=per, readcontent=readcontent, realcontent=realcontent)
        items.append(bugmeta)
    else:
        for c1 in readcontent:
            if c1 not in realcontent:
                if bugmsg == "":
                    bugmsg = "Read dir content differ from real."
                bugmeta = BugMetaFD_READDIR(runtime=runtime, bugmsg=bugmsg, problemdir=problemdir, 
                                    openstyle=openstyle, per=per, readcontent=readcontent, realcontent=realcontent)
                items.append(bugmeta)



        