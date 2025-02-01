import re
import sys
sys.path.append("../preliminary_classification/bugmeta")
from bugmeta_fd_datasync import BugMetaFD_DATASYNC

DIR = "./deduplicateresult"
       
def add_msg(msg_set, msg):
    if msg in msg_set:
        for eachmsg in msg_set:
            if msg == eachmsg:
                eachmsg.problemdir.append(msg.problemdir)
    else:
        msg.problemdir = [msg.problemdir]
        msg_set.add(msg)     
 

def deduplicate_fd_datasync(filename, version="None"):
    print(f"Deduplicating FD_DATASYNC_result ...")
    outputfile = f"{DIR}/FD_DATASYNC_final.txt"
    if version == "new":
        outputfile = f"{DIR}/new_version/FD_DATASYNC_final.txt"
    elif version == "old":
        outputfile = f"{DIR}/old_version/FD_DATASYNC_final.txt"
    
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
        
        bugmsg = "default"
        pattern = r"\[Bug message\]:Enter function fd_datasync_(.*?)\nFailed to synchronize data to disk"
        match = re.search(pattern, record)
        if match:
            bugmsg = f"Enter function fd_datasync_xxxxx.\nFailed to synchronize data to disk"
            
        msg = BugMetaFD_DATASYNC(runtime=runtime, bugmsg=bugmsg, 
                                 problemdir=problemdir)
        
        add_msg(msg_set, msg)
        
    print(f"After deduplicating, there are {len(msg_set)} items.")
         
    newcontent = ""
    for msg in msg_set:
        newcontent = f"{newcontent}--------------------------------------------------\n\
{msg.get()}\
--------------------------------------------------\n\n\n"

    with open(outputfile, 'w') as file:
        file.write(newcontent)
    
    
    