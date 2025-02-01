import os
from enum import Enum

class FileType(Enum):
    NormalType = 0
    SoftLinkType = 1
    HardLinkType = 2
    DirType = 3 
    

class NormalFile:
    def __init__(self, filename, content, size):
        self.type = FileType.NormalType
        self.name = filename
        self.content = content
        self.size = size

    def print(self):
        print(self.get())
    
    def get(self):
        return (f"Normal file: '{self.name}' \nFile size: '{self.size}'\nFile content: '{self.content}'")


class SoftLink:
    def __init__(self, sname, lname):
        self.type = FileType.SoftLinkType
        self.source = sname
        self.name = lname
    
    def print(self):
        print(self.get())

    def get(self):
        return (f"Softlink file: '{self.name}' -> '{self.source}'")

class HardLink:
    def __init__(self, sname, lname):
        self.type = FileType.HardLinkType
        self.source = sname
        self.name = lname

    def print(self):
        print(self.get())
    
    def get(self):
        return (f"Hardlink file: '{self.name}' -> '{self.source}'")

class Dir:
    def __init__(self, filename):
        self.type = FileType.DirType
        self.name = filename

    def print(self):
        print(self.get())

    def get(self):
        return (f"Dir: '{self.name}'")
       