
#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>
#include <stdlib.h>
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


void path_link_00001_Nan21() {

    printf("Enter function path_link_00001_Nan21\n");
    
    
    
    int result = linkat(AT_FDCWD, "EXAMPLEFILE", AT_FDCWD, "HARDLINKFILE", AT_SYMLINK_FOLLOW);
    
    if (result == -1) {
        printf("linkat failed");
    } else {
        printf("Hard link creation successful\n");
    }

    
}

int main() {
    printf("Enter function main\n");
    
    
    
    
    path_link_00001_Nan21();

    
    
    
    return 0;
}
