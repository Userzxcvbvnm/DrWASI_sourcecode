
#include <stdio.h>
#include <string.h>
#include <fcntl.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/stat.h>

void path_symlink_00001_Hxmt0() {
    printf("Enter function path_symlink_00001_Hxmt0\n");
    

    
    if (symlinkat("EXAMPLEFILE", AT_FDCWD, "NEWFILE") == -1) {
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
    
    
    path_symlink_00001_Hxmt0();
    
    
    
    return 0;
}
