import re
import sys
sys.path.append("./bugmeta")
from bugmeta_fd_allocate import BugMetaFD_ALLOCATE

def judge_fd_allocate(items, runtime, snapshotbefore, snapshotafter, logcontent, ccontent, problemdir):
    print("Judging fd_allocate bug ...")

    
    startvalue = -1
    allocatelen = -1
    pattern = re.compile(r'posix_fallocate\(fd, (.*), (.*)\);')
    match = re.search(pattern, ccontent)
    if match:
        startvalue = int(match.group(1))
        allocatelen = int(match.group(2))
    print(f"startvalue:{startvalue}")
    print(f"allocatelen:{allocatelen}")
        
    readsizebefore = -1
    readsizeafter = -1
    pattern = re.compile(r'Get file size: (\d+) bytes\.\nEnter function fd_allocate_.*?\n.*?\nGet file size: (\d+) bytes\.')
    match = re.search(pattern, logcontent)
    if match:
        readsizebefore = int(match.group(1))
        readsizeafter = int(match.group(2))
    print(f"readsizebefore:{readsizebefore}") 
    print(f"readsizeafter:{readsizeafter}")   
    
       
    # 没有打开文件，直接返回
    if readsizebefore == -1 and readsizeafter == -1:
        return
            
    
    filename = ""  
    openstyle = ""       
    sizebefore = -1
    sizeafter = -1
    pattern = re.compile(r'int fd = get_fd\("(.*?)", (.*?)\);')
    match = re.search(pattern, ccontent)
    if match:
        filename = match.group(1)
        openstyle = match.group(2)
    sourcefile = filename
    print(f"filename:{filename}")
    print(f"openstyle:{openstyle}")
    
    if filename.startswith("hardfile") or filename.startswith("softfile"):
        pattern = re.compile(rf"""(Soft|Hard)link file: '{filename}' -> '(.*?)'""")
        match = re.search(pattern, snapshotbefore)
        if match:
            sourcefile = match.group(2) 
    print(f"sourcefile:{sourcefile}")
        
    pattern = re.compile(rf"""Normal file: '{sourcefile}'\s*File size: '(\d+)'""")
    match = re.search(pattern, snapshotbefore)
    # print(f"pattern:{pattern}")
    # print(f"snapshotbefore:{snapshotbefore}")
    if match:
        sizebefore = int(match.group(1)) 
    print(f"sizebefore:{sizebefore}")
        
    pattern = re.compile(rf"""Normal file: 'Data/{sourcefile}'\s*File size: '(\d+)'""")
    match = re.search(pattern, snapshotafter)
    if match:
        sizeafter = int(match.group(1)) 
    print(f"sizeafter:{sizeafter}")
    
    sizebeforereal = sizebefore
    if readsizebefore < sizebefore:
        sizebeforereal = readsizebefore
    print(f"sizebeforereal:{sizebeforereal}")
       
    # pattern0 
    if sizebefore != readsizebefore and "O_TRUNC" not in openstyle:
        bugmeta = BugMetaFD_ALLOCATE(runtime=runtime, bugmsg="Read size before != Real size before", problemdir=problemdir, 
                                     startvalue=startvalue, allocatelen=allocatelen, 
                                     sizebefore=sizebefore, sizeafter=sizeafter,
                                     readsizebefore=readsizebefore, readsizeafter=readsizeafter)
        items.append(bugmeta)   
        
    if sizeafter != readsizeafter and "O_TRUNC" not in openstyle:
        bugmeta = BugMetaFD_ALLOCATE(runtime=runtime, bugmsg="Read size after != Real size after", problemdir=problemdir, 
                                     startvalue=startvalue, allocatelen=allocatelen, 
                                     sizebefore=sizebefore, sizeafter=sizeafter,
                                     readsizebefore=readsizebefore, readsizeafter=readsizeafter)
        items.append(bugmeta)  
       
       
    # pattern1  
    if sizebeforereal > (startvalue + allocatelen) and "Space allocation in file successful." in logcontent and sizeafter == sizebeforereal:
        bugmeta = BugMetaFD_ALLOCATE(runtime=runtime, bugmsg="Startvalue + lenvalue < filesize, the file is not trunced, however, print allocation succeed.", problemdir=problemdir, 
                                     startvalue=startvalue, allocatelen=allocatelen, 
                                     sizebefore=sizebefore, sizeafter=sizeafter,
                                     readsizebefore=readsizebefore, readsizeafter=readsizeafter)
        items.append(bugmeta)
 
      
        
    # pattern2 
    if (startvalue + allocatelen) < sizebeforereal and (startvalue + allocatelen) == sizeafter:
        bugmeta = BugMetaFD_ALLOCATE(runtime=runtime, bugmsg="Startvalue + lenvalue < filesize, the file is trunced, which is not expected.", problemdir=problemdir, 
                                     startvalue=startvalue, allocatelen=allocatelen, 
                                     sizebefore=sizebefore, sizeafter=sizeafter,
                                     readsizebefore=readsizebefore, readsizeafter=readsizeafter)
        items.append(bugmeta)
        
        
    # pattern3 
    if ("O_WRONLY" in openstyle or "O_RDWR" in openstyle) and (startvalue + allocatelen) > sizebeforereal and sizebeforereal == sizeafter:
        bugmeta = BugMetaFD_ALLOCATE(runtime=runtime, bugmsg="Startvalue + lenvalue > filesize, the file is not extended, which is not expected.", problemdir=problemdir, 
                                     startvalue=startvalue, allocatelen=allocatelen, 
                                     sizebefore=sizebefore, sizeafter=sizeafter,
                                     readsizebefore=readsizebefore, readsizeafter=readsizeafter)
        items.append(bugmeta)
        
    # pattern4 
    if "O_WRONLY" not in openstyle and "O_RDWR" not in openstyle and (startvalue + allocatelen) > sizebeforereal and sizebeforereal < sizeafter:
        bugmeta = BugMetaFD_ALLOCATE(runtime=runtime, bugmsg="Startvalue + lenvalue > filesize, but without O_RDWR or O_WRONLY, the file is extended, which is not expected.", problemdir=problemdir, 
                                     startvalue=startvalue, allocatelen=allocatelen, 
                                     sizebefore=sizebefore, sizeafter=sizeafter,
                                     readsizebefore=readsizebefore, readsizeafter=readsizeafter)
        items.append(bugmeta)
        
        
    

