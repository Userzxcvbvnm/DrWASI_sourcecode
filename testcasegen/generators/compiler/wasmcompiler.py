import platform
import subprocess


class WasmCompiler:
    def __init__(self):
        self.current_os = platform.system()
        self.com = "../../../wasi-sdk-21.0/bin/clang --target=wasm32-unkown-wasi --sysroot=/Users/user1/WASM/WASI/wasi-sdk-21.0/share/wasi-sysroot {file1} -o {file2}"
        self.wasmdir = "../../../executedir/wasmfiles"
        self.watdir = "../../../executedir/watfiles"
        
    def compile(self, cfilename, wasmfilename): 
        command = self.com.format(file1=cfilename, file2=wasmfilename)
        print(f"Wasm compiling command: {command}")
        try:
            subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
            return 0, "success"
        except subprocess.CalledProcessError as e:
            print("Command failed with error:", e)
            return -1, e.stderr


    def wasm2wat(self, wasmfilename, watfilename):
        command = f"wasm2wat --enable-all -o {watfilename} {wasmfilename}"
        print(f"Wasm2wat command: {command}")
        subprocess.run(command, shell=True, check=True, capture_output=True, text=True)

