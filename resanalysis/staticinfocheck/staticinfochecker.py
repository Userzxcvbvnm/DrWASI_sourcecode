import sys
sys.path.append("../../executor/staticinfo")
sys.path.append("../../executor/envbulid")
from StaticInfo import dump_dir
from build_Data import UnitDir

def checkbypaths(paths, unitdir="Data"):
    if len(paths) <= 1:
        return True, []
    oracle = dump_dir(paths[0], unitdir).get_unitdir()

    dumps = [f"---Dump dir: {paths[0]}---\n{oracle}----- End dump dir -----\n\n"]
    i = 1
    while i < len(paths):
        cur_dump = dump_dir(paths[i], unitdir).get_unitdir()
        if  cur_dump != oracle:
            j = 1
            while j < len(paths):
                dumps.append(f"---Dump dir: {paths[j]}---\n{dump_dir(paths[j], unitdir).get_unitdir()}----- End dump dir -----\n\n")
                j = j + 1
            return False, dumps
        i = i + 1
    return True, dumps
