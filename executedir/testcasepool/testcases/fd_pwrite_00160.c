
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

void fd_pwrite_00160_nEEKq(int fd) {
    printf("Enter function fd_pwrite_00160_nEEKq\n");
    off_t size = lseek(fd, 0, SEEK_END); 
    printf("Current file size before: %ld\n", size);

    
    struct iovec iov[1];
    iov[0].iov_base = "BHLJdsMzSNUATaKQE1nfCNMGjd84HsHAWyCyU1Pdwl3P7smGtLIhCMOlM5gGUEpO4QGZj80iGTtDtRB8PwVY7BKgkQyfaSvFNGbQMpNyOpNZ0rLH5bZmNmYhhNSkPWBo6syl8Sm7ADoUOUt2kKY5BrrTsUOchhvfWKw5SHwWZDUEBzx4dvsoM4TBNR5mrWt626Hv754CrULfCXxQoHLeRnBn6BLzJJswXl8ATeFUSUDBakmWGWi47BXpUQzIKYrnmqTk6pqDl7HHd74k0WWQXiPfLwUeNxKMy2Qt8xUr36K51MMW8khyT3svYeKLr2kXGCbUeNa3PQggI6esDYm3Y9PUzzNai5cUYT18F7MM4XyRzkA9usLTk39V0rB4b4nMKYkefYZMmGuvVPTsMQ";
    iov[0].iov_len = 402;
    
    off_t offset = lseek(fd, 0, SEEK_CUR);
    if (offset == -1) {
        printf("Failed to get current offset\n");
        return;
    }
    
    ssize_t bytes_written = pwritev(fd, iov, 1, 45);
    if (bytes_written == -1) {
        printf("pwritev failed\n");
    } else {
        printf("pwritev successful. %zd bytes written\n", bytes_written);
    }
    size = lseek(fd, 0, SEEK_END); 
    printf("Current file size after: %ld\n", size);

}

int main() {
    int fd = get_fd("EXAMPLEFILE", O_WRONLY | O_TRUNC);
    if (fd == -1) {
        return 1;
    }
    
    fd_pwrite_00160_nEEKq(fd);
    
    closebyfd(fd);
    
    return 0;
}
