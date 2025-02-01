from openai import OpenAI 
import re
import os
import sys
import time
from enum import Enum
sys.path.append("../GPT")
sys.path.append("../../WASImodel")
sys.path.append("../compiler")
from GPTagent import GPTAgent
from indexgen import gen_random_string
from WASImodelTransformer import gen_model
from ccompiler import CCompiler
from wasmcompiler import WasmCompiler
from sourcetool import get_func
from handwritten import HandWritten


class SeedGenerator:
    def __init__(self, genpath="../../../executedir/testcasepool"):
        self.agent = GPTAgent()
        self.ccompiler = CCompiler()
        self.wasmcompiler = WasmCompiler()
        if not os.path.exists(f"{genpath}/seeds/basicoper/get_fd.c"):
            self.gen_get_fd()
        if not os.path.exists(f"{genpath}/seeds/basicoper/closebyfd.c"):
            self.gen_closebyfd()
        self.get_fd = get_func(f"{genpath}/seeds/basicoper/get_fd.c", "get_fd")
        self.closebyfd = get_func(f"{genpath}/seeds/basicoper/closebyfd.c", "closebyfd")
        


    def gen_get_fd(self, filepath="../../../executedir/testcasepool/seeds/basicoper/get_fd.c"):
        reqstr = """Please generate a C function named get_fd, \
which could open the file example.txt with O_RDONLY parameter.\n\
Both the filename and O_RDONLY are parameters of the function.\
If the file is successfully opened, output ("Get file descriptor of file %s succeed!\n", filename) and return the file descriptor.\
And if not, output ("Get file descriptor of file %s failed!\n", filename) and return -1.\n\
Don't need a main function to call get_fd.\
Contain the code with ```c and ```\
"""
        print(f"Prompt: {reqstr}")
        res = self.agent.request(reqstr)
        print(f"Answer: \n{res}")
        pattern = r'```c(.*?)```'
        match = re.search(pattern, res, re.DOTALL)
        code = ""
        if match:
            code = match.group(1)
            print(f"Get code in the answer: \n{code}")
        if code != "" and filepath != "":
            with open(filepath, 'w') as file:
                file.write(code)



    def gen_closebyfd(self, filepath="../../../executedir/testcasepool/seeds/basicoper/closebyfd.c"):
        reqstr = """Please generate a C function named closebyfd, \
with one parameter represents a file descriptor,\
close the file in the function.\
If the file is failed to close, output ("Close the file %d by descriptor failed!\n", fd)\
Don't need a main function to call closebyfd.\
Contain the code with ```c and ```\
"""
        print(f"Prompt: {reqstr}")
        res = self.agent.request(reqstr)
        print(f"Answer: \n{res}")
        pattern = r'```c(.*?)```'
        match = re.search(pattern, res, re.DOTALL)
        code = ""
        if match:
            code = match.group(1)
            print(f"Get code in the answer: \n{code}")
        if code != "" and filepath != "":
            with open(filepath, 'w') as file:
                file.write(code)


    def getcode_fromreq(self, reqstr, filepath):
        print(f"Prompt: {reqstr}")
        res = self.agent.request(reqstr)
        print(f"Answer: \n{res}")
        pattern = r'```c(.*?)```'
        match = re.search(pattern, res, re.DOTALL)
        code = ""
        if match:
            code = match.group(1)
            print(f"Get code in the answer: \n{code}")
        if code != "" and filepath != "":
            with open(filepath, 'w') as file:
                file.write(code)


    def gentemcode_unit(self, func, filepath=""):
        index = gen_random_string(5)
        if func.posix == "":
            reqstr = f"""Please generate a C function named {func.name}_{index}, \
which has the following functionality: {func.functionality}.\n"""
        else:
            reqstr = f"""Please generate a C function named {func.name}_{index}, \
which has the following functionality: {func.functionality}, and make sure to use the {func.posix} function in POSIX.\
 And output the result message aftering calling the {func.posix} function.\n"""

        
        reqstr = f"""{reqstr}And provide a function named main to call the {func.name}_{index} function.\n\
Finally, insert a print statement at the beginning of each function execution to print 'Enter function ' followed by the function name.\n"""

        if func.needfd:
            reqstr = f"""{reqstr}\
If this program needs a descriptor of a file or directory, please use {self.get_fd} to get the fd variant.\
 If the program needs to access a file, using int fd = get_fd("EXAMPLEFILE", O_RDONLY).\
 And if the program needs to access a directory, using int fd = get_fd("EXAMPLEDIR", O_RDONLY).\
 If this program needs to close a file or directory, please use {self.closebyfd}.\n\
And use the main function to call the function get_fd and closebyfd.\
 After gettig the fd from function, judge whether the result is -1.\
 If it is, return from the main function.\n\
The signature of function {func.name}_{index} is `void {func.name}_{index}(int fd)`.\n\
Please ensure that all possible locations where exceptions may be thrown are handled.\
"""
        reqstr = f"""{reqstr}\
Place the generated code between ```c and ```.\
"""
        self.getcode_fromreq(reqstr, filepath)


    def compile_unit(self, filepath, formatted_file):
       
        
        print(f"Compiling to Wasm binary...")
        r, m = self.wasmcompiler.compile(filepath, f"{self.wasmcompiler.wasmdir}/{formatted_file}.wasm")
        if r == -1:
            while(r == -1):
                print("Regenerating c code...")
                reqstr = f"Get the result {m}, please modify the generated code between ```c and ```."
                self.getcode_fromreq(reqstr, filepath)
                r, m = self.ccompiler.compile(filepath, f"{self.ccompiler.exedir}/{formatted_file}")
                if r == 0:
                    r, m = self.wasmcompiler.compile(filepath, f"{self.wasmcompiler.wasmdir}/{formatted_file}.wasm")
        self.wasmcompiler.wasm2wat(f"{self.wasmcompiler.wasmdir}/{formatted_file}.wasm", f"{self.wasmcompiler.watdir}/{formatted_file}.wat")



    def gentemcode(self, filepath="../../WASImodel/modelfiles/wasi_snapshot_preview1.witx", modelpath="../../WASImodel/modelfiles/model", genpath="../../../executedir/testcasepool/seeds"):
        model = gen_model(file=filepath, output=modelpath)
        model.print()
        for f in model.func:
            if f.name in HandWritten:
                continue
            index = 0 # test case file index
            formatted_index = str(index).zfill(5)
            formatted_file = f"{f.name}_{formatted_index}"
            print(f"【GPT】 generate code for function [{formatted_file}]...")
            filepath = f"{genpath}/{formatted_file}.c"
            self.gentemcode_unit(f, filepath)
            self.compile_unit(filepath, formatted_file)


if __name__ == "__main__":
    start_time = time.time()
    
    fungen = SeedGenerator()
    fungen.gentemcode(filepath="../../WASImodel/modelfiles/wasi_snapshot_preview1.witx")

    end_time = time.time()
    execution_time = end_time - start_time  
    print(f"Execution Time for Generating Seeds: {execution_time:.2f} s")  