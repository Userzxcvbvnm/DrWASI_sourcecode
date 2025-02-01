
#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>
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

void fd_pread_iTNDD(int fd) {
    printf("Enter function fd_pread_iTNDD\n");

    struct iovec iov;
    char buffer[100];

    iov.iov_base = buffer;
    iov.iov_len = sizeof(buffer);

    ssize_t bytes_read = preadv(fd, &iov, 1, 0);

    if (bytes_read == -1) {
        perror("preadv");
        return;
    }

    printf("preadv successfully read %zd bytes\n", bytes_read);
}

int main() {
    int fd = get_fd("EXAMPLEFILE", O_RDONLY);
    if (fd == -1) {
        return 1;
    }

    fd_pread_iTNDD(fd);

    closebyfd(fd);
    return 0;
}
