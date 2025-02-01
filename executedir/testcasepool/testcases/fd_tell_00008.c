
#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>

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

void fd_tell_00008_pFIk0(int fd) {
    printf("Enter function fd_tell_00008_pFIk0\n");
    off_t offset = lseek(fd, 0, SEEK_CUR);
    printf("Current offset of the file descriptor: %ld\n", offset);
}

int main() {
    printf("Enter function main\n");
    
    int fd = get_fd("EXAMPLEFILE", O_WRONLY | O_APPEND);
    
    if(fd == -1) {
        return -1;
    }
    
    fd_tell_00008_pFIk0(fd);
    
    closebyfd(fd);
    
    return 0;
}
