
#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>

void fd_advise_00239_mTE15(int fd) {
    printf("Enter function fd_advise_00239_mTE15\n");

    if (posix_fadvise(fd, 115, 21, POSIX_FADV_NORMAL) == 0) {
        printf("posix_fadvise function called successfully\n");
    } else {
        printf("Error: posix_fadvise function failed\n");
    }
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
    int fd = get_fd("EXAMPLEFILE", O_WRONLY | O_APPEND);
    if (fd == -1) {
        return -1;
    }

    fd_advise_00239_mTE15(fd);

    closebyfd(fd);

    return 0;
}
