import sys
import time
sys.path.append("./meta")
sys.path.append("../envbuild")
sys.path.append("../envbuild/caseprocess")
sys.path.append("../envbuild/permission")
sys.path.append("../runtime")
sys.path.append("../diffrecord")
sys.path.append("../commandline")
sys.path.append("../../resanalysis/dynamicinfocheck")
sys.path.append("../../resanalysis/staticinfocheck")
import os
import copy
import platform
from UnitDir import UnitDir
from diffrecord import DiffRecorder
from commandline import gen_ran_com_par
from wasmerT import Wasmer
from wasmtime import Wasmtime
from wamr import WAMR
from wasmedge import WasmEdge
from native import Native
from dynamicinfochecker import checkbycontents
from staticinfochecker import checkbypaths
from filearrange import get_names, arrage
from exemeta import ExeMeta
from permissionchanger import getfile2per, getdir2per



class ExEntrance:
    def __init__(self):
        self.EXECUTION_TIMES = 0
        
        current_os = platform.system()
        self.recorder = DiffRecorder()
        self.cfile_dir = "../../executedir/testcasepool/testcases/"
        self.exe_dir = "../../executedir/macOSdir/"
        
    def exe(self, cfilename, envdata=None, perflag=False):
        native = Native()
        
        if envdata == None:
            native.build_env()
        else:
            native.copy_env(UnitDir.build_fromstr(envdata))

        newfilename, arrangedfiles, arrageddirs = arrage(native.data, cfilename)
        
        if cfilename.startswith("path_link"):
            if len(arrangedfiles) == 1:
                print(f"cfilename:{cfilename}")
                while arrangedfiles[0].startswith("hardfile"):
                    newfilename, arrangedfiles, arrageddirs = arrage(native.data, cfilename)
        if cfilename.startswith("path_readlink"):
            if len(arrangedfiles) == 1:
                print(f"cfilename:{cfilename}")
                while not arrangedfiles[0].startswith("softfile"):
                    newfilename, arrangedfiles, arrageddirs = arrage(native.data, cfilename)
                 

        if perflag:
            changefiles = set()
            if len(arrangedfiles) > 0:
                for f in arrangedfiles:
                    changefiles.add(f)
            changedirs = set()
            if len(arrageddirs) > 0:
                for d in arrageddirs:
                    changedirs.add(d)

            changefile2perlist = getfile2per(changefiles)
            changedir2perlist = getdir2per(changedirs)
            changefile2perlist.extend(changedir2perlist)


            if len(changefile2perlist) > 0:
                for c in changefile2perlist:
                    self.exe_unit(f"{newfilename}", native.data, c)       
            else:
                self.exe_unit(f"{newfilename}", native.data)
        else:
            self.exe_unit(f"{newfilename}", native.data)

        os.remove(f"../../executedir/testcasepool/testcases/{newfilename}.c")
        os.remove(f"../../executedir/wasmfiles/{newfilename}.wasm")
        native.del_env()

    def exe_unit(self, cfilename, dirdata, file2per=None):
        print(f"\n\n\n\n\n========================= Start test {cfilename} =========================")
        if file2per != None:
            print(f"Change {file2per.type} type of {file2per.name} permission to {file2per.per}.")

        wasmruntimes = []
        wasmruntimes.append(Wasmer())
        wasmruntimes.append(Wasmtime())
        wasmruntimes.append(WAMR())
        wasmruntimes.append(WasmEdge())

        for r in wasmruntimes:
            r.copy_env(dirdata)
        

        print_contents = []
        dylog = []
        args = gen_ran_com_par(count=2, len=10)

        

        for r in wasmruntimes:
            res, com = r.exe(filepath=f"../../../wasmfiles/{cfilename}.wasm", arg=args, exepath=f"{r.dir}", fileper=copy.copy(file2per))
            print_contents.append(com)
            dylog.append(res)
    

        res1 = checkbycontents(cfilename, print_contents)
        print(f"----- Check dynamic info: {res1}-----")
        res2, dumps = checkbypaths([f"{self.exe_dir}wasmtime", f"{self.exe_dir}wasmer", f"{self.exe_dir}wamr", f"{self.exe_dir}wasmedge"])
        print(f"----- Check static info: {res2}-----")
        if res1 and res2:
            print(f"----- Check pass ^_^ -----")
        else:
            print(f"----- Check not pass! -----")
            exemeta = ExeMeta(name=f"{cfilename}", builtunitdirstr=dirdata.get_unitdir(), dyres=res1, stres=res2, dylogs=dylog, stdumps=dumps, fileper=file2per)
            self.recorder.diffrecord(exemeta.name, exemeta.content)
            
        for r in wasmruntimes:
            r.del_env()


        self.EXECUTION_TIMES = self.EXECUTION_TIMES + 1

        print(f"========================= Finish test {cfilename} =========================\n\n\n\n\n")




    def start_exe_seeds(self):
        items = os.listdir(self.cfile_dir)
        for item in items:
            self.exe(cfilename=item.split('.')[0], perflag=True)
        


if __name__ == "__main__":

    ex = ExEntrance()
    ex.start_exe_seeds()



