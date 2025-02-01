
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/uio.h>
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

void fd_write_WOtrt(int fd) {
    printf("Enter function fd_write_WOtrt\n");
    
    char *str1 = "Hello, ";
    char *str2 = "World!";
    struct iovec iov[2];
    iov[0].iov_base = str1;
    iov[0].iov_len = strlen(str1);
    iov[1].iov_base = str2;
    iov[1].iov_len = strlen(str2);

    ssize_t numBytes = writev(fd, iov, 2);

    if (numBytes == -1) {
        printf("Write to file descriptor failed!\n");
    } else {
        printf("Write to file descriptor successful. Number of bytes written: %zd\n", numBytes);
    }
}

int main() {
    int fd = get_fd("EXAMPLEFILE", O_WRONLY);
    if (fd == -1) {
        return -1;
    }

    fd_write_WOtrt(fd);

    closebyfd(fd);

    return 0;
}
