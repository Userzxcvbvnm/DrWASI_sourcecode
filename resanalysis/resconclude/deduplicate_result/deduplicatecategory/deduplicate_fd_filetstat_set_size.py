import re
import sys
sys.path.append("../preliminary_classification/bugmeta")
from bugmeta_fd_filestat_set_size import BugMetaFD_FILESTAT_SET_SIZE

DIR = "./deduplicateresult"
        
def add_msg(msg_set, msg):
    if msg in msg_set:
        for eachmsg in msg_set:
            if msg == eachmsg:
                eachmsg.problemdir.append(msg.problemdir)
    else:
        msg.problemdir = [msg.problemdir]
        msg_set.add(msg)  
        
        
def deduplicate_fd_filestat_set_size(filename, version="None"):
    print(f"Deduplicating FD_FILESTAT_SET_SIZE_result ...")
    outputfile = f"{DIR}/FD_FILESTAT_SET_SIZE_final.txt"
    if version == "new":
        outputfile = f"{DIR}/new_version/FD_FILESTAT_SET_SIZE_final.txt"
    elif version == "old":
        outputfile = f"{DIR}/old_version/FD_FILESTAT_SET_SIZE_final.txt"  
    
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
  

        sizebefore = ""
        pattern = r"\[Size before\]:(.*?)\n"
        match = re.search(pattern, record)
        if match:
            sizebefore = int(match.group(1))
        sizebefore = "sizebefore"
    
    
        sizeafter = ""
        pattern = r"\[Size after\]:(.*?)\n"
        match = re.search(pattern, record)
        if match:
            sizeafter = int(match.group(1))       
        sizeafter = "sizeafter"
            
        readsizebefore = ""
        pattern = r"\[Read size before\]:(.*?)\n"
        match = re.search(pattern, record)
        if match:
            readsizebefore = int(match.group(1))
        readsizebefore = "readsizebefore"
            
        readsizeafter = ""
        pattern = r"\[Read size after\]:(.*?)\n"
        match = re.search(pattern, record)
        if match:
            readsizeafter = int(match.group(1))  
        readsizeafter = "readsizeafter" 
    
        setsize = ""
        pattern = r"\[Set size\]:(.*?)\n"
        match = re.search(pattern, record)
        if match:
            setsize = int(match.group(1)) 
        setsize = "setsize"   

        openstyle = ""
        pattern = r"\[Openstyle\]:(.*?)\n"
        match = re.search(pattern, record)
        if match:
            openstyle = match.group(1)   
    
            
        msg = BugMetaFD_FILESTAT_SET_SIZE(runtime=runtime, bugmsg=bugmsg, problemdir=problemdir, 
                                    sizebefore=sizebefore, sizeafter=sizeafter,
                                    readsizebefore=readsizebefore, readsizeafter=readsizeafter,
                                    setsize=setsize,
                                    openstyle=openstyle)
        
        add_msg(msg_set, msg)
       
        
    print(f"After deduplicating, there are {len(msg_set)} items.")
         
    newcontent = ""
    for msg in msg_set:
        newcontent = f"{newcontent}--------------------------------------------------\n\
{msg.get()}\
--------------------------------------------------\n\n\n"

    with open(outputfile, 'w') as file:
        file.write(newcontent)
    
    
    