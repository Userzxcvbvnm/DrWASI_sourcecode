from bugmeta import BugMeta

class BugMetaTRUNC(BugMeta):
    def __init__(self, runtime, bugmsg, problemdir, 
                 filename, per, openstyle, filesizebefore, filesizeafter,
                 item="TRUNC"):
        self.item = item
        self.runtime = runtime
        self.bugmsg = bugmsg 
        
        self.filename = filename
        self.per = per
        self.openstyle = openstyle
        self.filesizebefore = filesizebefore
        self.filesizeafter = filesizeafter
        
        self.problemdir = problemdir
        
    def print(self):
        print(self.get())
        
    def get(self):
        mes = f"[Runtime]:{self.runtime} -> [Bug item]:{self.item}\n[Bug message]:{self.bugmsg}\n"
        
        mes = f"{mes}[Filename]:{self.filename}\n"
        mes = f"{mes}[Per]:{self.per}\n"
        mes = f"{mes}[Openstyle]:{self.openstyle}\n"
        mes = f"{mes}[File size before]:{self.filesizebefore}\n"
        mes = f"{mes}[File size after]:{self.filesizeafter}\n"

            
        if isinstance(self.problemdir, str):
            mes = f"{mes}[Problem dir]:{self.problemdir}\n"
        elif isinstance(self.problemdir, list):
            mes = f"{mes}[Problem dir]:{self.problemdir[0]}\n"
            for i in range(1, len(self.problemdir)):
                mes = f"{mes}              {self.problemdir[i]}\n"
        return mes
    
    
    def __eq__(self, other):
        if not isinstance(other, BugMetaTRUNC):
            return NotImplemented
        return (self.runtime == other.runtime and
                self.item == other.item and
                self.bugmsg == other.bugmsg and
                self.filename == other.filename and
                self.per == other.per and
                self.openstyle == other.openstyle and
                self.filesizebefore == other.filesizebefore and
                self.filesizeafter == other.filesizeafter)

    def __hash__(self):
        return hash((self.runtime, self.item, self.bugmsg,
                     self.filename, self.per, self.openstyle, 
                     self.filesizebefore, self.filesizeafter))
