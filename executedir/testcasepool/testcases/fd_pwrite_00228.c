
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

void fd_pwrite_00228_nEEKq(int fd) {
    printf("Enter function fd_pwrite_00228_nEEKq\n");
    off_t size = lseek(fd, 0, SEEK_END); 
    printf("Current file size before: %ld\n", size);

    
    struct iovec iov[1];
    iov[0].iov_base = "YOQYyAxtRtB1wLRqI0FwpyxETCxT3HHULW4Z1WRdpTnRU3qTNEUvplaCUdyAwNQAVLn9qjBoSLjt43CW8clWArywq9rKXwir0earRNLfUizFOe32V4HnZCr8DYAvGuKqx4KPB2QFUUKEfAXhYNgHn15whzzdr2eUG2lx7wLdJxcMA9whkAguSLP9AFiGDH0jNfbouLf4iqAEQrUiFxdPNGDWDe9pTAB8P9JeQdAmACih7kHaujblrQnuAWU9UxgBRuYDorGBy3uhAUkKSV1bbJ51O8OSaBG0C29q5UMvBQFl1Osod6xK5BMwt2lsyhZgcQTAnhsD1eMEND5yz2wuhZcPfC21mhHF1Zbqe2eXxE0Q6K2HxP5JNiwJkiTGJ4LTxGy7sNVSI85dlQg5b7YygAgxFWjUMcdhrmqgXXcH0xt4tU7AskEcEj1xLenB3VFJBpUFWRSGXbJ9Sbp";
    iov[0].iov_len = 463;
    
    off_t offset = lseek(fd, 0, SEEK_CUR);
    if (offset == -1) {
        printf("Failed to get current offset\n");
        return;
    }
    
    ssize_t bytes_written = pwritev(fd, iov, 1, 420);
    if (bytes_written == -1) {
        printf("pwritev failed\n");
    } else {
        printf("pwritev successful. %zd bytes written\n", bytes_written);
    }
    size = lseek(fd, 0, SEEK_END); 
    printf("Current file size after: %ld\n", size);

}

int main() {
    int fd = get_fd("EXAMPLEFILE", O_WRONLY | O_APPEND);
    if (fd == -1) {
        return 1;
    }
    
    fd_pwrite_00228_nEEKq(fd);
    
    closebyfd(fd);
    
    return 0;
}
