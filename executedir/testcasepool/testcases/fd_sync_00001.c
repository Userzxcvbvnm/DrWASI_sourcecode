
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

void fd_sync_00001_5DByZ(int fd) {
    printf("Enter function fd_sync_00001_5DByZ\n");
    if (fd < 0) {
        printf("Invalid file descriptor\n");
        return;
    }

    if (fsync(fd) == -1) {
        printf("Failed to synchronize data and metadata to disk\n");
    } else {
        printf("Data and metadata synchronized to disk successfully\n");
    }
}

int main() {
    

    int fd = get_fd("EXAMPLEFILE", O_RDONLY);
    if (fd == -1) {
        return 1;
    }

    fd_sync_00001_5DByZ(fd);

    closebyfd(fd);

    return 0;
}
