from bugmeta import BugMeta

class BugMetaFD_PRESTAT_DIR_NAME(BugMeta):
    def __init__(self, runtime, bugmsg, problemdir,
                 openstyle, modevalue, modemsg,
                 item="FD_PRESTAT_DIR_NAME"):
        self.item = item
        self.runtime = runtime
        self.bugmsg = bugmsg 
      
        self.openstyle = openstyle
        self.modevalue = modevalue
        self.modemsg = modemsg
        
        self.problemdir = problemdir
        
    def print(self):
        print(self.get())
        
    def get(self):
        mes = f"[Runtime]:{self.runtime} -> [Bug item]:{self.item}\n[Bug message]:{self.bugmsg}\n"
        
        mes = f"{mes}[Openstyle]:{self.openstyle}\n"
        mes = f"{mes}[Modevalue]:{self.modevalue}\n"
        mes = f"{mes}[Modemsg]:{self.modemsg}\n"
        
        if isinstance(self.problemdir, str):
            mes = f"{mes}[Problem dir]:{self.problemdir}\n"
        elif isinstance(self.problemdir, list):
            mes = f"{mes}[Problem dir]:{self.problemdir[0]}\n"
            for i in range(1, len(self.problemdir)):
                mes = f"{mes}              {self.problemdir[i]}\n"
        return mes
    
    
    def __eq__(self, other):
        if not isinstance(other, BugMetaFD_PRESTAT_DIR_NAME):
            return NotImplemented
        return (self.runtime == other.runtime and
                self.item == other.item and
                self.bugmsg == other.bugmsg and 
                self.openstyle == other.openstyle and
                self.modevalue == other.modevalue and
                self.modemsg == other.modemsg)


    def __hash__(self):
        return hash((self.runtime, self.item, self.bugmsg,
                     self.openstyle, self.modevalue, self.modemsg))
