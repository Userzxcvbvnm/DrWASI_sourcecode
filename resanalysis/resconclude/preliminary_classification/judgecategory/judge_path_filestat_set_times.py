import re
import sys
sys.path.append("./bugmeta")
from bugmeta_path_filestat_set_times import BugMetaPATH_FILESTAT_SET_TIMES


def judge_path_filestat_set_times(items, runtime, logcontent, ccontent, problemdir):
    print("Judging path_filestat_set_times bug ...")

    bugmsg = ""
    
    printatime = ""
    printmtime = ""
    setatime = ""
    setmtime = ""
    
    pattern = r'Last access time: (.*)\n'
    match = re.search(pattern, logcontent)
    if match:
        printatime = match.group(1)
    print(f"printatime:{printatime}")
        
    pattern = r'Last modification time: (.*)'
    match = re.search(pattern, logcontent)
    if match:
        printmtime = match.group(1)
    print(f"printmtime:{printmtime}")
        
    pattern = r'struct timespec times\[2\] = {{(.*), 0}, {(.*), 0}};'
    match = re.search(pattern, ccontent)
    if match:
        setatime = match.group(1)
        setmtime = match.group(2)
    print(f"setatime:{setatime}")
    print(f"setmtime:{setmtime}")
        
    if printatime != "" and setatime != "" and printatime != setatime:
        bugmeta = BugMetaPATH_FILESTAT_SET_TIMES(runtime=runtime, bugmsg="printatime != setatime", problemdir=problemdir,
                                   printatime=printatime, printmtime=printmtime,
                                   setatime=setatime, setmtime=setmtime)
        items.append(bugmeta)
       
    if printmtime != "" and setmtime != "" and printmtime != setmtime:
        bugmeta = BugMetaPATH_FILESTAT_SET_TIMES(runtime=runtime, bugmsg="printmtime != setmtime", problemdir=problemdir,
                                   printatime=printatime, printmtime=printmtime,
                                   setatime=setatime, setmtime=setmtime)
        items.append(bugmeta)
        