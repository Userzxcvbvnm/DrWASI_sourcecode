import re
import sys
sys.path.append("./bugmeta")
from bugmeta_fd_pwrite import BugMetaFD_PWRITE

def judge_fd_pwrite(items, runtime, ccontent, snapshotbefore, snapshotafter, logcontent, problemdir):
    print("Judging fd_pwrite bug ...")

    offset = ""
    writesize = ""
    filesizebefore = ""
    filesizebeforetrunc = ""
    filesizeafter = ""
    readfilesizebefore = ""
    readfilesizeafter = ""
    filename = ""
    sourcefile = ""
    openstyle = ""
    
    pattern = r'get_fd\("(.*?)", (.*?)\);'
    match = re.search(pattern, ccontent)
    if match:
        filename = match.group(1) 
        openstyle = match.group(2)
        sourcefile = filename
    
    if filename.startswith("hard") or filename.startswith("soft"):
        pattern = rf"(Hard|Soft)link file: '{filename}' -> '(.*?)'"
        match = re.search(pattern, snapshotbefore)
        if match:
            sourcefile = match.group(2)    
    
    
    pattern = rf"Normal file: '{sourcefile}'\s*File size: '(\d+)'\s*File content:"
    match = re.search(pattern, snapshotbefore)
    if match:
        filesizebefore = int(match.group(1)) 
    if "O_TRUNC" in openstyle:
        filesizebeforetrunc = filesizebefore
        print(f"测试位置1 filesizebeforetrunc:{filesizebeforetrunc}")
        filesizebefore = 0
        
    pattern = rf"Normal file: 'Data/{sourcefile}'\s*File size: '(\d+)'\s*File content:"
    match = re.search(pattern, snapshotafter)
    if match:
        filesizeafter = int(match.group(1))
        
    pattern = r'ssize_t bytes_written = pwritev\(fd, iov, 1, (\d+)\);'
    match = re.search(pattern, ccontent)
    if match:
        offset = int(match.group(1))
  
    pattern = r'iov\[0\].iov_len = (\d+);'
    match = re.search(pattern, ccontent)
    if match:
        writesize = int(match.group(1))
          
    pattern = r'Current file size before: (\d+)'
    match = re.search(pattern, logcontent)
    if match:
        readfilesizebefore = int(match.group(1)) 
        
    pattern = r'Current file size after: (\d+)'
    match = re.search(pattern, logcontent)
    if match:
        readfilesizeafter = int(match.group(1))  

        
    if isinstance(readfilesizebefore, int) and isinstance(filesizebefore, int) and readfilesizebefore != filesizebefore:
        bugmeta = BugMetaFD_PWRITE(runtime=runtime, bugmsg="readfilesizebefore != filesizebefore", problemdir=problemdir, 
                                    offset=offset, writesize=writesize, 
                                    filesizebefore=filesizebefore, filesizeafter=filesizeafter,
                                    readfilesizebefore=readfilesizebefore, readfilesizeafter=readfilesizeafter)
        items.append(bugmeta)
    
    if isinstance(readfilesizeafter, int) and isinstance(filesizeafter, int) and readfilesizeafter != filesizeafter:
        bugmeta = BugMetaFD_PWRITE(runtime=runtime, bugmsg="readfilesizeafter != filesizeafter", problemdir=problemdir, 
                                    offset=offset, writesize=writesize, 
                                    filesizebefore=filesizebefore, filesizeafter=filesizeafter,
                                    readfilesizebefore=readfilesizebefore, readfilesizeafter=readfilesizeafter)
        items.append(bugmeta)
        
    
    
    if ("O_WRONLY" in openstyle or "O_RDWR" in openstyle) and isinstance(offset, int) and isinstance(writesize, int) and isinstance(filesizebefore, int) and isinstance(filesizeafter, int) and isinstance(readfilesizebefore, int) and isinstance(readfilesizeafter, int):
        if (offset + writesize) > filesizebefore and writesize > 0 and filesizeafter <= filesizebefore:
            bugmeta = BugMetaFD_PWRITE(runtime=runtime, bugmsg="(offset + writesize) > filesizebefore(writesize > 0), however, filesize not extend.", problemdir=problemdir, 
                                    offset=offset, writesize=writesize, 
                                    filesizebefore=filesizebefore, filesizeafter=filesizeafter,
                                    readfilesizebefore=readfilesizebefore, readfilesizeafter=readfilesizeafter)
            items.append(bugmeta)
        elif (offset + writesize) > filesizebefore and writesize == 0 and filesizeafter != filesizebefore:
            if isinstance(filesizebeforetrunc, int) and runtime == "wasmer":
                if filesizeafter != filesizebeforetrunc:
                    bugmeta = BugMetaFD_PWRITE(runtime=runtime, bugmsg="(offset + writesize) > filesizebefore(writesize == 0), however, filesize changed.", problemdir=problemdir, 
                                    offset=offset, writesize=writesize, 
                                    filesizebefore=filesizebefore, filesizeafter=filesizeafter,
                                    readfilesizebefore=readfilesizebefore, readfilesizeafter=readfilesizeafter)
                    items.append(bugmeta)
            else:
                bugmeta = BugMetaFD_PWRITE(runtime=runtime, bugmsg="(offset + writesize) > filesizebefore(writesize == 0), however, filesize changed.", problemdir=problemdir, 
                                    offset=offset, writesize=writesize, 
                                    filesizebefore=filesizebefore, filesizeafter=filesizeafter,
                                    readfilesizebefore=readfilesizebefore, readfilesizeafter=readfilesizeafter)
                items.append(bugmeta)
        elif (offset + writesize) == filesizebefore and filesizebefore != filesizeafter:
            if isinstance(filesizebeforetrunc, int) and runtime == "wasmer":
                if filesizeafter != filesizebeforetrunc:
                    bugmeta = BugMetaFD_PWRITE(runtime=runtime, bugmsg="(offset + writesize) == filesizebefore, however, filesize changed.", problemdir=problemdir, 
                                    offset=offset, writesize=writesize, 
                                    filesizebefore=filesizebefore, filesizeafter=filesizeafter,
                                    readfilesizebefore=readfilesizebefore, readfilesizeafter=readfilesizeafter)
                    items.append(bugmeta)
            else:
                bugmeta = BugMetaFD_PWRITE(runtime=runtime, bugmsg="(offset + writesize) == filesizebefore, however, filesize changed.", problemdir=problemdir, 
                                    offset=offset, writesize=writesize, 
                                    filesizebefore=filesizebefore, filesizeafter=filesizeafter,
                                    readfilesizebefore=readfilesizebefore, readfilesizeafter=readfilesizeafter)
                items.append(bugmeta)

        elif (offset + writesize) < filesizebefore and ("O_APPEND" not in openstyle) and filesizeafter != filesizebefore:
            bugmeta = BugMetaFD_PWRITE(runtime=runtime, bugmsg="(offset + writesize) < filesizebefore (no O_APPEND), however, filesize changed.", problemdir=problemdir, 
                                    offset=offset, writesize=writesize, 
                                    filesizebefore=filesizebefore, filesizeafter=filesizeafter,
                                    readfilesizebefore=readfilesizebefore, readfilesizeafter=readfilesizeafter)           
            items.append(bugmeta)
        elif (offset + writesize) < filesizebefore and ("O_APPEND" in openstyle) and writesize > 0 and filesizeafter == filesizebefore:
            bugmeta = BugMetaFD_PWRITE(runtime=runtime, bugmsg="(offset + writesize) < filesizebefore (has O_APPEND), however, filesize not extend.", problemdir=problemdir, 
                                    offset=offset, writesize=writesize, 
                                    filesizebefore=filesizebefore, filesizeafter=filesizeafter,
                                    readfilesizebefore=readfilesizebefore, readfilesizeafter=readfilesizeafter)           
            items.append(bugmeta)
    elif "O_WRONLY" not in openstyle and "O_RDWR" not in openstyle and "pwritev successful." in logcontent:
        bugmeta = BugMetaFD_PWRITE(runtime=runtime, bugmsg="Not open with O_WRONLY or O_RDWR, however, pwrite succeed.", problemdir=problemdir, 
                                    offset=offset, writesize=writesize, 
                                    filesizebefore=filesizebefore, filesizeafter=filesizeafter,
                                    readfilesizebefore=readfilesizebefore, readfilesizeafter=readfilesizeafter)           
        items.append(bugmeta)