
#include <stdio.h>
#include <stdlib.h>
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

void fd_fdstat_set_flags_ZJtyU(int fd) {
    printf("Enter function fd_fdstat_set_flags_ZJtyU\n");

    int flags = fcntl(fd, F_GETFL);
    flags = flags | O_APPEND;
    
    if (fcntl(fd, F_SETFL, flags) == -1) {
        printf("Setting flags failed!\n", fd);
    } else {
        printf("Setting flags succeed!\n", fd);
    }
}

int main() {
    int fd = get_fd("EXAMPLEFILE", O_RDONLY);

    if (fd == -1) {
        return 1;
    }

    fd_fdstat_set_flags_ZJtyU(fd);

    closebyfd(fd);

    return 0;
}
