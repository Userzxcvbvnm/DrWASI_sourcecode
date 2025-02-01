import re
import sys
sys.path.append("../preliminary_classification/bugmeta")
from bugmeta_fd_write import BugMetaFD_WRITE

DIR = "./deduplicateresult"
        
def add_msg(msg_set, msg):
    if msg in msg_set:
        for eachmsg in msg_set:
            if msg == eachmsg:
                eachmsg.problemdir.append(msg.problemdir)
    else:
        msg.problemdir = [msg.problemdir]
        msg_set.add(msg) 
        
def deduplicate_fd_write(filename, version="None"):
    print(f"Dedusplicating FD_WRITE_result ...")
    outputfile = f"{DIR}/FD_WRITE_final.txt"
    if version == "new":
        outputfile = f"{DIR}/new_version/FD_WRITE_final.txt"
    elif version == "old":
        outputfile = f"{DIR}/old_version/FD_WRITE_final.txt"     
    
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
        

        file2per = ""
        pattern = r"\[File2per\]:(.*)"
        match = re.search(pattern, record)
        if match:
            file2per = match.group(1)
            filename = file2per.split("->")[0]
       
        file2per = "file2per"
        
        
        file2openstyle = ""
        pattern = r"\[File2openstyle\]:(.*)"
        match = re.search(pattern, record)
        if match:
            file2openstyle = match.group(1)
        
        file2openstyle = "file2openstyle"
       
        
        
        filesizebefore = ""
        pattern = r"\[File size before\]:(.*)"
        match = re.search(pattern, record)
        if match:
            sizebefore = match.group(1)  
        

        filesizeafter = ""
        pattern = r"\[File size after\]:(.*)"
        match = re.search(pattern, record)
        if match:
            sizeafter = match.group(1)    
       
 
        writebytesexpected = ""
        pattern = r"\[Write bytes expected\]:(.*)"
        match = re.search(pattern, record)
        if match:
            writebytesexpected = match.group(1)  
       
 
        writebytesreal = ""
        pattern = r"\[Write bytes real\]:(.*)"
        match = re.search(pattern, record)
        if match:
            writebytesreal = match.group(1)   
       
 
        sizeexpected = ""
        pattern = r"\[File size expected\]:(.*)"
        match = re.search(pattern, record)
        if match:
            sizeexpected = match.group(1)
       
 
        offsetbefore = ""
        pattern = r"\[Offset before\]:(.*)"
        match = re.search(pattern, record)
        if match:
            offsetbefore = match.group(1)
       
        offsetafter = ""
        pattern = r"\[Offset after\]:(.*)"
        match = re.search(pattern, record)
        if match:
            offsetafter = match.group(1)
        
        
        offsetafterexpected = ""  
        pattern = r"\[Offset after expected\]:(.*)"
        match = re.search(pattern, record)
        if match:
            offsetafterexpected = match.group(1)
  
        sizeexpectednew = ""
        sizebeforenew = ""
        sizeafternew = ""
        writebytesexpectednew = ""
        writebytesrealnew = ""
        offsetbeforenew = ""
        offsetafternew = "" 
        offsetafterexpected = ""  
           
        if writebytesexpected > writebytesreal:
            writebytesexpectednew = "writebytesexpected(writebytesexpected > writebytesreal)"
            writebytesrealnew = "writebytesreal"
        elif writebytesexpected == writebytesreal:
            writebytesexpectednew = "writebytesexpected(writebytesexpected == writebytesreal)"
            writebytesrealnew = "writebytesread"
        elif writebytesexpected < writebytesreal:
            writebytesexpectednew = "writebytesexpected(writebytesexpected < writebytesreal)"
            writebytesrealnew = "writebytesexpected"
                
        if sizeexpected > sizeafter:
            sizeexpectednew = "sizeexpect(sizeexpect > sizeafter)"
            sizeafternew = "sizeafter"
        elif sizeexpected == sizeafter:
            sizeexpectednew = "sizeexpect(sizeexpect == sizeafter)"
            sizeafternew = "sizeafter"
        elif sizeexpected < sizeafter:
            sizeexpectednew = "sizeexpect(sizeexpect < sizeafter)"
            sizeafternew = "sizeafter"
                
        if offsetbefore > offsetafter:
            offsetbeforenew = "offsetbefore(offsetbefore > offsetafter)"
        elif offsetbefore == offsetafter:
            offsetbeforenew = "offsetbefore(offsetbefore== offsetafter)"
        if offsetbefore < offsetafter:
            offsetbeforenew = "offsetbefore(offsetbefore < offsetafter)" 

        sizeexpectednew = ""
        sizebeforenew = ""
        sizeafternew = ""
        writebytesexpectednew = ""
        writebytesrealnew = ""
        offsetbeforenew = ""
        
        msg = BugMetaFD_WRITE(runtime=runtime, bugmsg=bugmsg, problemdir=problemdir, 
                                file2per=file2per, file2openstyle=file2openstyle,
                                sizeexpected=sizeexpectednew, sizebefore=sizebeforenew, sizeafter=sizeafternew,
                                writebytesexpected=writebytesexpectednew, writebytesreal=writebytesrealnew,
                                offsetbefore=offsetbeforenew, offsetafter=offsetafternew,
                                offsetafterexpected=offsetafterexpected)
        add_msg(msg_set, msg) 

       
    print(f"After deduplicating, there are {len(msg_set)} items.")
         
         
    newcontent = ""
    for msg in msg_set:
        newcontent = f"{newcontent}--------------------------------------------------\n\
{msg.get()}\
--------------------------------------------------\n\n\n"

    with open(outputfile, 'w') as file:
        file.write(newcontent)
    
    
    