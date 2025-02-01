import re
import sys
sys.path.append("../preliminary_classification/bugmeta")
from bugmeta_path_filestat_set_times import BugMetaPATH_FILESTAT_SET_TIMES

DIR = "./deduplicateresult"
        
def add_msg(msg_set, msg):
    if msg in msg_set:
        for eachmsg in msg_set:
            if msg == eachmsg:
                eachmsg.problemdir.append(msg.problemdir)
    else:
        msg.problemdir = [msg.problemdir]
        msg_set.add(msg) 
        
        
def deduplicate_path_filestat_set_times(filename, version="None"):
    print(f"Dedusplicating PATH_FILESTAT_SET_TIMES_result ...")
    outputfile = f"{DIR}/PATH_FILESTAT_SET_TIMES_final.txt"
    if version == "new":
        outputfile = f"{DIR}/new_version/PATH_FILESTAT_SET_TIMES_final.txt"
    elif version == "old":
        outputfile = f"{DIR}/old_version/PATH_FILESTAT_SET_TIMES_final.txt"     
    
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
        #print(f"\n\n\n\n\nruntime:{runtime}")
            
        problemdir = "default"
        pattern = r"\[Problem dir\]:(.*)"
        match = re.search(pattern, record)
        if match:
            problemdir = match.group(1)
        #print(f"problemdir:{problemdir}")
        
        
        bugmsg = ""
        pattern = r"\[Bug message\]:(.*?)\n"
        match = re.search(pattern, record)
        if match:
            bugmsg = match.group(1)
        #print(f"bugmsg:{bugmsg}") 
        
        setatime = ""
        pattern = r"\[Set access time\]:(.*?)\n"
        match = re.search(pattern, record)
        if match:
            setatime = match.group(1)
        #print(f"setatime:{setatime}") 
        setatime = "setatime"
        
        
        setmtime = ""
        pattern = r"\[Set modification time\]:(.*?)\n"
        match = re.search(pattern, record)
        if match:
            setmtime = match.group(1)
        #print(f"setmtime:{setmtime}") 
        setmtime = "setmtime"        
 
 
        printatime = ""
        pattern = r"\[Last access time\]:(.*?)\n"
        match = re.search(pattern, record)
        if match:
            printatime = match.group(1)
        #print(f"printatime:{printatime}") 
        printatime = "printatime"  
        
        printmtime = ""
        pattern = r"\[Last modification time\]:(.*?)\n"
        match = re.search(pattern, record)
        if match:
            printmtime = match.group(1)
        #print(f"printmtime:{printmtime}")  
        printmtime = "printmtime"      
  
        msg = BugMetaPATH_FILESTAT_SET_TIMES(runtime=runtime, bugmsg=bugmsg, problemdir=problemdir,
                                             setatime=setatime, setmtime=setmtime,
                                             printatime=printatime, printmtime=printmtime)
        add_msg(msg_set, msg)
        
        
    print(f"After deduplicating, there are {len(msg_set)} items.")
         
         
    newcontent = ""
    for msg in msg_set:
        newcontent = f"{newcontent}--------------------------------------------------\n\
{msg.get()}\
--------------------------------------------------\n\n\n"

    with open(outputfile, 'w') as file:
        file.write(newcontent)
    
    
    