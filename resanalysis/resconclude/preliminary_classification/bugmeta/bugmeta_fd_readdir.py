from bugmeta import BugMeta

class BugMetaFD_READDIR(BugMeta):
    def __init__(self, runtime, bugmsg, problemdir,
                 openstyle, per, readcontent, realcontent,
                 item="FD_READDIR"):
        self.item = item
        self.runtime = runtime
        self.bugmsg = bugmsg 

        self.openstyle = openstyle
        self.per = per
        self.readcontent = readcontent
        self.realcontent = realcontent
        
        self.problemdir = problemdir
        
    def print(self):
        print(self.get())
        
    def get(self):
        mes = f"[Runtime]:{self.runtime} -> [Bug item]:{self.item}\n[Bug message]:{self.bugmsg}\n"
        
        mes = f"{mes}[Openstyle]:{self.openstyle}\n"
        mes = f"{mes}[Per]:{self.per}\n"
        mes = f"{mes}[Readcontent]:{self.readcontent}\n"
        mes = f"{mes}[Realcontent]:{self.realcontent}\n"
        
        if isinstance(self.problemdir, str):
            mes = f"{mes}[Problem dir]:{self.problemdir}\n"
        elif isinstance(self.problemdir, list):
            mes = f"{mes}[Problem dir]:{self.problemdir[0]}\n"
            for i in range(1, len(self.problemdir)):
                mes = f"{mes}              {self.problemdir[i]}\n"
        return mes
    
    
    def __eq__(self, other):
        if not isinstance(other, BugMetaFD_READDIR):
            return NotImplemented
        return (self.runtime == other.runtime and
                self.item == other.item and
                self.bugmsg == other.bugmsg and 
                self.openstyle == other.openstyle and
                self.per == other.per and
                self.readcontent == other.readcontent and
                self.realcontent == other.realcontent)
        

    def __hash__(self):
        return hash((self.runtime, self.item, self.bugmsg,
                     self.openstyle, self.per, self.readcontent, self.realcontent))
