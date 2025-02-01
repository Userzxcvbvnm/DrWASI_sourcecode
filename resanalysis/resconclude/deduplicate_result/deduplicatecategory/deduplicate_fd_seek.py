import re
import sys
sys.path.append("../preliminary_classification/bugmeta")
from bugmeta_fd_seek import BugMetaFD_SEEK

DIR = "./deduplicateresult"

def add_msg(msg_set, msg):
    if msg in msg_set:
        for eachmsg in msg_set:
            if msg == eachmsg:
                eachmsg.problemdir.append(msg.problemdir)
    else:
        msg.problemdir = [msg.problemdir]
        msg_set.add(msg)      

def deduplicate_fd_seek(filename, version="None"):
    print(f"Deduplicating FD_SEEK_result ...")
    outputfile = f"{DIR}/FD_SEEK_final.txt"
    if version == "new":
        outputfile = f"{DIR}/new_version/FD_SEEK_final.txt"
    elif version == "old":
        outputfile = f"{DIR}/old_version/FD_SEEK_final.txt"  
    
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
            
        
        filename = ""
        pattern = r"\[Filename\]:(.*?)\n"
        match = re.search(pattern, record)
        if match:
            filename = match.group(1)
        filename = "FILENAME"
            
        per = ""
        pattern = r"\[Per\]:(.*?)\n"
        match = re.search(pattern, record)
        if match:
            per = match.group(1)
        per = "PER"    
   
        openstyle = ""
        pattern = r"\[Openstyle\]:(.*?)\n"
        match = re.search(pattern, record)
        if match:
            openstyle = match.group(1)
        openstyle = "Openstyle"               
 
        filesizebefore = ""
        pattern = r"\[Filesizebefore\]:(.*?)\n"
        match = re.search(pattern, record)
        if match:
            filesizebefore = match.group(1)
        filesizebefore = "Filesizebefore"    

        filesizeafter = ""
        pattern = r"\[Filesizeafter\]:(.*?)\n"
        match = re.search(pattern, record)
        if match:
            filesizeafter = match.group(1)
        filesizeafter = "Filesizeafter"           
  
        readoffset = ""
        pattern = r"\[Readoffset\]:(.*?)\n"
        match = re.search(pattern, record)
        if match:
            readoffset = match.group(1)
        
 
        seekpar = ""
        pattern = r"\[Seekpar\]:(.*?)\n"
        match = re.search(pattern, record)
        if match:
            seekpar = match.group(1)  
 
        seeknum = ""
        pattern = r"\[Seeknum\]:(.*?)\n"
        match = re.search(pattern, record)
        if match:
            seeknum = match.group(1)
        seeknum = "Seeknum" 
     
        expectoffset = ""
        pattern = r"\[Expectoffset\]:(.*?)\n"
        match = re.search(pattern, record)
        if match:
            expectoffset = match.group(1)
        
        if readoffset < expectoffset:
            bugmsg = f"The seekpar is {seekpar}. readoffset < expectoffset"
        else:
            bugmsg = f"The seekpar is {seekpar}. readoffset > expectoffset"
        
        readoffset = "Readoffset"  
        expectoffset = "Expectoffset"    
            
        msg = BugMetaFD_SEEK(runtime=runtime, bugmsg=bugmsg, problemdir=problemdir, 
                                filename=filename, per=per, openstyle=openstyle,
                                filesizebefore=filesizebefore, filesizeafter=filesizeafter,
                                readoffset=readoffset, expectoffset=expectoffset,
                                seekpar=seekpar, seeknum=seeknum)
        add_msg(msg_set, msg)
        
    print(f"After deduplicating, there are {len(msg_set)} items.")
         
         
    newcontent = ""
    for msg in msg_set:
        newcontent = f"{newcontent}--------------------------------------------------\n\
{msg.get()}\
--------------------------------------------------\n\n\n"

    with open(outputfile, 'w') as file:
        file.write(newcontent)
    
    
    