from bugmeta import BugMeta

class BugMetaFD_FILESTAT_GET(BugMeta):
    def __init__(self, runtime, bugmsg, problemdir, 
                 filename, realhardlinknum, printhardlinknum,
                 item="FD_FILESTAT_GET"):
        self.item = item
        self.runtime = runtime
        self.bugmsg = bugmsg 
        
        self.filename = filename
        self.realhardlinknum = realhardlinknum
        self.printhardlinknum = printhardlinknum
        
        self.problemdir = problemdir
        
    def print(self):
        print(self.get())
        
    def get(self):
        mes = f"[Runtime]:{self.runtime} -> [Bug item]:{self.item}\n[Bug message]:{self.bugmsg}\n"
        
        mes = f"{mes}[Filename]:{self.filename}\n"
        mes = f"{mes}[Real hard link num]:{self.realhardlinknum}\n"
        mes = f"{mes}[Print hard link num]:{self.printhardlinknum}\n"
            
        if isinstance(self.problemdir, str):
            mes = f"{mes}[Problem dir]:{self.problemdir}\n"
        elif isinstance(self.problemdir, list):
            mes = f"{mes}[Problem dir]:{self.problemdir[0]}\n"
            for i in range(1, len(self.problemdir)):
                mes = f"{mes}              {self.problemdir[i]}\n"
        return mes
    
    
    def __eq__(self, other):
        if not isinstance(other, BugMetaFD_FILESTAT_GET):
            return NotImplemented
        return (self.runtime == other.runtime and
                self.item == other.item and
                self.bugmsg == other.bugmsg and
                self.filename == self.filename and
                self.realhardlinknum == other.realhardlinknum and
                self.printhardlinknum == other.printhardlinknum)

    def __hash__(self):
        return hash((self.runtime, self.item, self.bugmsg, 
                     self.filename,
                     self.realhardlinknum, self.printhardlinknum))
