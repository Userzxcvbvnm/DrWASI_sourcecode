
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

void fd_pwrite_00307_nEEKq(int fd) {
    printf("Enter function fd_pwrite_00307_nEEKq\n");
    off_t size = lseek(fd, 0, SEEK_END); 
    printf("Current file size before: %ld\n", size);

    
    struct iovec iov[1];
    iov[0].iov_base = "t5BU4x0bvdM5bJi2GVuhuyWhPeEgH3DHQKVtdHv6IJuC7bn1SiRK4aX3WOlmouA4vIdDsRlG7MjMsYKzPQO5fPY6PMiVV5dA3Kl9ovkFHyN5lmLIi8RhrDDeO5J09iugL5KJMLHfvdxESSKa18Ce0wze1ip6VREmvD6efs1WH4UihzIQUGakSGSjh4kj";
    iov[0].iov_len = 188;
    
    off_t offset = lseek(fd, 0, SEEK_CUR);
    if (offset == -1) {
        printf("Failed to get current offset\n");
        return;
    }
    
    ssize_t bytes_written = pwritev(fd, iov, 1, 470);
    if (bytes_written == -1) {
        printf("pwritev failed\n");
    } else {
        printf("pwritev successful. %zd bytes written\n", bytes_written);
    }
    size = lseek(fd, 0, SEEK_END); 
    printf("Current file size after: %ld\n", size);

}

int main() {
    int fd = get_fd("EXAMPLEFILE", O_WRONLY | O_TRUNC | O_CREAT);
    if (fd == -1) {
        return 1;
    }
    
    fd_pwrite_00307_nEEKq(fd);
    
    closebyfd(fd);
    
    return 0;
}
