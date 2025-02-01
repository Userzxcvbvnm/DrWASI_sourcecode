from bugmeta import BugMeta

class BugMetaFD_READ(BugMeta):
    def __init__(self, runtime, bugmsg, problemdir,
                 filesize, buffersize, readsize,
                 item="FD_READ"):
        self.item = item
        self.runtime = runtime
        self.bugmsg = bugmsg 

        self.filesize = filesize
        self.buffersize = buffersize
        self.readsize = readsize
        
        self.problemdir = problemdir
        
    def print(self):
        print(self.get())
        
    def get(self):
        mes = f"[Runtime]:{self.runtime} -> [Bug item]:{self.item}\n[Bug message]:{self.bugmsg}\n"
        
        mes = f"{mes}[Filesize]:{self.filesize}\n"
        mes = f"{mes}[Buffersize]:{self.buffersize}\n"
        mes = f"{mes}[Readsize]:{self.readsize}\n"
        
        if isinstance(self.problemdir, str):
            mes = f"{mes}[Problem dir]:{self.problemdir}\n"
        elif isinstance(self.problemdir, list):
            mes = f"{mes}[Problem dir]:{self.problemdir[0]}\n"
            for i in range(1, len(self.problemdir)):
                mes = f"{mes}              {self.problemdir[i]}\n"
        return mes
    
    
    def __eq__(self, other):
        if not isinstance(other, BugMetaFD_READ):
            return NotImplemented
        return (self.runtime == other.runtime and
                self.item == other.item and
                self.bugmsg == other.bugmsg and 
                self.filesize == other.filesize and 
                self.buffersize == other.buffersize and
                self.readsize == other.readsize)
        

    def __hash__(self):
        return hash((self.runtime, self.item, self.bugmsg,
                     self.filesize, self.buffersize, self.readsize))
