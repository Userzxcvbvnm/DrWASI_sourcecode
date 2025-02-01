import platform
import sys
sys.path.append("../envbuild")
from UnitDir import UnitDir
from runtime import Runtime

class Wasmer(Runtime):
    def __init__(self):
        self.name = "wasmer"
        super().__init__()
        self.com = "../../engines/WASMER/wasmer/target/release/wasmer run --dir=. {file1} {args}"
        