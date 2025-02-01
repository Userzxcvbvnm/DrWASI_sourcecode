
#include <stdio.h>
#include <stdlib.h>
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

void fd_fdstat_set_flags_00016_ZJtyU(int fd) {
    printf("Enter function fd_fdstat_set_flags_00016_ZJtyU\n");

    int flags = fcntl(fd, F_GETFL);
    flags = flags | O_NONBLOCK;
    
    if (fcntl(fd, F_SETFL, flags) == -1) {
        printf("Setting flags failed!\n");
    } else {
        printf("Setting flags succeed!\n");
    }
}


    
void print_flags(int fd){
    int flags1 = fcntl(fd, F_GETFL);
    int access_mode1 = flags1 & O_ACCMODE;
    if (access_mode1 == O_RDONLY) {
        printf("Access mode: Read Only\n");
    }
    if (access_mode1 == O_WRONLY) {
        printf("Access mode: Write Only\n");
    }
    if (access_mode1 == O_RDWR) {
        printf("Access mode: Read/Write\n");
    }
    
    
    if (flags1 & O_APPEND) {
        printf("Access mode: O_APPEND\n");
    }
    
    if (flags1 & O_NONBLOCK) {
        printf("Access mode: Non-blocking\n");
    }    
}
    
int main() {
    
    int fd = get_fd("EXAMPLEFILE", O_RDWR | O_CREAT);

    if (fd == -1) {
        return 1;
    }

    
    print_flags(fd);
    fd_fdstat_set_flags_00016_ZJtyU(fd);
    printf("After setting flags\n");
    print_flags(fd);


    closebyfd(fd);

    return 0;
}
