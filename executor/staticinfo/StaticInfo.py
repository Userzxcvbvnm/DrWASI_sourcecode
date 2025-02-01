import sys
sys.path.append("../envbuild")
import os
import stat
import hashlib
from File import NormalFile, Dir, SoftLink, HardLink
from UnitDir import UnitDir

def dump_dir_without_hard_source(basedir, curdir):
    cur_path = os.path.join(basedir, curdir)
    curdata = UnitDir(basedir, adddataflag=False)
    curdata.dirs.append(Dir(curdir))

    dirs_and_files = next(os.walk(cur_path))[1:]
    dirs = dirs_and_files[0]
    files = dirs_and_files[1]
    
        
    for file in files:
        file_path = os.path.join(cur_path, file)
        file_stat = os.lstat(file_path)
        file_name = os.path.join(curdir, file)
        if stat.S_ISLNK(file_stat.st_mode):
            target = os.readlink(file_path)
            index = target.rfind("Data")
            target = target[index:]
            curdata.softlinkfiles.append(SoftLink(target, file_name))
        elif file_stat.st_nlink > 1 and file.startswith("hard"):
            curdata.hardlinkfiles.append(HardLink("", file_name))
        else:
            try:
                with open(file_path, "r") as f:
                    content = f.read()
                    size = os.path.getsize(file_path)
            except Exception:
                content = "Read content failed."
                size = len(content.encode('utf-8'))

            curdata.normalfiles.append(NormalFile(file_name, content, size))
        
    for dir in dirs:
        subdirdata = dump_dir_without_hard_source(basedir, f"{curdir}/{dir}")
        curdata.dirs.extend(subdirdata.dirs)
        curdata.normalfiles.extend(subdirdata.normalfiles)
        curdata.softlinkfiles.extend(subdirdata.softlinkfiles)
        curdata.hardlinkfiles.extend(subdirdata.hardlinkfiles)

    return curdata


def dump_dir(basedir, curdir="Data"):
    data = dump_dir_without_hard_source(basedir, curdir)

    for hard in data.hardlinkfiles:
        hard_stat = os.lstat(os.path.join(basedir, hard.name))
        for file in data.normalfiles:
            file_stat = os.lstat(os.path.join(basedir, file.name))
            if hard_stat.st_ino == file_stat.st_ino:
                hard.source = file.name
                break

    return data



if __name__ == "__main__":
    data = dump_dir("./", "Data")
    data_stat = data.get_unitdir()

    data2 = dump_dir("./copy", "Data")
    data_stat2 = data2.get_unitdir()


    print(data_stat == data_stat2)

