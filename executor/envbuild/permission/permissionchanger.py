from permission import FilePer, DirPer, Type

def getfile2per(filepath):
    file2perlist = []
    if filepath == None or len(filepath) == 0:
        return file2perlist

    pers = FilePer.get_pers()
    for f in filepath:
        for p in pers:
            file2perlist.append(FilePer(f, p, Type.FILE))

    return file2perlist

def getdir2per(dirpath):
    dir2perlist = []
    if dirpath == None or len(dirpath) == 0:
        return dir2perlist

    pers = DirPer.get_pers()
    for d in dirpath:
        for p in pers:
            dir2perlist.append(DirPer(d, p, Type.DIR))

    return dir2perlist
