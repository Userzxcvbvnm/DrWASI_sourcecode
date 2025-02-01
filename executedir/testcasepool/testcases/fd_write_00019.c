
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

void fd_write_00019_WOtrt(int fd) {
    printf("Enter function fd_write_00019_WOtrt\n");
    
    
    struct iovec iov[2];
    iov[0].iov_base = "f";
    iov[0].iov_len = 1;
    iov[1].iov_base = "f";
    iov[1].iov_len = 1;

    off_t offset = lseek(fd, 0, SEEK_CUR);
    printf("File current offset before write: %lld\n", (long long)offset);
    ssize_t numBytes = writev(fd, iov, 2);
    offset = lseek(fd, 0, SEEK_CUR);
    printf("File current offset after write: %lld\n", (long long)offset);


    if (numBytes == -1) {
        printf("Write to file descriptor failed!\n");
    } else {
        printf("Write to file descriptor successful. Number of bytes written: %zd\n", numBytes);
    }
}

int main() {
    int fd = get_fd("EXAMPLEFILE", O_WRONLY | O_APPEND);
    if (fd == -1) {
        return -1;
    }

    fd_write_00019_WOtrt(fd);

    closebyfd(fd);

    return 0;
}
