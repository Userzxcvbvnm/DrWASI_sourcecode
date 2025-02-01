
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

void fd_fdstat_get_yBbmO(int fd) {
    printf("Enter function fd_fdstat_get_yBbmO\n");

    int flags = fcntl(fd, F_GETFL);
    if (flags == -1) {
        printf("Error getting file descriptor flags\n");
        return;
    }

    printf("File descriptor flags: %d\n", flags);

    int access_mode = flags & O_ACCMODE;

    switch(access_mode) {
        case O_RDONLY:
            printf("File access mode: O_RDONLY\n");
            break;
        case O_WRONLY:
            printf("File access mode: O_WRONLY\n");
            break;
        case O_RDWR:
            printf("File access mode: O_RDWR\n");
            break;
        case O_NONBLOCK:
            printf("File access mode: O_NONBLOCK\n");
            break;
        case O_SYNC:
            printf("File access mode: O_SYNC\n");
            break;
        case O_DSYNC:
            printf("File access mode: O_DSYNC\n");
            break;
        default:
            printf("File access mode: Unknown\n");
            break;
    }
}

int main() {
    int fd = get_fd("EXAMPLEFILE", O_RDONLY);
    if (fd == -1) {
        return -1;
    }

    fd_fdstat_get_yBbmO(fd);

    closebyfd(fd);

    return 0;
}
