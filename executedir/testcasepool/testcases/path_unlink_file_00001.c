
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

void path_unlink_file_00001_ggOQt() {
    printf("Enter function path_unlink_file_00001_ggOQt\n");
    
    if (unlinkat(AT_FDCWD, "EXAMPLEFILE", 0) == -1) {
        printf("Unlink file failed!\n");
        return;
    }
    printf("File unlinked successfully\n");
}

int main() {
    

    path_unlink_file_00001_ggOQt();

    

    return 0;
}
