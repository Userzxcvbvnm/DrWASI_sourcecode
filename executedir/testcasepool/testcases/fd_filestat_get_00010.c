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

int fd_filestat_get_00010_1s23e(int fd) {
    printf("Enter function fd_filestat_get_00010_1s23e.\n");

    __wasi_filestat_t filestat;

    __wasi_errno_t result = __wasi_fd_filestat_get(fd, &filestat);

    if (result != 0) {{
        printf("Error %d while getting file stat\n", result);
        return result;
    }}

    // printf("Device ID: %llu bytes\n", filestat.dev);
    // printf("File serial number: %llu bytes\n", filestat.ino);
    printf("File Type: %u\n", filestat.filetype);
    printf("Number of hard links to the file: %llu \n", filestat.nlink);
    printf("File Size: %llu bytes\n", filestat.size);
    // printf("Last data access timestamp: %llu\n", filestat.atim);
    // printf("Last data modification timestamp: %llu\n", filestat.mtim);
    // printf("Last file status change timestamp: %llu\n", filestat.ctim);

    printf("Leaver fd_filestat_get_00010.\n");
    return 0;
}


int main() {
    int fd = get_fd("EXAMPLEFILE", O_WRONLY | O_TRUNC | O_CREAT); // Change the filename as needed
    if (fd == -1) {
        return -1;
    }

    fd_filestat_get_00010_1s23e(fd);

    closebyfd(fd);

    return 0;
}
