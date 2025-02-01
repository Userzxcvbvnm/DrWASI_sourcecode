import re
import sys
sys.path.append("./bugmeta")
from bugmeta_fd_pread import BugMetaFD_PREAD

def judge_fd_pread(items, runtime, ccontent, logcontent, problemdir):
    print("Judging fd_pread bug ...")
