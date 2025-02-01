import platform
import sys
sys.path.append("../envbuild")
sys.path.append("../envbuild/permission")
import subprocess
import os
from UnitDir import UnitDir
from permission import Type, FilePer, DirPer

class Runtime:
    def __init__(self):
        self.current_os = platform.system()
        self.dir = f"../../executedir/{self.name}/Data"  
        self.com = "com"
        self.data = "envData"
        

    def build_env(self):
        data = UnitDir(self.dir)
        data.gen_ran_unitdir()
        self.data = data
        return data

    def copy_env(self, data):
        self.data = data.copy_unitdir(self.dir)

    def del_env(self):
        self.data.del_unitdir()
    
    def changeper(self, file2per):
        filename = file2per.name
        if filename.startswith("softfile"):
            filename = os.readlink(filename)
  
        if self.current_os == 'Darwin' or self.current_os == 'Linux':
            com = f"chmod {file2per.per} {filename}"
        elif self.current_os == 'Windows':
            pass
        
        result = subprocess.run(com, shell=True, capture_output=True, text=True)
        print(f"Change permission of {filename} to {file2per.per} : {result}")


    def exe(self, filepath, arg="", exepath="./", fileper=None):
        res = f"--- {self.name} start execute ---\n"

        original_path = os.getcwd()
        res += f"original path {original_path}\n"
        try:
            os.chdir(f"{exepath}")
            if fileper != None:
                self.changeper(fileper)
            res += f"exe path {exepath}\n"
            com = self.com.format(file1=f"{filepath}", args=f"{arg}")   
            res += f"command:{com}\n"
            result = subprocess.run(com, shell=True, capture_output=True, text=True)
            comres2 = f"<stdout>: \n{result.stdout}\n<stderr>: \n{result.stderr}"
            comres = f"<stdout>: \n{result.stdout}"
            res = f"{res}{comres2}"
            
            if fileper != None:
                if fileper.type == Type.FILE:
                    fileper.per = FilePer.get_reset_per()
                elif fileper.type == Type.DIR:
                    fileper.per = DirPer.get_reset_per()
                self.changeper(fileper)
        finally:
            os.chdir(original_path)



        res += f"--- {self.name} finish execute ---\n\n"
        print(res)
        return res, comres