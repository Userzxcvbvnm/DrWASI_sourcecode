import re
import sys
sys.path.append("../preliminary_classification/bugmeta")
from bugmeta_fd_renumber import BugMetaFD_RENUMBER

DIR = "./deduplicateresult"

def add_msg(msg_set, msg):
    if msg in msg_set:
        for eachmsg in msg_set:
            if msg == eachmsg:
                eachmsg.problemdir.append(msg.problemdir)
    else:
        msg.problemdir = [msg.problemdir]
        msg_set.add(msg)      

def deduplicate_fd_renumber(filename, version="None"):
    print(f"Deduplicating FD_RENUMBER_result ...")
    outputfile = f"{DIR}/FD_RENUMBER_final.txt"
    if version == "new":
        outputfile = f"{DIR}/new_version/FD_RENUMBER_final.txt"
    elif version == "old":
        outputfile = f"{DIR}/old_version/FD_RENUMBER_final.txt"  
         
    
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
            
        
        filename1 = ""
        pattern = r"\[Filename1\]:(.*?)\n"
        match = re.search(pattern, record)
        if match:
            filename1 = match.group(1)
        filename1 = "FILENAME1"
            
        filename2 = ""
        pattern = r"\[Filename2\]:(.*?)\n"
        match = re.search(pattern, record)
        if match:
            filename2 = match.group(1)  
        filename2 = "FILENAME2" 
            
        fileper = ""
        pattern = r"\[Fileper\]:(.*?)\n"
        match = re.search(pattern, record)
        if match:
            fileper = match.group(1)  
        fileper = "FILEPER"
 
        file1openstyle = ""
        pattern = r"\[File1openstyle\]:(.*?)\n"
        match = re.search(pattern, record)
        if match:
            file1openstyle = match.group(1) 
        file1openstyle = "FILE1OPENSTYLE"  

        file2openstyle = ""
        pattern = r"\[File2openstyle\]:(.*?)\n"
        match = re.search(pattern, record)
        if match:
            file2openstyle = match.group(1) 
        file2openstyle = "FILE2OPENSTYLE"             
          
        
        msg = BugMetaFD_RENUMBER(runtime=runtime, bugmsg=bugmsg, problemdir=problemdir, 
                                fileper=fileper, 
                                filename1=filename1, filename2=filename2,
                                file1openstyle=file1openstyle, file2openstyle=file2openstyle)
        add_msg(msg_set, msg)
        
    print(f"After deduplicating, there are {len(msg_set)} items.")
         
         
    newcontent = ""
    for msg in msg_set:
        newcontent = f"{newcontent}--------------------------------------------------\n\
{msg.get()}\
--------------------------------------------------\n\n\n"

    with open(outputfile, 'w') as file:
        file.write(newcontent)
    
    
    