import platform
import sys
sys.path.append("../envbuild")
import subprocess
import os
from UnitDir import UnitDir
from runtime import Runtime

class Native(Runtime):
    def __init__(self):
        self.name = "native"
        super().__init__()
        if self.current_os == 'Darwin':
            self.com = "{file1} {args}"
        elif self.current_os == 'Linux':
            self.com = "{file1} {args}"
            
