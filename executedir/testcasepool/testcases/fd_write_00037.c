
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/uio.h>
#include <fcntl.h>

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

void fd_write_00037_WOtrt(int fd) {
    printf("Enter function fd_write_00037_WOtrt\n");
    
    
    struct iovec iov[2];
    iov[0].iov_base = "doJUQXYtynjE5XK2U3wz74mLiUgvj3KRdXW53cEZlHufWFDE00MaV3wCl2ba0ekJcwY0OqjToempqbPWO6VTrm350ZoJATKaRWDgCrt8sgEYtF6Mqc3L8tFU2Luj5jzOjUa6oGiotIkxURfgq40jY0WICosyaZQ1Ijn5hP6vkqgPgR7U2sFCM8hbAgLNcW4WbmGCtoVG0JGltIwxOk5ybogkIjJKHYYgUMAAGZ4kdAnN7GI8XSmyub7Gx8HCcYdl9GTRhkondsPf1ynAnDSJOzumCvNvaLYiCobGvLI6AsvAoauDXfBF";
    iov[0].iov_len = 308;
    iov[1].iov_base = "doJUQXYtynjE5XK2U3wz74mLiUgvj3KRdXW53cEZlHufWFDE00MaV3wCl2ba0ekJcwY0OqjToempqbPWO6VTrm350ZoJATKaRWDgCrt8sgEYtF6Mqc3L8tFU2Luj5jzOjUa6oGiotIkxURfgq40jY0WICosyaZQ1Ijn5hP6vkqgPgR7U2sFCM8hbAgLNcW4WbmGCtoVG0JGltIwxOk5ybogkIjJKHYYgUMAAGZ4kdAnN7GI8XSmyub7Gx8HCcYdl9GTRhkondsPf1ynAnDSJOzumCvNvaLYiCobGvLI6AsvAoauDXfBF";
    iov[1].iov_len = 308;

    off_t offset = lseek(fd, 0, SEEK_CUR);
    printf("File current offset before write: %lld\n", (long long)offset);
    ssize_t numBytes = writev(fd, iov, 2);
    offset = lseek(fd, 0, SEEK_CUR);
    printf("File current offset after write: %lld\n", (long long)offset);


    if (numBytes == -1) {
        printf("Write to file descriptor failed!\n");
    } else {
        printf("Write to file descriptor successful. Number of bytes written: %zd\n", numBytes);
    }
}

int main() {
    int fd = get_fd("EXAMPLEFILE", O_WRONLY | O_CREAT);
    if (fd == -1) {
        return -1;
    }

    fd_write_00037_WOtrt(fd);

    closebyfd(fd);

    return 0;
}
