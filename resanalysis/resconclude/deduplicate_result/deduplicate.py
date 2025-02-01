import os
import sys
import re
sys.path.append("../preliminary_classification")
sys.path.append("./deduplicatecategory")
from deduplicate_open import deduplicate_open
from deduplicate_clock_time_get import deduplicate_clock_time_get
from deduplicate_trunc import deduplicate_trunc
from deduplicate_fd_allocate import deduplicate_fd_allocate
from deduplicate_fd_datasync import deduplicate_fd_datasync
from deduplicate_fd_fdstat_get import deduplicate_fd_fdstat_get
from deduplicate_fd_fdstat_set_flags import deduplicate_fd_fdstat_set_flags
from deduplicate_fd_fdstat_set_rights import deduplicate_fd_fdstat_set_rights
from deduplicate_fd_filetstat_get import deduplicate_fd_filestat_get
from deduplicate_fd_filetstat_set_size import deduplicate_fd_filestat_set_size
from deduplicate_fd_prestat_dir_name import deduplicate_fd_prestat_dir_name
from deduplicate_fd_pwrite import deduplicate_fd_pwrite
from deduplicate_fd_read import deduplicate_fd_read
from deduplicate_fd_readdir import deduplicate_fd_readdir
from deduplicate_fd_renumber import deduplicate_fd_renumber
from deduplicate_fd_seek import deduplicate_fd_seek
from deduplicate_fd_write import deduplicate_fd_write
from deduplicate_path_filestat_get import deduplicate_path_filestat_get
from deduplicate_path_filestat_set_times import deduplicate_path_filestat_set_times
from deduplicate_path_link import deduplicate_path_link
from deduplicate_path_open import deduplicate_path_open
from deduplicate_path_readlink import deduplicate_path_readlink
from deduplicate_path_remove_directory import deduplicate_path_remove_directory
from deduplicate_path_rename import deduplicate_path_rename
from deduplicate_path_symlink import deduplicate_path_symlink
from deduplicate_path_unlink_file import deduplicate_path_unlink_file

PRELIMINARY_DIR = "../preliminary_classification/classificationresult"

def deduplicate_all(curwasifunc="", version="None"):
    if version == "new":
        PRELIMINARY_DIR = "../preliminary_classification/classificationresult/new_version"
    elif version == "old":
        PRELIMINARY_DIR = "../preliminary_classification/classificationresult/old_version"
        
    
    for _, _, filenames in os.walk(PRELIMINARY_DIR):
        for filename in filenames:
            if not filename.endswith(".txt"):
                continue    
            before, _, _ = filename.rpartition('_')
            method_id = before.lower()
            if curwasifunc == "":
                func = globals().get(f"deduplicate_{method_id}")
                func(os.path.join(PRELIMINARY_DIR, filename), version=version)
            elif method_id == curwasifunc:
                func = globals().get(f"deduplicate_{method_id}")
                func(os.path.join(PRELIMINARY_DIR, filename), version=version)
    
                
if __name__ == "__main__":
    deduplicate_all(version="new")
    deduplicate_all(version="old")

