import platform
import subprocess

class CCompiler:
    def __init__(self):
        self.current_os = platform.system()
        self.com = "/usr/local/Cellar/gcc/13.2.0/bin/gcc-13 {file1} -o {file2}"
        self.exedir = "../../../executedir/execfiles"
   
    def compile(self, cfilename, execfilename):
        command = self.com.format(file1=cfilename, file2=execfilename)
        print(f"C compiling command: {command}")
        try:
            subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
            return 0, "success"
        except subprocess.CalledProcessError as e:
            print(f"Command failed with error: {e.stderr}")
            return -1, e.stderr