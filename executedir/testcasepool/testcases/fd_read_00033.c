
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>
#include <sys/uio.h>

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

void fd_read_00033_Ep05V(int fd) {
    printf("Enter function fd_read_00033_Ep05V\n");

    char buf1[48];
    char buf2[48];
    struct iovec iov[2];
    ssize_t num_read;

    iov[0].iov_base = buf1;
    iov[0].iov_len = 48;
    iov[1].iov_base = buf2;
    iov[1].iov_len = 48;

    num_read = readv(fd, iov, 2);

    if (num_read == -1) {
        printf("Error reading from file descriptor\n");
    } else {
        printf("Read %ld bytes using readv\n", num_read);
    }
}

int main() {
    int fd = get_fd("EXAMPLEFILE", O_RDWR | O_TRUNC | O_CREAT);
    if (fd == -1) {
        return 1;
    }

    fd_read_00033_Ep05V(fd);

    closebyfd(fd);
    
    return 0;
}
