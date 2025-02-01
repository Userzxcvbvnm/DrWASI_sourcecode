import platform
from datetime import datetime
import shutil
import os

class DiffRecorder:
    def __init__(self):
        self.dir = "../../executedir/problem"
        

    def diffrecord(self, testcasename, content):
        current_time = datetime.now()
        formatted_time = current_time.strftime("%Y-%m-%d-%H:%M:%S.%f")

        subdir = testcasename.split("_0")[0]
        path = f"{self.dir}/{subdir}/{testcasename}-{formatted_time}"
        os.makedirs(path)

        recordfile = f"{path}/{testcasename}.log"
        print(f"recordfile:{recordfile}")
        with open(recordfile, 'w') as file:
            file.write(content)
        
        destination_path = os.path.join(path, f"{testcasename}.c")
        print(f"destination_path:{destination_path}")
        shutil.copy2(f"../../executedir/testcasepool/testcases/{testcasename}.c", destination_path)

        destination_path = os.path.join(path, f"{testcasename}.wasm")
        shutil.copy2(f"../../executedir/wasmfiles/{testcasename}.wasm", destination_path)



