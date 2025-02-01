from bugmeta import BugMeta

class BugMetaFD_RENUMBER(BugMeta):
    def __init__(self, runtime, bugmsg, problemdir,
                 fileper,
                 filename1, filename2,
                 file1openstyle, file2openstyle,
                 item="FD_RENUMBER"):
        self.item = item
        self.runtime = runtime
        self.bugmsg = bugmsg 

        self.filename1 = filename1
        self.filename2 = filename2
        self.fileper = fileper
        self.file1openstyle = file1openstyle
        self.file2openstyle = file2openstyle
        
        self.problemdir = problemdir
        
    def print(self):
        print(self.get())
        
    def get(self):
        mes = f"[Runtime]:{self.runtime} -> [Bug item]:{self.item}\n[Bug message]:{self.bugmsg}\n"
        
        mes = f"{mes}[Filename1]:{self.filename1}\n"
        mes = f"{mes}[Filename2]:{self.filename2}\n"
        mes = f"{mes}[Fileper]:{self.fileper}\n"
        mes = f"{mes}[File1openstyle]:{self.file1openstyle}\n"
        mes = f"{mes}[File2openstyle]:{self.file2openstyle}\n"
        
        if isinstance(self.problemdir, str):
            mes = f"{mes}[Problem dir]:{self.problemdir}\n"
        elif isinstance(self.problemdir, list):
            mes = f"{mes}[Problem dir]:{self.problemdir[0]}\n"
            for i in range(1, len(self.problemdir)):
                mes = f"{mes}              {self.problemdir[i]}\n"
        return mes
    
    
    def __eq__(self, other):
        if not isinstance(other, BugMetaFD_RENUMBER):
            return NotImplemented
        return (self.runtime == other.runtime and
                self.item == other.item and
                self.bugmsg == other.bugmsg and 
                self.filename1 == other.filename1 and
                self.filename2 == other.filename2 and
                self.fileper == other.fileper and
                self.file1openstyle == other.file1openstyle and
                self.file2openstyle == other.file2openstyle)
        

    def __hash__(self):
        return hash((self.runtime, self.item, self.bugmsg,
                     self.filename1, self.filename2,
                     self.fileper, self.file1openstyle, self.file2openstyle))
