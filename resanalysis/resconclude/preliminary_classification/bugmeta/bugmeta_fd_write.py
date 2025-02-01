from bugmeta import BugMeta

class BugMetaFD_WRITE(BugMeta):
    def __init__(self, runtime, bugmsg, problemdir,
                 file2per, file2openstyle,
                 sizeexpected, sizebefore, sizeafter,
                 writebytesexpected, writebytesreal,
                 offsetbefore, offsetafter, offsetafterexpected,
                 item="FD_WRITE"):
        self.item = item
        self.runtime = runtime
        self.bugmsg = bugmsg 

        self.file2per = file2per
        self.file2openstyle = file2openstyle
        
        self.sizebefore = sizebefore
        self.sizeafter = sizeafter
        self.sizeexpected = sizeexpected
        
        self.writebytesexpected = writebytesexpected
        self.writebytesreal = writebytesreal
        
        self.offsetbefore = offsetbefore
        self.offsetafter = offsetafter
        self.offsetafterexpected = offsetafterexpected
        
        self.problemdir = problemdir
        
    def print(self):
        print(self.get())
        
    def get(self):
        mes = f"[Runtime]:{self.runtime} -> [Bug item]:{self.item}\n[Bug message]:{self.bugmsg}\n"
        
        mes = f"{mes}[File2per]:{self.file2per}\n"
        mes = f"{mes}[File2openstyle]:{self.file2openstyle}\n"
        mes = f"{mes}[File size before]:{self.sizebefore}\n"
        mes = f"{mes}[File size after]:{self.sizeafter}\n"
        mes = f"{mes}[Write bytes expected]:{self.writebytesexpected}\n"
        mes = f"{mes}[Write bytes real]:{self.writebytesreal}\n"
        mes = f"{mes}[File size expected]:{self.sizeexpected}\n"
        mes = f"{mes}[Offset before]:{self.offsetbefore}\n"
        mes = f"{mes}[Offset after]:{self.offsetafter}\n"
        mes = f"{mes}[Offset after expected]:{self.offsetafterexpected}\n"
        
        if isinstance(self.problemdir, str):
            mes = f"{mes}[Problem dir]:{self.problemdir}\n"
        elif isinstance(self.problemdir, list):
            mes = f"{mes}[Problem dir]:{self.problemdir[0]}\n"
            for i in range(1, len(self.problemdir)):
                mes = f"{mes}              {self.problemdir[i]}\n"
        return mes
    
    
    def __eq__(self, other):
        if not isinstance(other, BugMetaFD_WRITE):
            return NotImplemented
        return (self.runtime == other.runtime and
                self.item == other.item and
                self.bugmsg == other.bugmsg and 
                self.file2per == other.file2per and
                self.file2openstyle == other.file2openstyle and
                self.sizeexpected == other.sizeexpected and
                self.sizebefore == other.sizebefore and
                self.sizeafter == other.sizeafter and 
                self.writebytesexpected == other.writebytesexpected and
                self.writebytesreal == other.writebytesreal and
                self.offsetbefore == other.offsetbefore and
                self.offsetafter == other.offsetafter and
                self.offsetafterexpected == other.offsetafterexpected)
        

    def __hash__(self):
        return hash((self.runtime, self.item, self.bugmsg,
                     self.file2per, self.file2openstyle,
                     self.sizeexpected, self.sizebefore, self.sizeafter,
                     self.writebytesexpected, self.writebytesreal,
                     self.offsetbefore, self.offsetafter, self.offsetafterexpected))
