from bugmeta import BugMeta

class BugMetaPATH_UNLINK_FILE(BugMeta):
    def __init__(self, runtime, bugmsg, problemdir,
                 item="PATH_UNLINK_FILE"):
        self.item = item
        self.runtime = runtime
        self.bugmsg = bugmsg 

        
        self.problemdir = problemdir
        
    def print(self):
        print(self.get())
        
    def get(self):
        mes = f"[Runtime]:{self.runtime} -> [Bug item]:{self.item}\n[Bug message]:{self.bugmsg}\n"
        
        
        if isinstance(self.problemdir, str):
            mes = f"{mes}[Problem dir]:{self.problemdir}\n"
        elif isinstance(self.problemdir, list):
            mes = f"{mes}[Problem dir]:{self.problemdir[0]}\n"
            for i in range(1, len(self.problemdir)):
                mes = f"{mes}              {self.problemdir[i]}\n"
        return mes
    
    
    def __eq__(self, other):
        if not isinstance(other, BugMetaPATH_UNLINK_FILE):
            return NotImplemented
        return (self.runtime == other.runtime and
                self.item == other.item and
                self.bugmsg == other.bugmsg)
        

    def __hash__(self):
        return hash((self.runtime, self.item, self.bugmsg))
