import re
import sys
sys.path.append("../preliminary_classification/bugmeta")
from bugmeta_path_readlink import BugMetaPATH_READLINK

DIR = "./deduplicateresult"
        
        
def add_msg(msg_set, msg):
    if msg in msg_set:
        for eachmsg in msg_set:
            if msg == eachmsg:
                eachmsg.problemdir.append(msg.problemdir)
    else:
        msg.problemdir = [msg.problemdir]
        msg_set.add(msg) 
        

def deduplicate_path_readlink(filename, version="None"):
    print(f"Dedusplicating PATH_READLINK_result ...")
    outputfile = f"{DIR}/PATH_READLINK_final.txt"
    if version == "new":
        outputfile = f"{DIR}/new_version/PATH_READLINK_final.txt"
    elif version == "old":
        outputfile = f"{DIR}/old_version/PATH_READLINK_final.txt"   
    
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
        print(f"\n\n\n\n\nruntime:{runtime}")
            
        problemdir = "default"
        pattern = r"\[Problem dir\]:(.*)"
        match = re.search(pattern, record)
        if match:
            problemdir = match.group(1)
        print(f"problemdir:{problemdir}")
        
        
        bugmsg = ""
        pattern = r"\[Bug message\]:(.*?)\n"
        match = re.search(pattern, record)
        if match:
            bugmsg = match.group(1)
        print(f"bugmsg:{bugmsg}") 
       
        msg = BugMetaPATH_READLINK(runtime=runtime, bugmsg=bugmsg, problemdir=problemdir)
        add_msg(msg_set, msg)
        
    print(f"After deduplicating, there are {len(msg_set)} items.")
         
         
    newcontent = ""
    for msg in msg_set:
        newcontent = f"{newcontent}--------------------------------------------------\n\
{msg.get()}\
--------------------------------------------------\n\n\n"

    with open(outputfile, 'w') as file:
        file.write(newcontent)
    
    
    