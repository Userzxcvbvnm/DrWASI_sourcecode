
#include <stdio.h>
#include <string.h>
#include <fcntl.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/stat.h>

void path_symlink_Hxmt0(int fd) {
    printf("Enter function path_symlink_Hxmt0\n");
    
    char target[] = "example_target";
    char linkpath[] = "example_link";
    
    if (symlinkat(target, fd, linkpath) == -1) {
        perror("symlinkat");
        return;
    }
    
    printf("Symbolic link created successfully\n");
}

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

int main() {
    int fd = get_fd("EXAMPLEDIR", O_RDONLY);
    if (fd == -1) {
        return 1;
    }
    
    path_symlink_Hxmt0(fd);
    
    closebyfd(fd);
    
    return 0;
}
