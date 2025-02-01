
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

void fd_pwrite_00119_nEEKq(int fd) {
    printf("Enter function fd_pwrite_00119_nEEKq\n");
    off_t size = lseek(fd, 0, SEEK_END); 
    printf("Current file size before: %ld\n", size);

    
    struct iovec iov[1];
    iov[0].iov_base = "LIYTKYtfgm0yh6fKfgi5V0BFOMpDzQsHOL5rSWXvTZcHRgeoERhAtn24pEaujnztRHCn7C6eLiy1M30HuaHpzWR8i6leLM4cx89sgpwvOURPwexkk";
    iov[0].iov_len = 113;
    
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
    int fd = get_fd("EXAMPLEFILE", O_RDWR | O_APPEND);
    if (fd == -1) {
        return 1;
    }
    
    fd_pwrite_00119_nEEKq(fd);
    
    closebyfd(fd);
    
    return 0;
}
