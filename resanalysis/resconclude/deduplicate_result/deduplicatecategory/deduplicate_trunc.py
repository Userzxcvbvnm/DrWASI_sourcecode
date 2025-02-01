import re
import sys
sys.path.append("../preliminary_classification/bugmeta")
from bugmeta_trunc import BugMetaTRUNC

DIR = "./deduplicateresult"
        

def deduplicate_trunc(filename, version="None"):
    print(f"Deduplicating TRUNC_result ...")
    outputfile = f"{DIR}/TRUNC_final.txt"
    if version == "new":
        outputfile = f"{DIR}/new_version/TRUNC_final.txt"
    elif version == "old":
        outputfile = f"{DIR}/old_version/TRUNC_final.txt"
    
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
        pattern = r"\[Bug message\]:(.*)"
        match = re.search(pattern, record)
        if match:
            bugmsg = match.group(1)
        
        filename = "default"
        pattern = r"\[Filename\]:(.*)"
        match = re.search(pattern, record)
        if match:
            filename = match.group(1)
        filename = "FILENAME"
  
        per= "default"
        pattern = r"\[Per\]:(.*)"
        match = re.search(pattern, record)
        if match:
            per = match.group(1) 
        per = "per" 
            
  
        openstyle= "default"
        pattern = r"\[Openstyle\]:(.*)"
        match = re.search(pattern, record)
        if match:
            openstyle = match.group(1) 
        openstyle = "Contains O_TRUNC" 

   
        filesizebefore= "default"
        pattern = r"\[File size before\]:(.*)"
        match = re.search(pattern, record)
        if match:
            filesizebefore = int(match.group(1))
        filesizebefore = "FILESIZEBEFORE"   
 
        filesizeafter= "default"
        pattern = r"\[File size after\]:(.*)"
        match = re.search(pattern, record)
        if match:
            filesizeafter = int(match.group(1))
            if filesizeafter > 0:
                filesizeafter = "FILESIZEAFTER > 0"
            else:
                print("!!!FILESIZEAFTER error!!!")
            
            
        msg = BugMetaTRUNC(runtime=runtime, bugmsg=bugmsg, 
                                 filename=filename, per=per, openstyle=openstyle,
                                 filesizebefore=filesizebefore, filesizeafter=filesizeafter,
                                 problemdir=problemdir)
        
        if msg in msg_set:
            for eachmsg in msg_set:
                if msg == eachmsg:
                    eachmsg.problemdir.append(msg.problemdir)
        else:
            msg.problemdir = [msg.problemdir]
            msg_set.add(msg)

    print(f"After deduplicating, there are {len(msg_set)} items.")
         
    newcontent = ""
    for msg in msg_set:
        newcontent = f"{newcontent}--------------------------------------------------\n\
{msg.get()}\
--------------------------------------------------\n\n\n"

    with open(outputfile, 'w') as file:
        file.write(newcontent)