
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

void fd_write_00051_WOtrt(int fd) {
    printf("Enter function fd_write_00051_WOtrt\n");
    
    
    struct iovec iov[2];
    iov[0].iov_base = "z5y7Lnj6mrnpJkMm0spJhtliCs3TUHQxAdfxqrrsG5AhDZ69NwihP1LGLjYCrToNmXG65pzbYkPvL8RmkXr6wiL6reQqmHKCxuL8m1Rzu6li9xmmP0nfT83K91Q0Mr9AjvwnBz5j1KVicSSs7KhkJmPWfrsCsMzcIC1kY6tXJ8yhOxWYJ1LCOoTcm5eHQYNrWdyqtalGcWsHwH29ars7WV1ZtNBliEU1Hp1DbP9ZFO3EkrgIqBDF1wSgnUHwvcVIrK82RMk3PsvdQaI6Ai0NxNY5AIb1Oqs2iLx1LusEkPHwSgIKD5tbLOBYEDVXioV3ZmkGXNeVdPBG5phwgwCXIyhO3hN4BVRyKIhsDnisG6JiWiUDutKB9kXWbqFCSZ5CYpuNwgRQHzKwkSve";
    iov[0].iov_len = 400;
    iov[1].iov_base = "z5y7Lnj6mrnpJkMm0spJhtliCs3TUHQxAdfxqrrsG5AhDZ69NwihP1LGLjYCrToNmXG65pzbYkPvL8RmkXr6wiL6reQqmHKCxuL8m1Rzu6li9xmmP0nfT83K91Q0Mr9AjvwnBz5j1KVicSSs7KhkJmPWfrsCsMzcIC1kY6tXJ8yhOxWYJ1LCOoTcm5eHQYNrWdyqtalGcWsHwH29ars7WV1ZtNBliEU1Hp1DbP9ZFO3EkrgIqBDF1wSgnUHwvcVIrK82RMk3PsvdQaI6Ai0NxNY5AIb1Oqs2iLx1LusEkPHwSgIKD5tbLOBYEDVXioV3ZmkGXNeVdPBG5phwgwCXIyhO3hN4BVRyKIhsDnisG6JiWiUDutKB9kXWbqFCSZ5CYpuNwgRQHzKwkSve";
    iov[1].iov_len = 400;

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
    int fd = get_fd("EXAMPLEFILE", O_RDWR | O_TRUNC);
    if (fd == -1) {
        return -1;
    }

    fd_write_00051_WOtrt(fd);

    closebyfd(fd);

    return 0;
}
