
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

void fd_pwrite_00253_nEEKq(int fd) {
    printf("Enter function fd_pwrite_00253_nEEKq\n");
    off_t size = lseek(fd, 0, SEEK_END); 
    printf("Current file size before: %ld\n", size);

    
    struct iovec iov[1];
    iov[0].iov_base = "ruc6DtNxegBeJlZ3mtHCUtJKIJw6syHiaGDkWWbXFyTDlZDQ6Aw4QSc91dEa8JGxr5uLp67YHmV33zK2vPCuhWw5RYIooyZh1CpQww7aGSGN9zN0agyhTQmB3DRWlCL8KXNPvwKkhkZcH3x2pVZwkYv5qatHs99QTim8sL2SLsphI7muABMRT7qAZ6nyuxOSF5JmvyU1ap3LTnpT8EDjoo6UvLoW";
    iov[0].iov_len = 220;
    
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
    int fd = get_fd("EXAMPLEFILE", O_RDWR | O_TRUNC | O_CREAT);
    if (fd == -1) {
        return 1;
    }
    
    fd_pwrite_00253_nEEKq(fd);
    
    closebyfd(fd);
    
    return 0;
}
