import sys
sys.path.append("./bugmeta")
sys.path.append("../../../executor/envbuild/permission")
from permission import LinuxDirPer 
import re 
from bugmeta_path_open import BugMetaPATH_OPEN

def judge_path_open(items, runtime, file2per, ccontent, logcontent, platform, problemdir):
    print("Judging path_open bug ...")
    
    
    file2openstyle = ""
    pattern = re.compile(r'int file_fd = openat\(fd, "(.*?)",(.*?)\);', re.DOTALL)
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
            
            
            openjudgeflag = False
            if res:
                pattern = r'Open file or directory failed:\s*(.*)'
                match = re.search(pattern, logcontent)

                if match:
                    openjudgeflag = True
                    bugmeta = BugMetaPATH_OPEN(runtime=runtime, bugmsg=f"Should open, but not. Open file or directory failed: {match.group(1)}", 
                                               file2perstr=f"{filename}->{per}", file2openstyle=f"{filename}->{openstyle}",
                                               problemdir=problemdir)
                    items.append(bugmeta)
            else: 
                pattern = f'Open file or directory succeeded!'
                match = re.search(pattern, logcontent)
                if match:
                    openjudgeflag = True
                    bugmeta = BugMetaPATH_OPEN(runtime=runtime, bugmsg=f"Should not open, but open. Open file or directory succeeded!", 
                                               file2perstr=f"{filename}->{per}", file2openstyle=f"{filename}->{openstyle}",
                                               problemdir=problemdir)
                    items.append(bugmeta)
                   
            
            if openjudgeflag == False and "Open file or directory failed: No such file or directory" in logcontent:
                bugmeta = BugMetaPATH_OPEN(runtime=runtime, bugmsg="Fail message error. Open file or directory failed: No such file or directory", 
                                               file2perstr=f"{filename}->{per}", file2openstyle=f"{filename}->{openstyle}",
                                               problemdir=problemdir)
                items.append(bugmeta)
       
