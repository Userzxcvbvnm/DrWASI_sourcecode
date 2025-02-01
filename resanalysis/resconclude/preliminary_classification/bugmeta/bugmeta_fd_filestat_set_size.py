from bugmeta import BugMeta

class BugMetaFD_FILESTAT_SET_SIZE(BugMeta):
    def __init__(self, runtime, bugmsg, problemdir, 
                 sizebefore, sizeafter,
                 readsizebefore, readsizeafter,
                 setsize, openstyle,
                 item="FD_FILESTAT_SET_SIZE"):
        self.item = item
        self.runtime = runtime
        self.bugmsg = bugmsg 
        
        self.sizebefore = sizebefore
        self.sizeafter = sizeafter
        self.readsizebefore = readsizebefore
        self.readsizeafter = readsizeafter
        self.setsize = setsize
        self.openstyle = openstyle
        
        self.problemdir = problemdir
        
    def print(self):
        print(self.get())
        
    def get(self):
        mes = f"[Runtime]:{self.runtime} -> [Bug item]:{self.item}\n[Bug message]:{self.bugmsg}\n"
        
        mes = f"{mes}[Size before]:{self.sizebefore}\n"
        mes = f"{mes}[Size after]:{self.sizeafter}\n"
        mes = f"{mes}[Read size before]:{self.readsizebefore}\n"
        mes = f"{mes}[Read size after]:{self.readsizeafter}\n"
        mes = f"{mes}[Set size]:{self.setsize}\n"
        mes = f"{mes}[Openstyle]:{self.openstyle}\n"
            
            
        if isinstance(self.problemdir, str):
            mes = f"{mes}[Problem dir]:{self.problemdir}\n"
        elif isinstance(self.problemdir, list):
            mes = f"{mes}[Problem dir]:{self.problemdir[0]}\n"
            for i in range(1, len(self.problemdir)):
                mes = f"{mes}              {self.problemdir[i]}\n"
        return mes
    
    
    def __eq__(self, other):
        if not isinstance(other, BugMetaFD_FILESTAT_SET_SIZE):
            return NotImplemented
        return (self.runtime == other.runtime and
                self.item == other.item and
                self.bugmsg == other.bugmsg and
                self.sizebefore == other.sizebefore and
                self.sizeafter == other.sizeafter and
                self.readsizebefore == other.readsizebefore and
                self.readsizeafter == other.readsizeafter and
                self.setsize == other.setsize and
                self.openstyle == other.openstyle)

    def __hash__(self):
        return hash((self.runtime, self.item, self.bugmsg, 
                     self.sizebefore, self.sizeafter,
                     self.readsizebefore, self.readsizeafter,
                     self.setsize, self.openstyle))
