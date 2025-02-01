import re
import sys
sys.path.append("./bugmeta")
from bugmeta_fd_fdstat_set_flags import BugMetaFD_FDSTAT_SET_FLAGS


def judge_open_print(open_style, access_mode):
    if  "O_RDONLY" in open_style and "Read Only" not in access_mode:
        return False, "O_RDONLY do not access"
    if  "O_WRONLY" in open_style and "Write Only" not in access_mode:
        return False, "O_WRONLY do not access"
    if  "O_RDWR" in open_style and "Read/Write" not in access_mode:
        return False, "O_RDWR do not access"
    return True, ""


def judge_set_print(open_style, set_flags, access_mode):
    set_items = set()
    opens = open_style.split(" | ")
    for o in opens:
        set_items.add(o)
        
    set_items.add(set_flags)
    print(f"set_items:{set_items}")
    
    
    access_items = set()
    for str in access_mode:
        if str == "Read Only":
            access_items.add("O_RDONLY")
        elif str == "Write Only":
            access_items.add("O_WRONLY")
        elif str == "Read/Write":
            access_items.add("O_RDWR")
        elif str == "O_APPEND":
            access_items.add("O_APPEND")
        elif str == "Non-blocking":
            access_items.add("O_NONBLOCK")
        
    print(f"access_items:{access_items}")
     
    flag = True
    bugmsg = ""
    if  "O_RDONLY" in set_items and "O_RDONLY" not in access_items:
        flag = False
        bugmsg = "O_RDONLY do not access"
    if  "O_WRONLY" in set_items and "O_WRONLY" not in access_items:
        flag = False
        bugmsg = "O_WRONLY do not access"
    if  "O_RDWR" in set_items and "O_RDWR" not in access_items:
        flag = False
        bugmsg = "O_RDWR do not access"
        
        
    if "O_APPEND" in set_items and ("O_WRONLY" in set_items or "O_RDWR" in set_items) and "O_APPEND" not in access_items:
        flag = False
        bugmsg = "O_APPEND do not access"

    if "O_ASYNC" in set_items and ("O_WRONLY" in set_items or "O_RDWR" in set_items) and "O_ASYNC" not in access_items:
        flag = False
        bugmsg = "O_ASYNC do not access"

    if "O_DIRECT" in set_items and ("O_WRONLY" in set_items or "O_RDWR" in set_items) and "O_DIRECT" not in access_items:
        flag = False
        bugmsg = "O_DIRECT do not access"   
    
    if "O_NOATIME" in set_items and "O_NOATIME" not in access_items:
        flag = False
        bugmsg = "O_NOATIME do not access"   
    
    return flag, bugmsg 
        
        

def judge_fd_fdstat_set_flags(items, runtime, ccontent, logcontent, problemdir):
    print("Judging fd_fdstat_set_flags bug ...")
            
    openstyle = ""
    pattern = r'get_fd\("([^"]+)",\s*([^)]*)\);'
    match = re.search(pattern, ccontent)
    if match:
        openstyle = match.group(2)
    print(f"openstyle:{openstyle}")
    

    access_modes1 = ""
    pattern = r'((?:Access mode: (.*?)\n)*?)Enter function fd_fdstat_set_flags_.*?\n'
    match = re.search(pattern, logcontent)
    if match:
        access_modes_block1 = match.group(1)  
        access_modes1 = re.findall(r'Access mode: (.*?)\n', access_modes_block1)  
   
    
    setflags = ""
    pattern = r'flags = flags \| (.*);'
    match = re.search(pattern, ccontent)
    if match:
        setflags = match.group(1)
   
        
    access_modes2 = ""
    matches = re.findall(r'After setting flags[\s\S]*?(Access mode: .+)', logcontent)
    if matches:
        after_flags_text = re.search(r'After setting flags[\s\S]*', logcontent).group(0)
        access_modes2 = re.findall(r'Access mode: (.+)', after_flags_text)
   
    
    
    if "Setting flags failed!" in logcontent:
        bugmeta = BugMetaFD_FDSTAT_SET_FLAGS(runtime=runtime, bugmsg="Setting flags failed!", problemdir=problemdir, 
                                    openflags=openstyle, getflagsbefore=access_modes1,
                                    setflags=setflags, getflagsafter=access_modes2)
        items.append(bugmeta)
        return     
      
    
    printbefore = True
    printafter = True
    bugmsg = ""
    if openstyle != "" and len(access_modes1) > 0:
        printbefore, bugmsg = judge_open_print(openstyle, access_modes1)
    if printbefore == False and bugmsg != "":
        bugmeta = BugMetaFD_FDSTAT_SET_FLAGS(runtime=runtime, bugmsg=bugmsg, problemdir=problemdir, 
                                    openflags=openstyle, getflagsbefore=access_modes1,
                                    setflags=setflags, getflagsafter=access_modes2)
        items.append(bugmeta)
        
    if openstyle != "" and setflags != "" and len(access_modes2) > 0:
        printafter, bugmsg= judge_set_print(openstyle, setflags, access_modes2)
    if printafter == False and bugmsg != "":
        bugmeta = BugMetaFD_FDSTAT_SET_FLAGS(runtime=runtime, bugmsg=bugmsg, problemdir=problemdir, 
                                    openflags=openstyle, getflagsbefore=access_modes1,
                                    setflags=setflags, getflagsafter=access_modes2)
        items.append(bugmeta)

        
       