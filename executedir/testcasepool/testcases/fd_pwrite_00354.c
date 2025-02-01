
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

void fd_pwrite_00354_nEEKq(int fd) {
    printf("Enter function fd_pwrite_00354_nEEKq\n");
    off_t size = lseek(fd, 0, SEEK_END); 
    printf("Current file size before: %ld\n", size);

    
    struct iovec iov[1];
    iov[0].iov_base = "O4HeBWsE6jMbRH3N8WEmGlfJziIyXJdwv5GDL8QrpwbQwr0YD0ZPRGmgULDO8BQuwzO2bYLIDiZYtRgKmU0qpPBFI6lvlS2SwvPPm3gg71vK4yuVEG6AISoSMrfKiaPr5KSL9B0w9RG3KCLxXr5jnWFv2oWa5OD1cblG5hSUC6iLwQnkWRecsVplOgLEPQnqS9CkXILbOwZXoKC4tYUOMi1inPFSyJMCq0oXoSAdWySnF0RmpP0TwGhmQQy3vKvZ6sfuPfN2KFlBA2drkrKiB3gGZffjL15JysYoRSbhxE4yBIkwrRVWgg2095L0P8FIDrLpMaqTJV9j";
    iov[0].iov_len = 332;
    
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
    int fd = get_fd("EXAMPLEFILE", O_WRONLY);
    if (fd == -1) {
        return 1;
    }
    
    fd_pwrite_00354_nEEKq(fd);
    
    closebyfd(fd);
    
    return 0;
}
