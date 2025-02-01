
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>

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

void fd_datasync_00010_TKDa3(int fd) {
    printf("Enter function fd_datasync_00010_TKDa3\n");
    
    if (fdatasync(fd) == -1) {
        printf("Failed to synchronize data to disk\n");
        return;
    }
    
    printf("Data synchronized to disk successfully\n");
}

int main() {
    int fd = get_fd("EXAMPLEFILE", O_WRONLY | O_TRUNC | O_CREAT);
    if (fd == -1) {
        return 1;
    }

    fd_datasync_00010_TKDa3(fd);

    closebyfd(fd);

    return 0;
}
