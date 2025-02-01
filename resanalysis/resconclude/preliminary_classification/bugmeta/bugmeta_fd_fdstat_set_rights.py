from bugmeta import BugMeta

class BugMetaFD_FDSTAT_SET_RIGHTS(BugMeta):
    def __init__(self, runtime, bugmsg, problemdir, 
                 rightbefore, setright, rightafter,
                 item="FD_FDSTAT_SET_RIGHTS"):
        self.item = item
        self.runtime = runtime
        self.bugmsg = bugmsg 
        
        self.rightbefore = rightbefore
        self.setright = setright
        self.rightafter = rightafter
        
        self.problemdir = problemdir
        
    def print(self):
        print(self.get())
        
    def get(self):
        mes = f"[Runtime]:{self.runtime} -> [Bug item]:{self.item}\n[Bug message]:{self.bugmsg}\n"
        
        mes = f"{mes}[Getrightsbefore]:{self.rightbefore}\n"
        if isinstance(self.setright, str):
            mes = f"{mes}[Setrights]:{self.setright}\n"
        elif isinstance(self.setright, set):
            my_list = list(self.setright)
            mes = f"{mes}[Setrights]:{my_list[0]}\n"
            for i in range(1, len(my_list)):
                mes = f"{mes}          | {my_list[i]}\n"
        mes = f"{mes}[Getrightsafter]:{self.rightafter}\n"
            
        if isinstance(self.problemdir, str):
            mes = f"{mes}[Problem dir]:{self.problemdir}\n"
        elif isinstance(self.problemdir, list):
            mes = f"{mes}[Problem dir]:{self.problemdir[0]}\n"
            for i in range(1, len(self.problemdir)):
                mes = f"{mes}              {self.problemdir[i]}\n"
        return mes
    
    
    def __eq__(self, other):
        if not isinstance(other, BugMetaFD_FDSTAT_SET_RIGHTS):
            return NotImplemented
        return (self.runtime == other.runtime and
                self.item == other.item and
                self.bugmsg == other.bugmsg and
                self.rightbefore == other.rightbefore and
                self.rightafter == other.rightafter)

    def __hash__(self):
        return hash((self.runtime, self.item, self.bugmsg, 
                     self.rightbefore, 
                     self.rightafter))
