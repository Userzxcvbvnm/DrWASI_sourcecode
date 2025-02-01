
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

void path_readlink_00001_xYCLW() {
    printf("Enter function path_readlink_00001_xYCLW\n");

    char link[100];
    ssize_t numBytes = readlinkat(AT_FDCWD, "EXAMPLEFILE", link, 100);

    if (numBytes == -1) {
        printf("readlinkat\n");
    } else {
        link[numBytes] = '\0';
        printf("Symbolic link contents: %s\n", link);
    }
}

int main() {
    

    path_readlink_00001_xYCLW();

    

    return 0;
}
