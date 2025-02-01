import re
import sys
sys.path.append("./bugmeta")
from bugmeta_trunc import BugMetaTRUNC

def judge_trunc(items, file2per, runtime, snapshotbefore, snapshotafter, logcontent, ccontent, problemdir):
    print("Judging trunc bug ...")
    
    filename = ""
    sourcefile = ""
    openstyle = ""
    per = ""
    filesizebefore = ""
    filesizeafter = ""
        
    pattern = re.compile(r'int fd = get_fd\("(.*?)", (.*?)\);')
    match = re.search(pattern, ccontent)
    if match:
        filename = match.group(1)
        sourcefile = filename
        openstyle = match.group(2)  

    pername = file2per.split("->")[0]
    if file2per.split("->"):
        per = file2per.split("->")[1]
    
    
    if filename.startswith("hardfile") or filename.startswith("softfile"):
        pattern = re.compile(rf"""(Soft|Hard)link file: '{filename}' -> '(.*?)'""")
        match = re.search(pattern, snapshotbefore)
        if match:
            sourcefile = match.group(2) 
        
    pattern = re.compile(rf"""Normal file: '{sourcefile}'\s*File size: '(\d+)'""")
    match = re.search(pattern, snapshotbefore)
    print(f"pattern:{pattern}")
    print(f"snapshotbefore:{snapshotbefore}")
    if match:
        filesizebefore = int(match.group(1)) 
        
    pattern = re.compile(rf"""Normal file: 'Data/{sourcefile}'\s*File size: '(\d+)'""")
    match = re.search(pattern, snapshotafter)
    if match:
        filesizeafter = int(match.group(1)) 
    
    getfdsuccess = f"Get file descriptor of file {filename} succeed!"
    if getfdsuccess in logcontent and "O_TRUNC" in openstyle and isinstance(filesizeafter, int) and filesizeafter != 0:
        bugmeta = BugMetaTRUNC(runtime=runtime, bugmsg="Open with trunc, however, the file is not trunced.", problemdir=problemdir, 
                                     filename=filename, per=per, openstyle=openstyle,
                                     filesizebefore=filesizebefore, filesizeafter=filesizeafter)
        items.append(bugmeta)
        
        