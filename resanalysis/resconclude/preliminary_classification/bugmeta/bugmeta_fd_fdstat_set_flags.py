from bugmeta import BugMeta

class BugMetaFD_FDSTAT_SET_FLAGS(BugMeta):
    def __init__(self, runtime, bugmsg, problemdir, 
                 openflags, getflagsbefore,
                 setflags, getflagsafter,
                 item="FD_FDSTAT_SET_FLAGS"):
        self.item = item
        self.runtime = runtime
        self.bugmsg = bugmsg 
        
        self.openflags = openflags
        self.getflagsbefore = getflagsbefore
        self.setflags = setflags
        self.getflagsafter = getflagsafter
        
        self.problemdir = problemdir
        
    def print(self):
        print(self.get())
        
    def get(self):
        mes = f"[Runtime]:{self.runtime} -> [Bug item]:{self.item}\n[Bug message]:{self.bugmsg}\n"
        
        mes = f"{mes}[Openflags]:{self.openflags}\n"
        mes = f"{mes}[Getflagsbefore]:{self.getflagsbefore}\n"
        mes = f"{mes}[Setflags]:{self.setflags}\n"
        mes = f"{mes}[Getflagsafter]:{self.getflagsafter}\n"
            
        if isinstance(self.problemdir, str):
            mes = f"{mes}[Problem dir]:{self.problemdir}\n"
        elif isinstance(self.problemdir, list):
            mes = f"{mes}[Problem dir]:{self.problemdir[0]}\n"
            for i in range(1, len(self.problemdir)):
                mes = f"{mes}              {self.problemdir[i]}\n"
        return mes
    
    
    def __eq__(self, other):
        if not isinstance(other, BugMetaFD_FDSTAT_SET_FLAGS):
            return NotImplemented
        return (self.runtime == other.runtime and
                self.item == other.item and
                self.bugmsg == other.bugmsg and
                self.openflags == other.openflags and
                self.getflagsbefore == other.getflagsbefore and
                self.setflags == other.setflags and
                self.getflagsafter == other.getflagsafter)

    def __hash__(self):
        return hash((self.runtime, self.item, self.bugmsg, 
                     self.openflags, self.getflagsbefore, self.setflags, self.getflagsafter))
