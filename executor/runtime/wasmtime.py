import platform
import sys
sys.path.append("../envbuild")
from UnitDir import UnitDir
from runtime import Runtime

class Wasmtime(Runtime):
    def __init__(self):
        self.name = "wasmtime"
        super().__init__()
        self.com = "../../engines/WASM_TIME/wasmtime/target/release/wasmtime run --dir=. {file1} {args}"
      
