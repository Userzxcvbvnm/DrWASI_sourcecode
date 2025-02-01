
#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>
#include <stdlib.h>

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

void path_remove_directory_k8mfw(int fd) {
    printf("Enter function path_remove_directory_k8mfw\n");
    char *path = ".";
    if (unlinkat(fd, path, AT_REMOVEDIR) == 0) {
        printf("Directory removed successfully.\n");
    } else {
        printf("Error removing directory.\n");
        perror("Error removing directory.\n");
    }
}

int main() {
    int fd = get_fd("EXAMPLEDIR", O_RDONLY);
    if (fd == -1) {
        return -1;
    }
    path_remove_directory_k8mfw(fd);
    
    closebyfd(fd);
    return 0;
}
