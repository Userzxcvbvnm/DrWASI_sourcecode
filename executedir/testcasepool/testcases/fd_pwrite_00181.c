
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

void fd_pwrite_00181_nEEKq(int fd) {
    printf("Enter function fd_pwrite_00181_nEEKq\n");
    off_t size = lseek(fd, 0, SEEK_END); 
    printf("Current file size before: %ld\n", size);

    
    struct iovec iov[1];
    iov[0].iov_base = "0cfA5X6NhO4Earq4v5oBb9mnhkv9eBb1laHyt4S0Nux7DblNE4ExGS5NX8SGzwULYkc2io4Xqzb9aokvriyfprKTzYyg34aBC7UjuSlqMwylfzn3rhQmVssGYrjtMInQT8oczXeB4VpTQf5RUA1pYFbZktI5BPfGlWOUnHWG0XxGwk5SvUzEm8TeN4aEMjyWtcLiupobThnOnaYUo9eG4k1yGuFY2pxVlrb6UkgIL3KCcfD1mTsNftKJ29RxNztYHGdLaezhkz5nLYbr3Im6SpryUvRC536Y7lybCW2LhSZg0jWsav5uzsYGvl3UFXG";
    iov[0].iov_len = 319;
    
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
    int fd = get_fd("EXAMPLEFILE", O_RDWR | O_CREAT);
    if (fd == -1) {
        return 1;
    }
    
    fd_pwrite_00181_nEEKq(fd);
    
    closebyfd(fd);
    
    return 0;
}
