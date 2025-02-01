
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

void fd_pwrite_00370_nEEKq(int fd) {
    printf("Enter function fd_pwrite_00370_nEEKq\n");
    off_t size = lseek(fd, 0, SEEK_END); 
    printf("Current file size before: %ld\n", size);

    
    struct iovec iov[1];
    iov[0].iov_base = "vB1S0t71ua9O7vAd1CHojRoQ1fVbFc5gAYFIk6u53M8N2b2O0WlM3nEsamkG0DYlLu0T365ijJ9sBZX8fvZnwqqwYlRJEIgXOnDc44g1gdZ5zvAjuD3gRlv9sKnFZX1KkQeGrEMB4JkYm8lx5IlStxI0Rwa2eBUs2L4APJvk9kPAVokC76fBBhVfU7m1LH75b8wul4c5My6RLOVmtmWlkf9vs1rVyCFqsjskUmOCR1hXYuhXFu6TcEAHcymsX82oicglYP9fY4EayYImzqD6TFlGFNihN4MWkgexvnRa1BEo54ji5oGkgAsCJX6KPZeE7ICbok86lMijas3PZ8L1J4QRSPWQYT9TY";
    iov[0].iov_len = 353;
    
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
    int fd = get_fd("EXAMPLEFILE", O_RDWR | O_TRUNC);
    if (fd == -1) {
        return 1;
    }
    
    fd_pwrite_00370_nEEKq(fd);
    
    closebyfd(fd);
    
    return 0;
}
