import re
import sys
sys.path.append("../preliminary_classification/bugmeta")
from bugmeta_path_open import BugMetaPATH_OPEN

DIR = "./deduplicateresult"
        

def add_msg(msg_set, msg):
    if msg in msg_set:
        for eachmsg in msg_set:
            if msg == eachmsg:
                eachmsg.problemdir.append(msg.problemdir)
    else:
        msg.problemdir = [msg.problemdir]
        msg_set.add(msg) 
        
        
def deduplicate_path_open(filename, version="None"):
    print(f"Dedusplicating PATH_OPEN_result ...")
    outputfile = f"{DIR}/PATH_OPEN_final.txt"
    if version == "new":
        outputfile = f"{DIR}/new_version/PATH_OPEN_final.txt"
    elif version == "old":
        outputfile = f"{DIR}/old_version/PATH_OPEN_final.txt"  
    
    
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
        print(f"problemdir:{problemdir}")
        
        
        bugmsg = ""
        pattern = r"\[Bug message\]:(.*?)\n"
        match = re.search(pattern, record)
        if match:
            bugmsg = match.group(1)
        print(f"bugmsg:{bugmsg}") 
        
      


        filename = ""
        file2per = ""
        pattern = r"\[File2per\]:(.*?)\n"
        match = re.search(pattern, record)
        if match:
            file2per = match.group(1)
            filename = file2per.split("->")[0]
        print(f"filename:{filename}")
         
        
        file2openstyle = ""
        pattern = r"\[File2openstyle\]:(.*?)\n"
        match = re.search(pattern, record)
        if match:
            file2openstyle = match.group(1)
        
        
        
        shortname = ""
        if "/" in filename:
            tmplist = filename.split("//")
            shortname = tmplist[-1]
        else:
            shortname = filename
        print(f"shortname:{shortname}")
        if "file" in shortname:
            file2per = file2per.replace(filename, "FILENAME")
            file2openstyle = file2openstyle.replace(filename, "FILENAME")
        elif "dir" in shortname:
            file2per = file2per.replace(filename, "DIRNAME")
            file2openstyle = file2openstyle.replace(filename, "DIRNAME")
        print(f"file2per:{file2per}")
        print(f"file2openstyle:{file2openstyle}")
        
        file2per = "file2per"
        file2openstyle = "file2openstyle"
        msg = BugMetaPATH_OPEN(runtime=runtime, bugmsg=bugmsg, file2perstr=file2per, file2openstyle=file2openstyle, problemdir=problemdir)
        add_msg(msg_set, msg)
        
    print(f"After deduplicating, there are {len(msg_set)} items.")
         
    newcontent = ""
    for msg in msg_set:
        newcontent = f"{newcontent}--------------------------------------------------\n\
{msg.get()}\
--------------------------------------------------\n\n\n"
        
    with open(outputfile, 'w') as file:
        file.write(newcontent)
    
    