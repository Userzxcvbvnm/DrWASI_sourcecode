import re
import sys
sys.path.append("../preliminary_classification/bugmeta")
from bugmeta_fd_fdstat_set_rights import BugMetaFD_FDSTAT_SET_RIGHTS

DIR = "./deduplicateresult"
       
def add_msg(msg_set, msg):
    if msg in msg_set:
        for eachmsg in msg_set:
            if msg == eachmsg:
                eachmsg.setright.add(msg.setright)
                eachmsg.problemdir.append(msg.problemdir)
    else:
        tmpstr = msg.setright
        msg.setright = set()
        msg.setright.add(tmpstr)
        msg.problemdir = [msg.problemdir]
        msg_set.add(msg)  
         

def deduplicate_fd_fdstat_set_rights(filename, version="None"):
    print(f"Deduplicating FD_FDSTAT_SET_RIGHTS_result ...")
    outputfile = f"{DIR}/FD_FDSTAT_SET_RIGHTS_final.txt"
    if version == "new":
        outputfile = f"{DIR}/new_version/FD_FDSTAT_SET_RIGHTS_final.txt"
    elif version == "old":
        outputfile = f"{DIR}/old_version/FD_FDSTAT_SET_RIGHTS_final.txt" 
    
    with open(filename, 'r') as file:
        content = file.read()
                             
    records = content.split('--------------------------------------------------')
    records = [record.strip() for record in records if record.strip()]
    print(f"records len : {len(records)}")
    
    msg_set = set()
    for record in records:
        pattern = r"\[Runtime\]:(.*) ->"
        match = re.search(pattern, record)
        if match:
            runtime = match.group(1)
            
        problemdir = "default"
        pattern = r"\[Problem dir\]:(.*)"
        match = re.search(pattern, record)
        if match:
            problemdir = match.group(1)
        
        bugmsg = ""
        pattern = r"\[Bug message\]:(.*?)\n"
        match = re.search(pattern, record)
        if match:
            bugmsg = match.group(1)
            
        rightbefore = ""
        pattern = r"\[Getrightsbefore\]:\s*([\s\S]*?)(?=\n\[)"
        match = re.search(pattern, record)
        if match:
            rightbefore = match.group(1)
            
            
        setright = ""
        pattern = r"\[Setrights\]:\s*([\s\S]*?)(?=\n\[)"
        match = re.search(pattern, record)
        if match:
            setright = match.group(1).strip()
            
        rightafter = ""
        pattern = r"\[Getrightsafter\]:\s*([\s\S]*?)(?=\n\[)"
        match = re.search(pattern, record)
        if match:
            rightafter = match.group(1).strip()
            
        msg = BugMetaFD_FDSTAT_SET_RIGHTS(runtime=runtime, bugmsg=bugmsg, problemdir=problemdir, 
                                    rightbefore=rightbefore,
                                    setright=setright,
                                    rightafter=rightafter)
        
        add_msg(msg_set, msg)
       
        
    print(f"After deduplicating, there are {len(msg_set)} items.")
         
    newcontent = ""
    for msg in msg_set:
        newcontent = f"{newcontent}--------------------------------------------------\n\
{msg.get()}\
--------------------------------------------------\n\n\n"

    with open(outputfile, 'w') as file:
        file.write(newcontent)
    
    
    