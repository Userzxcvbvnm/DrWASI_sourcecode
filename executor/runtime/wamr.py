import platform
import sys
sys.path.append("../envbuild")
from UnitDir import UnitDir
from runtime import Runtime

class WAMR(Runtime):
    def __init__(self):
        self.name = "wamr"
        super().__init__()
        self.com = "../../engines/WAMR/wasm-micro-runtime/product-mini/platforms/darwin/build/iwasm --dir=. {file1} {args}"
       