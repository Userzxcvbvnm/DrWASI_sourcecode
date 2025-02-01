import sys
sys.path.append("./bugmeta")
sys.path.append("../../../executor/envbuild/permission")
from permission import LinuxDirPer 
import re 
from bugmeta_open import BugMetaOpen


CUR_CATEGORY = "OPEN"
        
def judge_open(items, runtime, file2per, ccontent,  snapshotbefore, logcontent, platform, problemdir):
    print("Judging open bug ...")
    
    
    file2openstyle = ""
    pattern = re.compile(r'get_fd\("(.*?)", (.*?)\);', re.DOTALL)
    matches = pattern.findall(ccontent)
    if len(matches) == 0:
        return
    for match in matches:
        openfile = match[0]
        openstyle = match[1]
        if file2openstyle == "":
            file2openstyle = f"{openfile}->{openstyle}"
        else:
            file2openstyle = f"{file2openstyle}   {openfile}->{openstyle}"

    file2open = file2openstyle.split("   ")
    file2per = file2per.split("   ")
        
    for fileopen in file2open:
        strs = fileopen.split("->")
        filename = strs[0]
        openstyle = strs[1]
        per = "default"
        
        containchange = False
        for fileper in file2per:
            strs2 = fileper.split("->")
            filename2 = strs2[0]
            if filename == filename2:
                containchange = True
                per = strs2[1]
                break
        if containchange == False:
            continue
        
        
        if platform == "Linux":
            if per == "default":
                strs = filename.split("/")
                if "subfile" in strs[-1] or "softfile" in strs[-1] or "hardfile" in strs[-1]:
                    per = "0600"
                elif "subdir" in strs[-1]:
                    per = "0700"
               
            res = LinuxDirPer.judge_openstyle(openstyle, per)
             
            if res:
                pattern = f'Get file descriptor of file {filename} failed!'
                match = re.search(pattern, logcontent)
                if match:
                    bugmeta = BugMetaOpen(runtime=runtime, bugmsg=pattern, 
                                               file2perstr=f"{filename}->{per}", file2openstyle=f"{filename}->{openstyle}",
                                               problemdir=problemdir)
                    items.append(bugmeta)
            else: 
                pattern = f'Get file descriptor of file {filename} succeed!'
                match = re.search(pattern, logcontent)
                if match:
                    bugmeta = BugMetaOpen(runtime=runtime, bugmsg=pattern, 
                                               file2perstr=f"{filename}->{per}", file2openstyle=f"{filename}->{openstyle}",
                                               problemdir=problemdir)
                    items.append(bugmeta)
                    
        
          