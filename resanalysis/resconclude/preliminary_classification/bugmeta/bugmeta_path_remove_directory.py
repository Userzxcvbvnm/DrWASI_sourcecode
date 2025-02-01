from bugmeta import BugMeta

class BugMetaPATH_REMOVE_DIRECTORY(BugMeta):
    def __init__(self, runtime, bugmsg, problemdir,
                 file2openstyle,
                 item="PATH_REMOVE_DIRECTORY"):
        self.item = item
        self.runtime = runtime
        self.bugmsg = bugmsg 

        self.file2openstyle = file2openstyle
        
        self.problemdir = problemdir
        
    