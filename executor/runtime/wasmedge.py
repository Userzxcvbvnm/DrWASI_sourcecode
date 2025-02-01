import platform
import sys
sys.path.append("../envbuild")
from UnitDir import UnitDir
from runtime import Runtime

class WasmEdge(Runtime):
    def __init__(self):
        self.name = "wasmedge"
        super().__init__()
        self.com = "../../engines/WASM_EDGE/WasmEdge-0.13.5-Darwin/bin/wasmedge --dir=. {file1} {args}"
        