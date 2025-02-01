from bugmeta import BugMeta

class BugMetaFD_PWRITE(BugMeta):
    def __init__(self, runtime, bugmsg, problemdir,
                 offset, writesize, 
                 filesizebefore, filesizeafter,
                 readfilesizebefore, readfilesizeafter,
                 item="FD_PWRITE"):
        self.item = item
        self.runtime = runtime
        self.bugmsg = bugmsg 
      
        self.offset = offset
        self.writesize = writesize
        self.filesizebefore = filesizebefore
        self.filesizeafter = filesizeafter
        self.readfilesizebefore = readfilesizebefore
        self.readfilesizeafter = readfilesizeafter
        
        self.problemdir = problemdir
        
    def print(self):
        print(self.get())
        
    def get(self):
        mes = f"[Runtime]:{self.runtime} -> [Bug item]:{self.item}\n[Bug message]:{self.bugmsg}\n"
        
        mes = f"{mes}[Offset]:{self.offset}\n"
        mes = f"{mes}[Writesize]:{self.writesize}\n"
        mes = f"{mes}[Filesizebefore]:{self.filesizebefore}\n"
        mes = f"{mes}[Filesizeafter]:{self.filesizeafter}\n"
        mes = f"{mes}[Readfilesizebefore]:{self.readfilesizebefore}\n"
        mes = f"{mes}[Readfilesizeafter]:{self.readfilesizeafter}\n"
        
        if isinstance(self.problemdir, str):
            mes = f"{mes}[Problem dir]:{self.problemdir}\n"
        elif isinstance(self.problemdir, list):
            mes = f"{mes}[Problem dir]:{self.problemdir[0]}\n"
            for i in range(1, len(self.problemdir)):
                mes = f"{mes}              {self.problemdir[i]}\n"
        return mes
    
    
    def __eq__(self, other):
        if not isinstance(other, BugMetaFD_PWRITE):
            return NotImplemented
        return (self.runtime == other.runtime and
                self.item == other.item and
                self.bugmsg == other.bugmsg and 
                self.offset == other.offset and
                self.writesize == other.writesize and
                self.filesizebefore == other.filesizebefore and
                self.filesizeafter == other.filesizeafter and 
                self.readfilesizebefore == other.readfilesizebefore and
                self.readfilesizeafter == other.readfilesizeafter)
        

    def __hash__(self):
        return hash((self.runtime, self.item, self.bugmsg,
                     self.offset, self.writesize, 
                     self.filesizebefore, self.filesizeafter,
                     self.readfilesizebefore, self.readfilesizeafter,))
