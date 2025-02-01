import os
import io
import re
import random
import string
import shutil
from File import Dir, NormalFile, SoftLink, HardLink

def gen_ran_str(min, max):
    length = random.randint(min, max)
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for _ in range(length))

class UnitDir:
    def __init__(self, rootdir, adddataflag=True):
        self.normalfiles = [] # file1
        self.softlinkfiles = []
        self.hardlinkfiles = []
        self.dirs = [] # subdir_1
    
        self.basedir = rootdir # ./
        if adddataflag:
            self.dirs.append(Dir('.')) # Data      
            try:
                os.mkdir(self.basedir)
                print(f"'{self.basedir}' created.")
            except FileExistsError:
                print(f"'{self.basedir}' Already exists!")

    @classmethod
    def build_fromstr(cls, str):
        data = UnitDir(rootdir="./Data", adddataflag=False)
        string_io = io.StringIO(str)
        while True:
            line = string_io.readline()
            if not line:
                break
            if line.startswith("Dir:"):
                start_index = line.find("'")
                end_index = line.find("'", start_index + 1)
                name = line[start_index + 1:end_index]
                data.dirs.append(Dir(name))
            elif line.startswith("Normal file:"):
                start_index = line.find("'")
                end_index = line.find("'", start_index + 1)
                name = line[start_index + 1:end_index]
                line = string_io.readline()
                start_index = line.find("'''")
                end_index = line.find("'''", start_index + 1)
                content = line[start_index + 1:end_index] 
                data.normalfiles.append(NormalFile(name, content))
            elif line.startswith("Softlink file:"):
                indices = [index for index, char in enumerate(line) if char == '\''][:4]
                linkfile = line[indices[0] + 1:indices[1]]
                sourcefile = line[indices[2] + 1:indices[3]]
                data.softlinkfiles.append(SoftLink(sourcefile, linkfile))
            elif line.startswith("Hardlink file:"):
                indices = [index for index, char in enumerate(line) if char == '\''][:4]
                linkfile = line[indices[0] + 1:indices[1]]
                sourcefile = line[indices[2] + 1:indices[3]]
                data.softlinkfiles.append(HardLink(sourcefile, linkfile))
            else:
                print("!!! Str pre directory error !!!")
                return None

        data.print_unitdir()
        return data

    def print_unitdir(self):
        print(self.get_unitdir())

    def get_unitdir(self):
        content = ""
        for dir in self.dirs:
            content += dir.get() + "\n"
        for file in self.normalfiles:
            content += file.get() + "\n"
        for soft in self.softlinkfiles:
            content += soft.get() + "\n"
        for hard in self.hardlinkfiles:
            content += hard.get() + "\n"
        return content
    
    def del_unitdir(self):
        datadir = os.path.join(self.basedir) 
        shutil.rmtree(datadir)
        del self

    def gen_ran_unitdir(self, min_subdirs=2, max_subdirs=3, min_subfiles=2, max_subfiles=3, min_content=0, max_content=100, min_softfiles=1, max_softfiles=5, min_hardfiles=1, max_hardfiles=5):
        num_subdirs = random.randint(min_subdirs, max_subdirs)
        
        cur_dir = os.getcwd()
        os.chdir(self.basedir)

        for i in range(num_subdirs):
            # subdir_name = f"Data/subdir_{i+1}"
            # subdir_path = os.path.join(self.basedir, subdir_name)
            subdir_name = f"subdir_{i+1}"
            subdir_path = subdir_name
            os.mkdir(subdir_path)
            self.dirs.append(Dir(subdir_name))
            # print(f"'{subdir_path}' created.")


        for j in range(5):
            dir = random.choice(self.dirs)
            while dir.name == ".":
                dir = random.choice(self.dirs)
            subdir_name = f"{dir.name}/subdir_{j+1}"
            subdir_path = subdir_name
            os.mkdir(subdir_path)
            self.dirs.append(Dir(subdir_name))
            # print(f"'{subdir_path}' created.")
        

        for dir in self.dirs:
            num_subfiles = random.randint(min_subfiles, max_subfiles)
            for i in range(num_subfiles):
                if dir.name == ".":
                    subfile_name = f"subfile_{i+1}"
                else:
                    subfile_name = f"{dir.name}/subfile_{i+1}"
                subfile_path = subfile_name
                content = gen_ran_str(min_content, max_content)
                with open(subfile_path, 'w') as f:
                    f.write(content)
                size = os.path.getsize(subfile_path)
                self.normalfiles.append(NormalFile(subfile_name, content, size))
                # print(f"'{subfile_path}' created.")

        num_softfiles = random.randint(min_softfiles, max_softfiles)
        for i in range(num_softfiles):
            subsoft_name = f"softfile_{i+1}"
            subsoft_path = subsoft_name
            source_file = random.choice(self.normalfiles)
            source_path = source_file.name
            os.symlink(source_path, subsoft_path)
            self.softlinkfiles.append(SoftLink(source_file.name, subsoft_name))
            # print(f"Softlink '{subsoft_path}' -> '{source_path}' created.")

        num_hardfiles = random.randint(min_hardfiles, max_hardfiles)
        for i in range(num_hardfiles):
            subhard_name = f"hardfile_{i+1}"
            subhard_path = subhard_name
            source_file = random.choice(self.normalfiles)
            source_path = source_file.name
            os.link(source_path, subhard_path)
            self.hardlinkfiles.append(HardLink(source_file.name, subhard_name))
            # print(f"Hardlink '{subhard_path}' -> '{source_path}' created.")

        os.chdir(cur_dir)
        


    def copy_unitdir(self, rootdir):
        current_path = os.getcwd()
        data = UnitDir(rootdir)
        data.normalfiles = self.normalfiles
        data.softlinkfiles = self.softlinkfiles
        data.hardlinkfiles = self.hardlinkfiles
        data.dirs = self.dirs
        
        cur_dir = os.getcwd()
        os.chdir(rootdir)
        

        for dir in data.dirs:
            if dir.name == ".":
                continue
            os.mkdir(dir.name)


        for file in data.normalfiles:
            with open(file.name, 'w') as f:
                    f.write(file.content)


        for softfile in data.softlinkfiles:
            os.symlink(softfile.source, softfile.name)
           

        for hardfile in data.hardlinkfiles:
            os.link(hardfile.source, hardfile.name)
          
        os.chdir(cur_dir)
        
        return data

