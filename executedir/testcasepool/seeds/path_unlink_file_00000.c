
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

void path_unlink_file_ggOQt(int fd) {
    printf("Enter function path_unlink_file_ggOQt\n");
    const char* path = "example.txt";
    if (unlinkat(fd, path, 0) == -1) {
        printf("Unlink file failed!\n");
        return;
    }
    printf("File unlinked successfully\n");
}

int main() {
    int fd = get_fd("example.txt", O_RDONLY);
    if (fd == -1) {
        return -1;
    }

    path_unlink_file_ggOQt(fd);

    closebyfd(fd);

    return 0;
}
