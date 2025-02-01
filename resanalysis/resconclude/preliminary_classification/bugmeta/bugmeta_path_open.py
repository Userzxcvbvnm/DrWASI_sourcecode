from bugmeta import BugMeta

class BugMetaPATH_OPEN(BugMeta):
    def __init__(self, runtime, bugmsg, problemdir,
                 file2perstr, file2openstyle,
                 item="PATH_OPEN"):
        self.item = item
        self.runtime = runtime
        self.bugmsg = bugmsg 

        self.file2openstyle = file2openstyle
        self.file2per = file2perstr
        
        self.problemdir = problemdir
        
    def print(self):
        print(self.get())
        
    def get(self):
        mes = f"[Runtime]:{self.runtime} -> [Bug item]:{self.item}\n[Bug message]:{self.bugmsg}\n"
        
        mes = f"{mes}[File2per]:{self.file2per}\n"
        mes = f"{mes}[File2openstyle]:{self.file2openstyle}\n"
        
        if isinstance(self.problemdir, str):
            mes = f"{mes}[Problem dir]:{self.problemdir}\n"
        elif isinstance(self.problemdir, list):
            mes = f"{mes}[Problem dir]:{self.problemdir[0]}\n"
            for i in range(1, len(self.problemdir)):
                mes = f"{mes}              {self.problemdir[i]}\n"
        return mes
    
    
    def __eq__(self, other):
        if not isinstance(other, BugMetaPATH_OPEN):
            return NotImplemented
        return (self.runtime == other.runtime and
                self.item == other.item and
                self.bugmsg == other.bugmsg and
                self.file2per == other.file2per and 
                self.file2openstyle == other.file2openstyle)
        

    def __hash__(self):
        return hash((self.runtime, self.item, self.bugmsg,
                     self.file2per, self.file2openstyle))
