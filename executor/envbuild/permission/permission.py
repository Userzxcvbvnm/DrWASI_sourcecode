import platform
from enum import Enum

class Type(Enum):
    FILE = "FILE"
    DIR = "DIR"

    @classmethod
    def build_from_str(cls, str):
        if type(str) == Type.FILE or type(str) == Type.DIR:
            return str
        if str == "Type.FILE":
            return Type.FILE
        if str == "Type.DIR":
            return Type.DIR

class LinuxFilePer(Enum):
    W = "0200"
    R = "0400"
    RW = "0600"

    @classmethod
    def get_pers(cls):
        pers = []
        for p in cls:
            pers.append(p.value)
        return pers

class LinuxDirPer(Enum):
    X = "0100"
    W = "0200"
    WX = "0300"
    R = "0400"
    RX = "0500"
    RW = "0600"
    RWX = "0700"

    @classmethod
    def get_pers(cls):
        pers = []
        for p in cls:
            pers.append(p.value)
        return pers

    @classmethod
    def judge_openstyle(cls, openstyle, per):
        print(f"permission judge openstyle: {openstyle} and per: {per}")
        
        demandR = False
        demandW = False
        demandX = False
        if "O_RDONLY" in openstyle:
            demandR = True
        if "O_WRONLY" in openstyle or "O_TRUNC" in openstyle:
            demandW = True
        if "O_RDWR" in openstyle:
            demandR = True
            demandW = True
  
        per = int(per[1])
        
        R = False
        W = False
        X = False
        if per == 1 or per == 3 or per == 5 or per == 7:
            X = True
        if per == 2 or per == 3 or per == 6 or per == 7:
            W = True
        if per == 4 or per == 5 or per ==6 or per == 7:
            R = True
       
        
        if (demandR and not R) or (demandW and not W) or (demandX and not X):
            return False
        return True



class FilePer():
    current_os = platform.system()

    def __init__(self, name, per, t):
        self.name = name
        self.per = per
        self.type = t
    
    def to_str(self):
        return f"{self.name} {self.per} {self.type}"

    @classmethod
    def get_pers(cls):
        if cls.current_os == 'Darwin' or cls.current_os == 'Linux':
            return LinuxFilePer.get_pers()
    
    @classmethod
    def get_reset_per(cls):
        if cls.current_os == 'Darwin' or cls.current_os == 'Linux':
            return LinuxFilePer.RW.value


class DirPer():
    current_os = platform.system()

    def __init__(self, name, per, t):
        self.name = name
        self.per = per
        self.type = t
    
    def to_str(self):
        return f"{self.name} {self.per} {self.type}"

    @classmethod
    def get_pers(cls):
        if cls.current_os == 'Darwin' or cls.current_os == 'Linux':
            return LinuxDirPer.get_pers()
    
    @classmethod
    def get_reset_per(cls):
        if cls.current_os == 'Darwin' or cls.current_os == 'Linux':
            return LinuxDirPer.RWX.value
