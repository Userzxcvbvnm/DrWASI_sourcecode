from bugmeta import BugMeta

class BugMetaPATH_FILESTAT_SET_TIMES(BugMeta):
    def __init__(self, runtime, bugmsg, problemdir,
                 setatime, setmtime,
                 printatime, printmtime,
                 item="PATH_FILESTAT_SET_TIMES"):
        self.item = item
        self.runtime = runtime
        self.bugmsg = bugmsg 
        
        self.setatime = setatime
        self.setmtime = setmtime
        
        self.printatime = printatime
        self.printmtime = printmtime

        self.problemdir = problemdir
        
    def print(self):
        print(self.get())
        
    def get(self):
        mes = f"[Runtime]:{self.runtime} -> [Bug item]:{self.item}\n[Bug message]:{self.bugmsg}\n"
        
        mes = f"{mes}[Set access time]:{self.setatime}\n"
        mes = f"{mes}[Set modification time]:{self.setmtime}\n"
        mes = f"{mes}[Last access time]:{self.printatime}\n"
        mes = f"{mes}[Last modification time]:{self.printmtime}\n"
        
        if isinstance(self.problemdir, str):
            mes = f"{mes}[Problem dir]:{self.problemdir}\n"
        elif isinstance(self.problemdir, list):
            mes = f"{mes}[Problem dir]:{self.problemdir[0]}\n"
            for i in range(1, len(self.problemdir)):
                mes = f"{mes}              {self.problemdir[i]}\n"
        return mes
    
    
    def __eq__(self, other):
        if not isinstance(other, BugMetaPATH_FILESTAT_SET_TIMES):
            return NotImplemented
        return (self.runtime == other.runtime and
                self.item == other.item and
                self.bugmsg == other.bugmsg and
                self.printatime == other.printatime and
                self.printmtime == other.printmtime and
                self.setatime == other.setatime and
                self.setmtime == other.setmtime)
        

    def __hash__(self):
        return hash((self.runtime, self.item, self.bugmsg,
                     self.printatime, self.printmtime,
                     self.setatime, self.setmtime))
