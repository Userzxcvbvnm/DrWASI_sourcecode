
#include <stdio.h>
#include <stdlib.h>
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

void fd_filestat_set_times_00007_A2Xjs(int fd) {
    printf("Enter function fd_filestat_set_times_00007_A2Xjs\n");

    struct timespec times[2] = {{946684800, 0}, {946684800, 0}}; // 2000-01-01 00:00:00 UTC

    if (futimens(fd, times) == -1) {
        printf("Adjust timestamps failed!\n");
    } else {
        printf("Adjust timestamps successful!\n");
    }

    // Get file status
    struct stat fileStat;
    if (fstat(fd, &fileStat) == -1) {
        printf("Get file status failed!\n");
        return;
    }

    printf("Timestamps of the file:\n");
    printf("Last access: %ld\n", fileStat.st_atim.tv_sec);
    printf("Last modified: %ld\n", fileStat.st_mtim.tv_sec);
}

int main() {
    int fd = get_fd("EXAMPLEFILE", O_RDWR | O_TRUNC); // Assume EXAMPLEFILE is the file to be operated on
    if (fd == -1) {
        return -1;
    }

    fd_filestat_set_times_00007_A2Xjs(fd);

    closebyfd(fd);

    return 0;
}
