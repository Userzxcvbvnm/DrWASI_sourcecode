import re
import sys
sys.path.append("../preliminary_classification/bugmeta")
from bugmeta_open import BugMetaOpen

DIR = "./deduplicateresult"

def add_msg(msg_set, msg):
    if msg in msg_set:
        for eachmsg in msg_set:
            if msg == eachmsg:
                eachmsg.problemdir.append(msg.problemdir)
    else:
        msg.problemdir = [msg.problemdir]
        msg_set.add(msg) 
        

def deduplicate_open(filename, version="None"):
    print(f"Deduplicating OPEN_result ...")
    outputfile = f"{DIR}/OPEN_final.txt"
    if version == "new":
        outputfile = f"{DIR}/new_version/OPEN_final.txt"
    elif version == "old":
        outputfile = f"{DIR}/old_version/OPEN_final.txt"
    
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
        pattern = r"\[Bug message\]:Get file descriptor of file (.*?) (failed|succeed)!"
        match = re.search(pattern, record)
        if match:
            operfile = match.group(1)
            shortname = ""
            if "/" in operfile:
                tmplist = operfile.split("//")
                shortname = tmplist[-1]
            else:
                shortname = operfile
            if "file" in shortname:
                record = record.replace(operfile, "FILENAME")
            elif "dir" in shortname:
                record = record.replace(operfile, "DIRNAME")
            
        pattern = r"\[Bug message\]:(.*?)\n"
        match = re.search(pattern, record)
        if match:
            msg = match.group(1)
            
        pattern = r"\[Changed permission file\]:(.*)"
        match = re.search(pattern, record)
        if match:
            fileandper = match.group(1)
        
        pattern = r"\[Open file\]:(.*)"
        match = re.search(pattern, record)
        if match:
            fileandopen = match.group(1)
            
        pattern = r"\[Problem dir\]:(.*)"
        match = re.search(pattern, record)
        if match:
            problemdir = match.group(1)
            
        msg = BugMetaOpen(runtime=runtime, bugmsg=msg, file2perstr=fileandper, file2openstyle=fileandopen, problemdir=problemdir)
        
        add_msg(msg_set, msg)
        
    print(f"After deduplicating, there are {len(msg_set)} items.")
         
    newcontent = ""
    for msg in msg_set:
        newcontent = f"{newcontent}--------------------------------------------------\n\
{msg.get()}\
--------------------------------------------------\n\n\n"
        
    with open(outputfile, 'w') as file:
        file.write(newcontent)
    
    
    

    
