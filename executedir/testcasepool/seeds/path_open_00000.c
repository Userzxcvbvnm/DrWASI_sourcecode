
#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>
#include <errno.h>
#include <string.h>

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

void path_open_UuZtc(int fd) {
    printf("Enter function path_open_UuZtc\n");
    const char *path = "example.txt";
    int file_fd = openat(fd, path, O_RDONLY);
    if (file_fd == -1) {
        printf("Open file or directory failed: %s\n", strerror(errno));
    } else {
        printf("Open file or directory succeeded!\n");
    }
}

int main() {
    printf("Enter main function\n");

    int fd = get_fd("EXAMPLEDIR", O_RDONLY);
    if (fd == -1) {
        return 1;
    }

    path_open_UuZtc(fd);

    closebyfd(fd);

    return 0;
}
