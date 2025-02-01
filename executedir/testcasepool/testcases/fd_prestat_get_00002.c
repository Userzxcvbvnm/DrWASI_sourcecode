
#include <stdio.h>
#include <unistd.h>
#include <fcntl.h>
#include <sys/stat.h>

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

void fd_prestat_get_00002_jhXOK(int fd) {
    printf("Enter function fd_prestat_get_00002_jhXOK\n");

    struct stat st;
    if (fstat(fd, &st) == -1) {
        printf("Error getting file descriptor info\n");
        return;
    }

    if (S_ISREG(st.st_mode)) {
        printf("File descriptor is for a regular file\n");
    } else if (S_ISDIR(st.st_mode)) {
        printf("File descriptor is for a directory\n");
    } else if (S_ISCHR(st.st_mode)) {
        printf("File descriptor is for a character special file\n");
    } else if (S_ISBLK(st.st_mode)) {
        printf("File descriptor is for a block special file\n");
    } else if (S_ISFIFO(st.st_mode)) {
        printf("File descriptor is for a FIFO special file\n");
    } else if (S_ISSOCK(st.st_mode)) {
        printf("File descriptor is for a socket\n");
    }
}

int main() {
    int fd = get_fd("EXAMPLEFILE", O_WRONLY);
    if (fd == -1) {
        return -1;
    }

    fd_prestat_get_00002_jhXOK(fd);

    closebyfd(fd);

    return 0;
}
