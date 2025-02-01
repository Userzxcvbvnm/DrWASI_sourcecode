
#include <stdio.h>
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

void fd_prestat_dir_name_00006_n0A5E(int fd) {
    printf("Enter function fd_prestat_dir_name_00006_n0A5E\n");
    
    int access_mode = fcntl(fd, F_GETFL) & O_ACCMODE;
    
    printf("c %d\n", access_mode);
    
    if (access_mode == O_RDONLY) {
        printf("Read-only access\n");
    }
    if (access_mode == O_WRONLY) {
        printf("Write-only access\n");
    }
    if (access_mode == O_RDWR) {
        printf("Read and write access\n");
    }
}

int main() {
    int fd = get_fd("EXAMPLEFILE", O_WRONLY | O_TRUNC);
    
    if (fd == -1) {
        return -1;
    }
    
    fd_prestat_dir_name_00006_n0A5E(fd);
    
    closebyfd(fd);
    
    return 0;
}
