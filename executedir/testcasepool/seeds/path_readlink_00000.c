
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>

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

void path_readlink_xYCLW(int fd) {
    printf("Enter function path_readlink_xYCLW\n");

    char link[100];
    ssize_t numBytes = readlinkat(fd, ".", link, 100);

    if (numBytes == -1) {
        perror("readlinkat");
    } else {
        link[numBytes] = '\0';
        printf("Symbolic link contents: %s\n", link);
    }
}

int main() {
    int fd = get_fd("EXAMPLEFILE", O_RDONLY);
    if (fd == -1) {
        return -1;
    }

    path_readlink_xYCLW(fd);

    closebyfd(fd);

    return 0;
}
