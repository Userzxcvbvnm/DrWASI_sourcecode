
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

void fd_pwrite_00122_nEEKq(int fd) {
    printf("Enter function fd_pwrite_00122_nEEKq\n");
    off_t size = lseek(fd, 0, SEEK_END); 
    printf("Current file size before: %ld\n", size);

    
    struct iovec iov[1];
    iov[0].iov_base = "owMuQqGBIXlmYY4w2gCu4QziM6UsRJjs5pUTLxVmelJCnPPbDQPAV6t5LtBlzxVv3csp57gQjkJUS337SPR4Gm48QKttzakflU9IBLZCxZB3Kscc12wjT8JXafAB7OF2K2YXkKE2W0XyVLer9nOtfxSz2IXjaO5X1YvE54PbWT5oqjsl7CfdZMhIyEns6WlHuVnKWRPuHN0Rx";
    iov[0].iov_len = 205;
    
    off_t offset = lseek(fd, 0, SEEK_CUR);
    if (offset == -1) {
        printf("Failed to get current offset\n");
        return;
    }
    
    ssize_t bytes_written = pwritev(fd, iov, 1, 7);
    if (bytes_written == -1) {
        printf("pwritev failed\n");
    } else {
        printf("pwritev successful. %zd bytes written\n", bytes_written);
    }
    size = lseek(fd, 0, SEEK_END); 
    printf("Current file size after: %ld\n", size);

}

int main() {
    int fd = get_fd("EXAMPLEFILE", O_RDONLY);
    if (fd == -1) {
        return 1;
    }
    
    fd_pwrite_00122_nEEKq(fd);
    
    closebyfd(fd);
    
    return 0;
}
