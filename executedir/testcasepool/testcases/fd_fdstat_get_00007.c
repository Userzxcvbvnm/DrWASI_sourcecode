
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

void fd_fdstat_get_00007_yBbmO(int fd) {
    printf("Enter function fd_fdstat_get_00007_yBbmO\n");

    int flags = fcntl(fd, F_GETFL);
    if (flags == -1) {
        printf("Error getting file descriptor flags\n");
        return;
    }

    printf("File descriptor flags: %d\n", flags);

    int access_mode = flags & O_ACCMODE;

    
    if (access_mode == O_RDONLY) {
        printf("Access mode: Read Only\n");
    }
    if (access_mode == O_WRONLY) {
        printf("Access mode: Write Only\n");
    }
    if (access_mode == O_RDWR) {
        printf("Access mode: Read/Write\n");
    }

    if (flags & O_APPEND) {
        printf("Flag: O_APPEND\n");
    }
}

int main() {
    int fd = get_fd("EXAMPLEFILE", O_RDWR | O_TRUNC);
    if (fd == -1) {
        return -1;
    }

    fd_fdstat_get_00007_yBbmO(fd);

    closebyfd(fd);

    return 0;
}
