import re
import sys
sys.path.append("../preliminary_classification/bugmeta")
from bugmeta_fd_allocate import BugMetaFD_ALLOCATE

DIR = "./deduplicateresult"
   
def add_msg(msg_set, msg):
    if msg in msg_set:
        for eachmsg in msg_set:
            if msg == eachmsg:
                eachmsg.problemdir.append(msg.problemdir)
    else:
        msg.problemdir = [msg.problemdir]
        msg_set.add(msg)     

def deduplicate_fd_allocate(filename, version = "None"):
    print(f"Deduplicating FD_ALLOCATE_result ...")
    outputfile = f"{DIR}/FD_ALLOCATE_final.txt"
    if version == "new":
        outputfile = f"{DIR}/new_version/FD_ALLOCATE_final.txt"
    elif version == "old":
        outputfile = f"{DIR}/old_version/FD_ALLOCATE_final.txt"
    
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
        
        sizebefore = -1
        sizeafter = -1
        readsizebefore = -1
        readsizeafter = -1
        startvalue = -1
        allocatelen = -1
        pattern = re.compile(
            r'\[Allocate start value\]:(\d+)\n'
            r'\[Allocate length\]:(\d+)\n'
            r'\[Size before allocate\]:(\d+)\n'
            r'\[Size after allocate\]:(\d+)\n'
            r'\[Size read before allocate\]:(\d+)\n'
            r'\[Size read after allocate\]:(\d+)\n',
            re.MULTILINE
        )
        match = re.search(pattern, record)
        if match:
            startvalue = int(match.group(1))
            allocatelen = int(match.group(2))
            sizebefore = int(match.group(3))
            sizeafter = int(match.group(4))
            readsizebefore = int(match.group(5))
            readsizeafter = int(match.group(6))
            
        # pattern 0 
        if "Read size before != Real size before"==bugmsg:
            msg = BugMetaFD_ALLOCATE(runtime=runtime, bugmsg=bugmsg, 
                                 startvalue="STARTVALUE", allocatelen="ALLOCATELEN",
                                 sizebefore="SIZEBEFORE", sizeafter="SIZEAFTER",
                                 readsizebefore="READ_SIZEBEFORE(!=SIZEBEFORE)", readsizeafter="READ_SIZEAFTER",
                                 problemdir=problemdir)
            add_msg(msg_set, msg)
            
        if  "Read size after != Real size after"==bugmsg:
            msg = BugMetaFD_ALLOCATE(runtime=runtime, bugmsg=bugmsg, 
                                 startvalue="STARTVALUE", allocatelen="ALLOCATELEN",
                                 sizebefore="SIZEBEFORE", sizeafter="SIZEAFTER",
                                 readsizebefore="READ_SIZEBEFORE", readsizeafter="READ_SIZEAFTER(!=SIZEAFTER)",
                                 problemdir=problemdir)
        
            add_msg(msg_set, msg)           
            
        # bug pattern 1
        if "Startvalue + lenvalue < filesize, the file is not trunced, however, print allocation succeed."==bugmsg:
            msg = BugMetaFD_ALLOCATE(runtime=runtime, bugmsg=bugmsg, 
                                 startvalue="STARTVALUE", allocatelen="ALLOCATELEN",
                                 sizebefore="SIZEBEFORE(startvalue+len < size)", sizeafter="SIZEAFTER",
                                 readsizebefore="READ_SIZEBEFORE", readsizeafter="READ_SIZEAFTER",
                                 problemdir=problemdir)
        
            add_msg(msg_set, msg)
        # end bug pattern 1
        
        # bug pattern 2
        if "Startvalue + lenvalue < filesize, the file is trunced, which is not expected."==bugmsg:
            msg = BugMetaFD_ALLOCATE(runtime=runtime, bugmsg=bugmsg, 
                                 startvalue="STARTVALUE", allocatelen="ALLOCATELEN",
                                 sizebefore="SIZEBEFORE(startvalue+len<size)", sizeafter="SIZEAFTER",
                                 readsizebefore="READ_SIZEBEFORE", readsizeafter="READ_SIZEAFTER",
                                 problemdir=problemdir)
        
            add_msg(msg_set, msg)
        # end bug pattern 2
        
        
        
        # bug pattern 3
        if "Startvalue + lenvalue > filesize, the file is not extended, which is not expected." in bugmsg:
            msg = BugMetaFD_ALLOCATE(runtime=runtime, bugmsg=bugmsg, 
                                 startvalue="STARTVALUE", allocatelen="ALLOCATELEN",
                                 sizebefore="SIZEBEFORE(startvalue+len>size)", sizeafter="SIZEAFTER",
                                 readsizebefore="READ_SIZEBEFORE", readsizeafter="READ_SIZEAFTER",
                                 problemdir=problemdir)
        
            add_msg(msg_set, msg)
        # end bug pattern 3
        
        
        # bug pattern 4
        if "Startvalue + lenvalue > filesize, but without O_RDWR or O_WRONLY, the file is extended, which is not expected." in bugmsg:
            msg = BugMetaFD_ALLOCATE(runtime=runtime, bugmsg=bugmsg, 
                                 startvalue="STARTVALUE", allocatelen="ALLOCATELEN",
                                 sizebefore="SIZEBEFORE(startvalue+len>size)", sizeafter="SIZEAFTER",
                                 readsizebefore="READ_SIZEBEFORE", readsizeafter="READ_SIZEAFTER",
                                 problemdir=problemdir)
        
            add_msg(msg_set, msg)
        # end bug pattern 4
        
        
        
    print(f"After deduplicating, there are {len(msg_set)} items.")
         
    newcontent = ""
    for msg in msg_set:
        newcontent = f"{newcontent}--------------------------------------------------\n\
{msg.get()}\
--------------------------------------------------\n\n\n"

    with open(outputfile, 'w') as file:
        file.write(newcontent)
    
    
    

    
