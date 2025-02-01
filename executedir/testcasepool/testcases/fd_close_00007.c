
#include <stdio.h>
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


void fd_close_00007_EaPzN(int fd) {
    printf("Enter function fd_close_00007_EaPzN\n");

    if (close(fd) == -1) {
        printf("Close file descriptor failed!\n");
        return;
    }

    printf("File descriptor closed successfully\n");
}

int main() {
    printf("Enter function main\n");

    int fd = get_fd("EXAMPLEFILE", O_RDWR | O_TRUNC);
    if (fd == -1) {
        return -1;
    }

    fd_close_00007_EaPzN(fd);

    

    return 0;
}
