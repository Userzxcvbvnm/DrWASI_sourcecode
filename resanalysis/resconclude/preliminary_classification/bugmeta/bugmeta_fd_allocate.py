from bugmeta import BugMeta

class BugMetaFD_ALLOCATE(BugMeta):
    def __init__(self, runtime, bugmsg, problemdir, 
                 startvalue, allocatelen, 
                 sizebefore, sizeafter,
                 readsizebefore, readsizeafter,
                 item="FD_ALLOCATE"):
        self.item = item
        self.runtime = runtime
        self.bugmsg = bugmsg 
        
        self.startvalue = startvalue 
        self.allocatelen = allocatelen 
        self.sizebefore = sizebefore 
        self.sizeafter = sizeafter 
        self.readsizebefore = readsizebefore
        self.readsizeafter = readsizeafter
        
        self.problemdir = problemdir
        
    def print(self):
        print(self.get())
        
    def get(self):
        mes = f"[Runtime]:{self.runtime} -> [Bug item]:{self.item}\n[Bug message]:{self.bugmsg}\n"
        
        mes = f"{mes}[Allocate start value]:{self.startvalue}\n"
        mes = f"{mes}[Allocate length]:{self.allocatelen}\n"
        mes = f"{mes}[Size before allocate]:{self.sizebefore}\n"
        mes = f"{mes}[Size after allocate]:{self.sizeafter}\n"
        mes = f"{mes}[Size read before allocate]:{self.readsizebefore}\n"
        mes = f"{mes}[Size read after allocate]:{self.readsizeafter}\n"
            
        if isinstance(self.problemdir, str):
            mes = f"{mes}[Problem dir]:{self.problemdir}\n"
        elif isinstance(self.problemdir, list):
            mes = f"{mes}[Problem dir]:{self.problemdir[0]}\n"
            for i in range(1, len(self.problemdir)):
                mes = f"{mes}              {self.problemdir[i]}\n"
        return mes
    
    
    def __eq__(self, other):
        if not isinstance(other, BugMetaFD_ALLOCATE):
            return NotImplemented
        return (self.runtime == other.runtime and
                self.item == other.item and
                self.bugmsg == other.bugmsg and
                self.startvalue == other.startvalue and
                self.allocatelen == other.allocatelen and
                self.sizebefore == other.sizebefore and
                self.sizeafter == other.sizeafter and
                self.readsizebefore == other.readsizebefore and
                self.readsizeafter == other.readsizeafter)

    def __hash__(self):
        return hash((self.runtime, self.item, self.bugmsg, 
                     self.startvalue, self.allocatelen,
                     self.sizebefore, self.sizeafter,
                     self.readsizebefore, self.readsizeafter))
