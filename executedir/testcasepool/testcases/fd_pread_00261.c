
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

void fd_pread_00261_iTNDD(int fd) {
    printf("Enter function fd_pread_00261_iTNDD\n");

    __wasi_filestat_t filestat;
    __wasi_errno_t result = __wasi_fd_filestat_get(fd, &filestat);
    if (result != 0) {
        printf("Error %d while getting file stat\n", result);
    } else{
        printf("File Size: %llu bytes\n", filestat.size);
    }


    struct iovec iov;
    char buffer[239];

    iov.iov_base = buffer;
    iov.iov_len = sizeof(buffer);

    ssize_t bytes_read = preadv(fd, &iov, 1, 48);

    if (bytes_read == -1) {
        printf("preadv error.\n");
        return;
    }

    printf("preadv successfully read %zd bytes\n", bytes_read);
}

int main() {
    int fd = get_fd("EXAMPLEFILE", O_WRONLY | O_APPEND);
    if (fd == -1) {
        return 1;
    }

    fd_pread_00261_iTNDD(fd);

    closebyfd(fd);
    return 0;
}
