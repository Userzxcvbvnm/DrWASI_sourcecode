from bugmeta import BugMeta

class BugMetaFD_PREAD(BugMeta):
    def __init__(self, runtime, bugmsg, problemdir,
                 filesize, preadoffset,
                 buffersize, preadsize,
                 item="FD_PREAD"):
        self.item = item
        self.runtime = runtime
        self.bugmsg = bugmsg 
      
        self.buffersize = buffersize
        self.preadsize = preadsize
        self.filesize = filesize
        self.preadoffset = preadoffset
        
        self.problemdir = problemdir
        
    