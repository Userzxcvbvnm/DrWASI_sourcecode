from enum import Enum
import sys
import re
sys.path.append("./judgecategory")
from judge_open import judge_open
from judge_clock_time_get import judge_clock_time_get
from judge_fd_allocate import judge_fd_allocate
from judge_fd_datasync import judge_fd_datasyc
from judge_fd_fdstat_get import judge_fd_fdstat_get
from judge_fd_fdstat_set_flags import judge_fd_fdstat_set_flags
from judge_fd_fdstat_set_rights import judge_fd_fdstat_set_rights
from judge_fd_filestat_get import judge_fd_filestat_get
from judge_fd_filestat_set_size import judge_fd_filestat_set_size
from judge_fd_pread import judge_fd_pread
from judge_fd_prestat_dir_name import judge_fd_prestat_dir_name
from judge_fd_pwrite import judge_fd_pwrite
from judge_fd_read import judge_fd_read
from judge_fd_readdir import judge_fd_readdir
from judge_fd_renumber import judge_fd_renumber
from judge_fd_seek import judge_fd_seek
from judge_fd_write import judge_fd_write
from judge_path_filestat_get import judge_path_filestat_get
from judge_path_filestat_set_times import judge_path_filestat_set_times
from judge_path_link import judge_path_link
from judge_path_open import judge_path_open
from judge_path_readlink import judge_path_readlink
from judge_path_rename import judge_path_rename
from judge_path_symlink import judge_path_symlink
from judge_path_unlink_file import judge_path_unlink_file
from judge_trunc import judge_trunc


def judge(runtimename, problemdir, file2per, logcontent, ccontent, snapshotbefore, snapshotafter, platform):
    items = []
        
    if file2per != "":
        judge_open(items=items, runtime=runtimename, snapshotbefore=snapshotbefore, file2per=file2per, ccontent=ccontent, 
                                        logcontent=logcontent, platform=platform, problemdir=problemdir)
        

    if "clock_time_get" in problemdir:
        judge_clock_time_get(items=items, runtime=runtimename, logcontent=logcontent, problemdir=problemdir)

    if "fd_advise" in problemdir:
        judge_trunc(items=items, runtime=runtimename, file2per=file2per, snapshotbefore=snapshotbefore, snapshotafter=snapshotafter, 
                          logcontent=logcontent, ccontent=ccontent, problemdir=problemdir)
    
    if "fd_allocate" in problemdir:
        judge_fd_allocate(items=items, runtime=runtimename, snapshotbefore=snapshotbefore, snapshotafter=snapshotafter, 
                          logcontent=logcontent, ccontent=ccontent, problemdir=problemdir)
        
    if "fd_datasync" in problemdir:
        judge_fd_datasyc(items=items, runtime=runtimename, logcontent=logcontent, problemdir=problemdir)
    
    if "fd_fdstat_get" in problemdir:
        judge_fd_fdstat_get(items=items, runtime=runtimename, logcontent=logcontent, ccontent=ccontent, problemdir=problemdir)
    
    if "fd_fdstat_set_flags" in problemdir:
        judge_fd_fdstat_set_flags(items=items, runtime=runtimename, logcontent=logcontent, ccontent=ccontent, problemdir=problemdir)
    
    if "fd_fdstat_set_rights" in problemdir:
        judge_fd_fdstat_set_rights(items=items, runtime=runtimename, logcontent=logcontent, ccontent=ccontent, problemdir=problemdir)
         
    if "fd_fdstat_set_rights" in problemdir:
        judge_fd_fdstat_set_rights(items=items, runtime=runtimename, logcontent=logcontent, ccontent=ccontent, problemdir=problemdir)
     
    if "fd_filestat_get" in problemdir:
        judge_fd_filestat_get(items=items, runtime=runtimename, snapshotbefore=snapshotbefore, logcontent=logcontent, ccontent=ccontent, problemdir=problemdir)
    
    
    if "fd_filestat_set_size" in problemdir:
        judge_fd_filestat_set_size(items=items, runtime=runtimename, snapshotbefore=snapshotbefore, snapshotafter=snapshotafter, logcontent=logcontent, ccontent=ccontent, problemdir=problemdir)
    
    
    if "fd_pread" in problemdir:
        judge_fd_pread(items=items, runtime=runtimename, logcontent=logcontent, ccontent=ccontent, problemdir=problemdir)
     
    if "fd_prestat_dir_name" in problemdir:
        judge_fd_prestat_dir_name(items=items, runtime=runtimename, logcontent=logcontent, ccontent=ccontent, problemdir=problemdir)
    
    if "fd_pwrite" in problemdir:
        judge_fd_pwrite(items=items, runtime=runtimename, logcontent=logcontent, snapshotbefore=snapshotbefore, snapshotafter=snapshotafter, ccontent=ccontent, problemdir=problemdir) 
    
    if "fd_read" in problemdir:
        if "fd_readdir" not in problemdir:
            judge_fd_read(items=items, runtime=runtimename, snapshotafter=snapshotafter, snapshotbefore=snapshotbefore, logcontent=logcontent, ccontent=ccontent, problemdir=problemdir)
     
    if "fd_readdir" in problemdir:
        judge_fd_readdir(items=items, file2per=file2per, runtime=runtimename, snapshotbefore=snapshotbefore, logcontent=logcontent, ccontent=ccontent, problemdir=problemdir)
     
    if "fd_renumber" in problemdir:
        judge_fd_renumber(items=items, file2per=file2per, runtime=runtimename, snapshotbefore=snapshotbefore, logcontent=logcontent, ccontent=ccontent, problemdir=problemdir)
   
    if "fd_seek" in problemdir:
        judge_fd_seek(items=items, file2per=file2per, runtime=runtimename, snapshotbefore=snapshotbefore, snapshotafter=snapshotafter, logcontent=logcontent, ccontent=ccontent, problemdir=problemdir)   
    
    if "fd_write" in problemdir:
        judge_fd_write(items=items, file2per=file2per, runtime=runtimename, snapshotbefore=snapshotbefore, snapshotafter=snapshotafter, logcontent=logcontent, ccontent=ccontent, problemdir=problemdir)
    
    if "path_filestat_get" in problemdir:
        judge_path_filestat_get(items=items, runtime=runtimename, logcontent=logcontent, problemdir=problemdir)
    
    if "path_filestat_set_times" in problemdir:
        judge_path_filestat_set_times(items=items, runtime=runtimename, logcontent=logcontent, ccontent=ccontent, problemdir=problemdir)
        

    if "path_link" in problemdir:
        judge_path_link(items=items, runtime=runtimename, logcontent=logcontent, snapshotafter=snapshotafter, problemdir=problemdir)
    
    if "path_open" in problemdir:
        judge_path_open(items=items, runtime=runtimename, file2per=file2per, ccontent=ccontent, logcontent=logcontent, platform=platform, problemdir=problemdir)
    
    if "path_readlink" in problemdir:
        judge_path_readlink(items=items, runtime=runtimename, logcontent=logcontent, problemdir=problemdir)
     
    # if "path_remove_directory" in problemdir:
    #     judge_path_remove_directory(items=items, runtime=runtimename, ccontent=ccontent, logcontent=logcontent, problemdir=problemdir)
    
    if "path_rename" in problemdir:
        judge_path_rename(items=items, runtime=runtimename, ccontent=ccontent, logcontent=logcontent, problemdir=problemdir)
         
    if "path_symlink" in problemdir:
        judge_path_symlink(items=items, runtime=runtimename, ccontent=ccontent, logcontent=logcontent, snapshotafter=snapshotafter, problemdir=problemdir)
           
    if "path_unlink_file" in problemdir:
        judge_path_unlink_file(items=items, runtime=runtimename, ccontent=ccontent, logcontent=logcontent, problemdir=problemdir)
       
         
    return items
        