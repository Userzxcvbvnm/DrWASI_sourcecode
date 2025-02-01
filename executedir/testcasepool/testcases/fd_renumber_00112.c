#include <stdio.h>
#include <stdlib.h>
#include <wasi/api.h>
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

int fd_renumber_00112_1x8fd(int fd) {
    printf("Enter function fd_renumber_00112_1x8fd.\n");

    int new_fd = get_fd("EXAMPLEFILE2", O_WRONLY); 
    __wasi_errno_t result = __wasi_fd_renumber(fd, new_fd);

    if (result != 0) {
        printf("Error %d while renumbering file descriptors.\n", result);
        return result;
    } else {
        printf("Successful file descriptors %d.\n", result);
        printf("Leave fd_renumber_00112.\n");
        closebyfd(new_fd);
        return result;
    }
    
}


int main() {
    int fd = get_fd("EXAMPLEFILE", O_RDWR | O_TRUNC | O_CREAT); // Change the filename as needed
    if (fd == -1) {
        return -1;
    }

    fd_renumber_00112_1x8fd(fd);

    

    return 0;
}
