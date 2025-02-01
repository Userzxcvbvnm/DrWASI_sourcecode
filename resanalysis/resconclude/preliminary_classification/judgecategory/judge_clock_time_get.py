import sys
import re
sys.path.append("./bugmeta")
from bugmeta_clock_time_get import BugMetaClock_TIME_GET

def judge_clock_time_get(items, runtime, logcontent, problemdir):
    print("Judging clock_time_get bug ...")
    
    CLOCK_PATTERN = 'Current time: 0 seconds'
    match = re.search(CLOCK_PATTERN, logcontent)
    if match:
        bugmeta = BugMetaClock_TIME_GET(runtime=runtime, bugmsg=match.group(0), problemdir=problemdir)
        items.append(bugmeta)


   