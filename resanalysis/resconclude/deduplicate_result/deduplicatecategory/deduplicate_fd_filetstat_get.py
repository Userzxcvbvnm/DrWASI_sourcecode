import re
import sys
sys.path.append("../preliminary_classification/bugmeta")
from bugmeta_fd_filestat_get import BugMetaFD_FILESTAT_GET

DIR = "./deduplicateresult"
        
def add_msg(msg_set, msg):
    if msg in msg_set:
        for eachmsg in msg_set:
            if msg == eachmsg:
                eachmsg.problemdir.append(msg.problemdir)
    else:
        msg.problemdir = [msg.problemdir]
        msg_set.add(msg)  
        
        
def deduplicate_fd_filestat_get(filename, version="None"):
    print(f"Deduplicating FD_FILESTAT_GET_result ...")
    outputfile = f"{DIR}/FD_FILESTAT_GET_final.txt"
    if version == "new":
        outputfile = f"{DIR}/new_version/FD_FILESTAT_GET_final.txt"
    elif version == "old":
        outputfile = f"{DIR}/old_version/FD_FILESTAT_GET_final.txt"  
    
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
        pattern = r"\[Filename\]:(.*)\n"
        match = re.search(pattern, record)
        if match:
            filename = match.group(1)

        filename = "FILE"
              

        realhardlinknum = ""
        pattern = r"\[Real hard link num\]:(\d+)"
        match = re.search(pattern, record)
        if match:
            realhardlinknum = int(match.group(1))
            
        printhardlinknum = ""
        pattern = r"\[Print hard link num\]:(\d+)"
        match = re.search(pattern, record)
        if match:
            printhardlinknum = int(match.group(1))
            
        if realhardlinknum < printhardlinknum:
            realhardlinknum = "REAL hardlink num (< printhardlink num)"
            printhardlinknum = "printhardlink num"
        elif realhardlinknum > printhardlinknum:
            realhardlinknum = "REAL hardlink num (> printhardlink num)"
            printhardlinknum = "printhardlink num"
            
        msg = BugMetaFD_FILESTAT_GET(runtime=runtime, bugmsg=bugmsg, problemdir=problemdir, 
                                    filename=filename,
                                    realhardlinknum=realhardlinknum,
                                    printhardlinknum=printhardlinknum)
        
        add_msg(msg_set, msg)
       
        
    print(f"After deduplicating, there are {len(msg_set)} items.")
         
    newcontent = ""
    for msg in msg_set:
        newcontent = f"{newcontent}--------------------------------------------------\n\
{msg.get()}\
--------------------------------------------------\n\n\n"

    with open(outputfile, 'w') as file:
        file.write(newcontent)
    
    
    