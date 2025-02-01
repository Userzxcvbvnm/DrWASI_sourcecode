#include <stdio.h>
#include <stdlib.h>
#include <wasi/api.h>
#include <fcntl.h>
#include <unistd.h>

int get_fd(const char *filename, int flags) {
    int fd = open(filename, flags);
    
    if (fd == -1) {
        printf("Get file descriptor of file %s failed!\n", filename);
        return -1;
    } else {
        printf("Get file descriptor of file %s succeed!\n", filename);
        return fd;
    }
}


void closebyfd(int fd) {
    if (close(fd) == -1) {
        printf("Close the file %d by descriptor failed!\n", fd);
    }
}


void print_rights(__wasi_rights_t rights) {
    if (rights & __WASI_RIGHTS_FD_READ)
        printf("__WASI_RIGHTS_FD_READ\n");
    if (rights & __WASI_RIGHTS_FD_SEEK)
        printf("__WASI_RIGHTS_FD_SEEK\n");
    if (rights & __WASI_RIGHTS_FD_FDSTAT_SET_FLAGS)
        printf("__WASI_RIGHTS_FD_FDSTAT_SET_FLAGS\n");
    if (rights & __WASI_RIGHTS_FD_SYNC)
        printf("__WASI_RIGHTS_FD_SYNC\n");
    if (rights & __WASI_RIGHTS_FD_TELL)
        printf("__WASI_RIGHTS_FD_TELL\n");
    if (rights & __WASI_RIGHTS_FD_WRITE )
        printf("__WASI_RIGHTS_FD_WRITE \n");
    if (rights & __WASI_RIGHTS_FD_ADVISE )
        printf("__WASI_RIGHTS_FD_ADVISE \n");
    if (rights & __WASI_RIGHTS_FD_ALLOCATE )
        printf("__WASI_RIGHTS_FD_ALLOCATE \n");
    if (rights & __WASI_RIGHTS_PATH_CREATE_DIRECTORY )
        printf("__WASI_RIGHTS_PATH_CREATE_DIRECTORY \n");
    if (rights & __WASI_RIGHTS_PATH_CREATE_FILE )
        printf("__WASI_RIGHTS_PATH_CREATE_FILE \n");   
    if (rights & __WASI_RIGHTS_PATH_LINK_SOURCE )
        printf("__WASI_RIGHTS_PATH_LINK_SOURCE \n");   
    if (rights & __WASI_RIGHTS_PATH_LINK_TARGET )
        printf("__WASI_RIGHTS_PATH_LINK_TARGET \n");   
    if (rights & __WASI_RIGHTS_PATH_OPEN )
        printf("__WASI_RIGHTS_PATH_OPEN \n");  
    if (rights & __WASI_RIGHTS_FD_READDIR )
        printf("__WASI_RIGHTS_FD_READDIR \n");  
    if (rights & __WASI_RIGHTS_PATH_READLINK )
        printf("__WASI_RIGHTS_PATH_READLINK \n");  
    if (rights & __WASI_RIGHTS_PATH_RENAME_SOURCE )
        printf("__WASI_RIGHTS_PATH_RENAME_SOURCE \n"); 
    if (rights & __WASI_RIGHTS_PATH_RENAME_TARGET )
        printf("__WASI_RIGHTS_PATH_RENAME_TARGET \n"); 
    if (rights & __WASI_RIGHTS_PATH_FILESTAT_GET )
        printf("__WASI_RIGHTS_PATH_FILESTAT_GET \n"); 
    if (rights & __WASI_RIGHTS_PATH_FILESTAT_SET_SIZE )
        printf("__WASI_RIGHTS_PATH_FILESTAT_SET_SIZE \n"); 
    if (rights & __WASI_RIGHTS_PATH_FILESTAT_SET_TIMES )
        printf("__WASI_RIGHTS_PATH_FILESTAT_SET_TIMES \n"); 
    if (rights & __WASI_RIGHTS_FD_FILESTAT_GET )
        printf("__WASI_RIGHTS_FD_FILESTAT_GET \n"); 
    if (rights & __WASI_RIGHTS_FD_FILESTAT_SET_SIZE )
        printf("__WASI_RIGHTS_FD_FILESTAT_SET_SIZE \n"); 
    if (rights & __WASI_RIGHTS_FD_FILESTAT_SET_TIMES)
        printf("__WASI_RIGHTS_FD_FILESTAT_SET_TIMES \n");
    if (rights & __WASI_RIGHTS_PATH_SYMLINK)
        printf("__WASI_RIGHTS_PATH_SYMLINK \n");
    if (rights & __WASI_RIGHTS_PATH_REMOVE_DIRECTORY)
        printf("__WASI_RIGHTS_PATH_REMOVE_DIRECTORY \n");
    if (rights & __WASI_RIGHTS_PATH_UNLINK_FILE)
        printf("__WASI_RIGHTS_PATH_UNLINK_FILE \n");
    if (rights & __WASI_RIGHTS_POLL_FD_READWRITE)
        printf("__WASI_RIGHTS_POLL_FD_READWRITE \n");
    if (rights & __WASI_RIGHTS_SOCK_SHUTDOWN)
        printf("__WASI_RIGHTS_SOCK_SHUTDOWN \n");
    if (rights & __WASI_RIGHTS_SOCK_ACCEPT)
        printf("__WASI_RIGHTS_SOCK_ACCEPT \n");
    printf("\n");
}


int fd_fdstat_set_rights_00279_7we45(int fd) {
    printf("Enter function fd_fdstat_set_rights_00279_7we45\n");

    __wasi_rights_t new_rights = __WASI_RIGHTS_PATH_UNLINK_FILE;

    __wasi_fdstat_t fdstat;
    if (__wasi_fd_fdstat_get(fd, &fdstat) != 0) {
        printf("Failed to get fd rights.\n");
        return 1;
    }
    printf("Current file rights: \n");
    print_rights(fdstat.fs_rights_base);
    
    if (__wasi_fd_fdstat_set_rights(fd, new_rights, 0) != 0) {
        printf("Failed to set fd rights.\n");
        return 1;
    }
    printf("New file rights: \n");
    print_rights(new_rights);
    return 0;
}


int main() {
    int fd = get_fd("EXAMPLEFILE", O_WRONLY | O_CREAT); // Change the filename as needed
    if (fd == -1) {
        return -1;
    }

    fd_fdstat_set_rights_00279_7we45(fd);

    closebyfd(fd);

    return 0;
}
