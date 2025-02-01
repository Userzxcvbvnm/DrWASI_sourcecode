import re
import sys
sys.path.append("../preliminary_classification/bugmeta")
from bugmeta_fd_readdir import BugMetaFD_READDIR

DIR = "./deduplicateresult"

def add_msg(msg_set, msg):
    if msg in msg_set:
        for eachmsg in msg_set:
            if msg == eachmsg:
                eachmsg.problemdir.append(msg.problemdir)
    else:
        msg.problemdir = [msg.problemdir]
        msg_set.add(msg)
        

def deduplicate_fd_readdir(filename, version="None"):
    print(f"Deduplicating FD_READDIR_result ...")
    outputfile = f"{DIR}/FD_READDIR_final.txt"
    if version == "new":
        outputfile = f"{DIR}/new_version/FD_READDIR_final.txt"
    elif version == "old":
        outputfile = f"{DIR}/old_version/FD_READDIR_final.txt"    
         
    
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
           
           
        openstyle = ""
        per = ""
        realcontent = ""
        readcontent = ""
        
        pattern = r"\[Openstyle\]:(.*)"
        match = re.search(pattern, record)
        if match:
            openstyle = match.group(1)
        
        
        pattern = r"\[Per\]:(.*)"
        match = re.search(pattern, record)
        if match:
            per = match.group(1)
            
        pattern = r"\[Readcontent\]:(.*)"
        match = re.search(pattern, record)
        if match:
            readcontent = match.group(1)


        pattern = r"\[Realcontent\]:(.*)"
        match = re.search(pattern, record)
        if match:
            realcontent = match.group(1)
        realcontent = "realcontent"
        
            
        msg = BugMetaFD_READDIR(runtime=runtime, bugmsg=bugmsg, problemdir=problemdir, 
                                    openstyle=openstyle, per=per, readcontent=readcontent, realcontent=realcontent)
        add_msg(msg_set, msg)
        
    print(f"After deduplicating, there are {len(msg_set)} items.")
         
         
    newcontent = ""
    for msg in msg_set:
        newcontent = f"{newcontent}--------------------------------------------------\n\
{msg.get()}\
--------------------------------------------------\n\n\n"

    with open(outputfile, 'w') as file:
        file.write(newcontent)
    
    
    