
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

void fd_pwrite_00289_nEEKq(int fd) {
    printf("Enter function fd_pwrite_00289_nEEKq\n");
    off_t size = lseek(fd, 0, SEEK_END); 
    printf("Current file size before: %ld\n", size);

    
    struct iovec iov[1];
    iov[0].iov_base = "hzscWmIIlnpg6XogNhYPW02EFtdQkVoIL78XXXqEfLK3x3qPCROfG45Z5IGxy0rEovDw2hWxvxJIK5rLUa0a7jzQvuOGBE2v3vYcrz7zK6Eayjv6ycAWCeyIWuwBNoPGFGiqNl7Su7jjIX5KPnnrWqlX3vwsw0Yh0O5UEPufg6C7oZJ1ldirWQ6P681zcTYVmSJOS0gwP3lbqUyTULD5Etiq4vmu4v9LNNyArCQZbaYgBaWqTH192EhsXgTFUCbOmlwBA9KqOYmtFeaUCcMxn67RR6IwzyPGXC3BGGNZq9dFcTF49hiwGVwn1NxIwOEYKn5VSt2llwvMJ22llFEqLaGqAaaBcvpNGQP7mEB5MXAUwmAAeNmcYkZUM6oQ1KHmtAbZokl0Q1QfUdbL7dwxSN2v8jQWtiz4v396AU9W2M3guhaTW43UaLq8pLZDnqhcFcZqVBRJdre4m";
    iov[0].iov_len = 461;
    
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
    int fd = get_fd("EXAMPLEFILE", O_RDWR);
    if (fd == -1) {
        return 1;
    }
    
    fd_pwrite_00289_nEEKq(fd);
    
    closebyfd(fd);
    
    return 0;
}
