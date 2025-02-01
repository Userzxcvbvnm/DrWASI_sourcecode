from bugmeta import BugMeta

class BugMetaFD_DATASYNC(BugMeta):
    def __init__(self, runtime, bugmsg, problemdir, 
                 item="FD_DATASYNC"):
        self.item = item
        self.runtime = runtime
        self.bugmsg = bugmsg 
        
        self.problemdir = problemdir
        
    def print(self):
        super().print()
        
    def get(self):
        return super().get()
    
    
    def __eq__(self, other):
        return super().__eq__(other)

    def __hash__(self):
        return super().__hash__()
