
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

void fd_pwrite_00043_nEEKq(int fd) {
    printf("Enter function fd_pwrite_00043_nEEKq\n");
    off_t size = lseek(fd, 0, SEEK_END); 
    printf("Current file size before: %ld\n", size);

    
    struct iovec iov[1];
    iov[0].iov_base = "Olbg2kSOTsMtsUg8R4j2wjT4rG7x2Q8x7iHujrLe50eTFeDrM7UZwoMOJrRRVJg2uR9WFvC2O0hjJypnkTmrz05UaXBkMRCQxqFaiZfx5ztsMYYV6SQkyPlGiYHMheP3qaLW27YW4a1RfBuODHlClC4OUc6LfYbqGUzvV9TpKUrIyXkLvqKu8gMclrNY9RQvtQYf81Mx0BDvmkowARvja3zlKUOLgRRYP6OoFgT9rQ5svL2dVQxO8fK7wEQJ8kGzmggen8nZHVfwJhQXyD84iDycwRkOtsCzEwNN3xnlPGYR";
    iov[0].iov_len = 300;
    
    off_t offset = lseek(fd, 0, SEEK_CUR);
    if (offset == -1) {
        printf("Failed to get current offset\n");
        return;
    }
    
    ssize_t bytes_written = pwritev(fd, iov, 1, 0);
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
    
    fd_pwrite_00043_nEEKq(fd);
    
    closebyfd(fd);
    
    return 0;
}
