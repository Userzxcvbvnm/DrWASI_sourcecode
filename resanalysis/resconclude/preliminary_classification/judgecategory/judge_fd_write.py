import re
import sys
sys.path.append("./bugmeta")
from bugmeta_fd_write import BugMetaFD_WRITE

def judge_fd_write(items, file2per, runtime, ccontent, snapshotbefore, snapshotafter, logcontent, problemdir):
    print("Judging fd_write bug ...")

    bugmsg = ""
    sourcefile = ""
    filename = ""
    
    file2openstyle = ""
    sizebefore = ""
    sizeafter = ""
    sizeexpected = ""
    
    writebytesexpected = ""
    writebytesreal = ""
    
    offsetbefore = ""
    offsetafter = ""
    
    offsetafterexpected = ""
    
    
    pattern = rf'Get file descriptor of file (.*?) failed!'
    match = re.search(pattern, logcontent)
    if match:
        return

    pattern = rf'get_fd\("(.*?)", (.*?)\);'
    match = re.search(pattern, ccontent)
    if match:
        filename = match.group(1)
        sourcefile = filename
        file2openstyle = f"{filename} open with {match.group(2)}"
    if filename != file2per.split('->')[0]:
        print("filename != file2per.split('->')[0] 出错")
    print(f"file2per:{file2per}")
    print(f"file2openstyle:{file2openstyle}")
    
    if filename.startswith("hard") or filename.startswith("soft"):
        pattern = rf"(Hard|Soft)link file: '{filename}' -> '(.*?)'"
        match = re.search(pattern, snapshotbefore)
        if match:
            sourcefile = match.group(2)  
    print(f"filename{filename}") 
    print(f"sourcefile:{sourcefile}")   

    pattern = rf'iov\[0\].iov_len = (\d+);\s*iov\[1\].iov_base = ".*";\s*iov\[1\].iov_len = (\d+);'
    match = re.search(pattern, ccontent)
    if match:
        writebytesexpected = int(match.group(1)) + int(match.group(2))
    print(f"writebytesexpected:{writebytesexpected}")
    
    pattern = rf'Write to file descriptor successful. Number of bytes written: (\d+)'
    match = re.search(pattern, logcontent)
    if match:
        writebytesreal = int(match.group(1))
    elif "Write to file descriptor failed!" in logcontent:
        writebytesreal = "Write to file descriptor failed!"
    print(f"writebytesreal:{writebytesreal}")   
       
        
    pattern = rf"Normal file: '{sourcefile}'\s*File size: '(\d+)'"
    match = re.search(pattern, snapshotbefore)
    if match:
        sizebefore = int(match.group(1))
    print(f"sizebefore:{sizebefore}") 
     
    
    pattern = rf"Normal file: 'Data/{sourcefile}'\s*File size: '(\d+)'"
    match = re.search(pattern, snapshotafter)
    if match:
        sizeafter = int(match.group(1))
    print(f"sizeafter:{sizeafter}")  
    
    pattern = r'File current offset before write: (\d+)\n'
    match = re.search(pattern, logcontent)
    if match:
        offsetbefore = int(match.group(1))
    print(f"offsetbefore:{offsetbefore}")  
    
    pattern = r'File current offset after write: (\d+)'
    match = re.search(pattern, logcontent)
    if match:
        offsetafter = int(match.group(1))
    print(f"offsetafter:{offsetafter}") 
    
    if sizebefore > writebytesexpected:
        sizeexpected = sizebefore
    else:
        sizeexpected = writebytesexpected

    offsetafterexpected = ""  
    if isinstance(sizebefore, int) and isinstance(writebytesexpected, int):
        if writebytesexpected > sizebefore:
            sizeexpected = writebytesexpected
            offsetafterexpected = writebytesexpected
        else:
            sizeexpected = sizebefore    
            offsetafterexpected = writebytesexpected
    if "O_APPEND" in file2openstyle:
        sizeexpected = writebytesexpected + sizebefore 
        offsetafterexpected = sizeexpected
    if "O_TRUNC" in file2openstyle:
        sizeexpected = writebytesexpected
        offsetafterexpected = writebytesexpected
    if writebytesexpected == 0:
        offsetafterexpected = 0
    print(f"sizeexpected:{sizeexpected}")
    print(f"offsetafterexpected:{offsetafterexpected}")
      
    
      
    if "Write to file descriptor failed!" in logcontent and "O_RDONLY" in file2openstyle:
        return
    
    if "Write to file descriptor successful." in logcontent and "O_RDONLY" in file2openstyle and writebytesreal > 0:
        bugmsg = "Open with O_RDONLY, but write succeed."
        bugmeta = BugMetaFD_WRITE(runtime=runtime, bugmsg=bugmsg, problemdir=problemdir, 
                                    file2per = file2per, file2openstyle=file2openstyle,
                                    sizeexpected=sizeexpected, sizebefore=sizebefore, sizeafter=sizeafter,
                                    writebytesexpected=writebytesexpected, writebytesreal=writebytesreal,
                                    offsetbefore=offsetbefore, offsetafter=offsetafter,
                                    offsetafterexpected=offsetafterexpected)
        items.append(bugmeta)
        return        
    
    if "Write to file descriptor failed!" in logcontent and ("O_WRONLY" in file2openstyle or "O_RDWR" in file2openstyle):
        bugmsg = "Write to file descriptor failed, although with O_OWRONLY or O_RDWR."
        bugmeta = BugMetaFD_WRITE(runtime=runtime, bugmsg=bugmsg, problemdir=problemdir, 
                                    file2per = file2per, file2openstyle=file2openstyle,
                                    sizeexpected=sizeexpected, sizebefore=sizebefore, sizeafter=sizeafter,
                                    writebytesexpected=writebytesexpected, writebytesreal=writebytesreal,
                                    offsetbefore=offsetbefore, offsetafter=offsetafter,
                                    offsetafterexpected=offsetafterexpected)
        items.append(bugmeta)
        return 
        
        
    if "Write to file descriptor failed!" in logcontent and sizebefore != sizeafter:
        bugmsg = "Fail to write byes, however, file size modified."
        bugmeta = BugMetaFD_WRITE(runtime=runtime, bugmsg=bugmsg, problemdir=problemdir, 
                                    file2per = file2per, file2openstyle=file2openstyle,
                                    sizeexpected=sizeexpected, sizebefore=sizebefore, sizeafter=sizeafter,
                                    writebytesexpected=writebytesexpected, writebytesreal=writebytesreal,
                                    offsetbefore=offsetbefore, offsetafter=offsetafter,
                                    offsetafterexpected=offsetafterexpected)
        items.append(bugmeta)
        return    
      
        
    if writebytesexpected == 0 and writebytesreal ==0 and sizebefore == sizeafter:
        return
    
    
    if ("O_WRONLY" in file2openstyle or "O_RDWR" in file2openstyle) and isinstance(writebytesexpected, int) and isinstance(writebytesreal, int) and writebytesexpected != writebytesreal:
        bugmsg = "writebytesexpected != writebytesreal"
        bugmeta = BugMetaFD_WRITE(runtime=runtime, bugmsg=bugmsg, problemdir=problemdir, 
                                    file2per = file2per, file2openstyle=file2openstyle,
                                    sizeexpected=sizeexpected, sizebefore=sizebefore, sizeafter=sizeafter,
                                    writebytesexpected=writebytesexpected, writebytesreal=writebytesreal,
                                    offsetbefore=offsetbefore, offsetafter=offsetafter,
                                    offsetafterexpected=offsetafterexpected)
        items.append(bugmeta)  
        return      
    
    if ("O_WRONLY" in file2openstyle or "O_RDWR" in file2openstyle) and isinstance(sizeexpected, int) and isinstance(sizeafter, int) and sizeafter != sizeexpected: 
        bugmsg = "File size not equals to the expected."
        if "Write to file descriptor failed!" in logcontent:
            bugmsg = f"{bugmsg}\nWrite to file descriptor failed!"
        bugmeta = BugMetaFD_WRITE(runtime=runtime, bugmsg=bugmsg, problemdir=problemdir, 
                                    file2per = file2per, file2openstyle=file2openstyle,
                                    sizeexpected=sizeexpected, sizebefore=sizebefore, sizeafter=sizeafter,
                                    writebytesexpected=writebytesexpected, writebytesreal=writebytesreal,
                                    offsetbefore=offsetbefore, offsetafter=offsetafter,
                                    offsetafterexpected=offsetafterexpected)
        items.append(bugmeta)
        return

    if isinstance(offsetafterexpected, int) and isinstance(offsetafter, int) and offsetafter != offsetafterexpected:
        bugmsg = "offsetafter != offsetafterexpected"
        bugmeta = BugMetaFD_WRITE(runtime=runtime, bugmsg=bugmsg, problemdir=problemdir, 
                                    file2per = file2per, file2openstyle=file2openstyle,
                                    sizeexpected=sizeexpected, sizebefore=sizebefore, sizeafter=sizeafter,
                                    writebytesexpected=writebytesexpected, writebytesreal=writebytesreal,
                                    offsetbefore=offsetbefore, offsetafter=offsetafter,
                                    offsetafterexpected=offsetafterexpected)
        items.append(bugmeta)
        return 
    
