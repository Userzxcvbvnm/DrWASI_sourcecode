from bugmeta import BugMeta

class BugMetaClock_TIME_GET(BugMeta):
    def __init__(self, runtime, bugmsg, problemdir, item="CLOCK_TIME_GET"):
        self.item = item
        self.runtime = runtime
        self.bugmsg = bugmsg 
        self.problemdir = problemdir
        
    def print(self):
        super().print()
    
    def get(self):
        return super().get()