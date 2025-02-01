
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

void fd_pwrite_00380_nEEKq(int fd) {
    printf("Enter function fd_pwrite_00380_nEEKq\n");
    off_t size = lseek(fd, 0, SEEK_END); 
    printf("Current file size before: %ld\n", size);

    
    struct iovec iov[1];
    iov[0].iov_base = "gXhRfRUYyXR1YFuqg1XOitufy06zPXdFJNDkL1BBr4JHUjeOq0me40CxblOeAUyE3hZhJg29okl64RR5UQabftBOQFGMR7eu0Ft53M79HPlLaemSUhUJUcYEYyv2FsDC1ymA7B7sw5PJjL893JSTyUxEj8O1LTiEVCv5pjqIoVOcym1gUSC4hVKHmUiVU1zXeWWaXpXXmFshM8TqycUm9eDpPtoE6b26XLaW8NnGSCKQHmYQrB10BPz3U2TdM6nmG5fWnVrYKl4ZucsvZMf0Rcxu5T2ymRA2kEY5bAPEKSckUz1Nid30emFPq0PvH8WJkZctSNja4WdR1KKxwrkJ9ycbJjF2292LVXNNNtjnCSUJLBCE3yyVOuXaoFzwihBKSYW5lkXYecqC5dDDWjAFIgShMSkBmKnNO5lqvtrT53o80Idyv";
    iov[0].iov_len = 433;
    
    off_t offset = lseek(fd, 0, SEEK_CUR);
    if (offset == -1) {
        printf("Failed to get current offset\n");
        return;
    }
    
    ssize_t bytes_written = pwritev(fd, iov, 1, 341);
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
    
    fd_pwrite_00380_nEEKq(fd);
    
    closebyfd(fd);
    
    return 0;
}
