
#include <stdio.h>
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

void fd_seek_00055_fOSeD(int fd) {
    printf("Enter function fd_seek_00055_fOSeD\n");
    
    off_t offset = lseek(fd, 5, SEEK_CUR);
    if (offset == -1) {
        printf("lseek failed\n");
    } else {
        printf("lseek success, new offset is: %ld\n", offset);
    }
}

int main() {
    int fd = get_fd("EXAMPLEFILE", O_RDWR | O_TRUNC | O_CREAT);
    if (fd == -1) {
        return 1;
    }

    fd_seek_00055_fOSeD(fd);

    closebyfd(fd);

    return 0;
}
