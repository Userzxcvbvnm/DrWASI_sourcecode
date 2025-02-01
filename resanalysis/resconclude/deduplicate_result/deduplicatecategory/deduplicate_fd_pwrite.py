import re
import sys
sys.path.append("../preliminary_classification/bugmeta")
from bugmeta_fd_pwrite import BugMetaFD_PWRITE

DIR = "./deduplicateresult"

def add_msg(msg_set, msg):
    if msg in msg_set:
        for eachmsg in msg_set:
            if msg == eachmsg:
                eachmsg.problemdir.append(msg.problemdir)
    else:
        msg.problemdir = [msg.problemdir]
        msg_set.add(msg)  
             

def deduplicate_fd_pwrite(filename, version="None"):
    print(f"Deduplicating FD_PWRITE_result ...")
    outputfile = f"{DIR}/FD_PWRITE_final.txt"
    if version == "new":
        outputfile = f"{DIR}/new_version/FD_PWRITE_final.txt"
    elif version == "old":
        outputfile = f"{DIR}/old_version/FD_PWRITE_final.txt"    
    
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
        pattern = r"\[Bug message\]:(.*)\n"
        match = re.search(pattern, record)
        if match:
            bugmsg = match.group(1) 
           
        filesizebefore = ""
        pattern = r"\[Filesizebefore\]:(.*)"
        match = re.search(pattern, record)
        if match:
            filesizebefore = int(match.group(1))
        
        filesizeafter = ""
        pattern = r"\[Filesizeafter\]:(.*)"
        match = re.search(pattern, record)
        if match:
            filesizeafter = int(match.group(1))
            
        offset = ""
        pattern = r"\[Offset\]:(.*)"
        match = re.search(pattern, record)
        if match:
            offset = int(match.group(1))
        
        writesize = ""
        pattern = r"\[Writesize\]:(.*)"
        match = re.search(pattern, record)
        if match:
            writesize = int(match.group(1))
        
        readfilesizebefore = ""
        pattern = r"\[Readfilesizebefore\]:(.*)"
        match = re.search(pattern, record)
        if match:
            readfilesizebefore = int(match.group(1))
            
        readfilesizeafter = ""
        pattern = r"\[Readfilesizeafter\]:(.*)"
        match = re.search(pattern, record)
        if match:
            readfilesizeafter = int(match.group(1))
            
        if bugmsg == "readfilesizeafter != filesizeafter" or bugmsg == "readfilesizebefore != filesizebefore":
            msg = BugMetaFD_PWRITE(runtime=runtime, bugmsg="readfilesizebefore != filesizebefore or readfilesizeafter != filesizeafter", problemdir=problemdir, 
                                    offset="OFFSET", writesize="WRITESIZE", 
                                    filesizebefore="FILESIZEBEFORE", filesizeafter="FILESIZEAFTER(!=READFILESIZEAFTER)",
                                    readfilesizebefore="READFILESIZEBEFORE", readfilesizeafter="READFILESIZEAFTER")
            add_msg(msg_set, msg)
        else:      
            msg = BugMetaFD_PWRITE(runtime=runtime, bugmsg=bugmsg, problemdir=problemdir, 
                                    offset="OFFSET", writesize="WRITESIZE", 
                                    filesizebefore="FILESIZEBEFORE", filesizeafter="FILESIZEAFTER",
                                    readfilesizebefore="READFILESIZEBEFORE", readfilesizeafter="READFILESIZEAFTER")
            add_msg(msg_set, msg)
        
        
    print(f"After deduplicating, there are {len(msg_set)} items.")
         
    newcontent = ""
    for msg in msg_set:
        newcontent = f"{newcontent}--------------------------------------------------\n\
{msg.get()}\
--------------------------------------------------\n\n\n"

    with open(outputfile, 'w') as file:
        file.write(newcontent)
    
    
    