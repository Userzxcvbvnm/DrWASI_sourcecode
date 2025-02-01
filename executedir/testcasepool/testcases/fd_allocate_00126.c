
#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>

void print_file_size(int fd){
    struct stat st;
    if (fstat(fd, &st) == -1) {
        printf("Get file size failed.\n");
    } else {
        printf("Get file size: %ld bytes.\n", st.st_size);
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
        printf("Close the file by descriptor failed!\n");
    }
}

void fd_allocate_00126_gxX49(int fd) {
    printf("Enter function fd_allocate_00126_gxX49\n");
    
    off_t offset = 0;
    off_t len = 1024; // 1KB allocation
    int result = posix_fallocate(fd, 10, 372);

    if (result == 0) {
        printf("Space allocation in file successful.\n");
    } else {
        printf("Error allocating space in file.\n");
    }
}

int main() {
    int fd = get_fd("EXAMPLEFILE", O_RDWR | O_CREAT);
    if (fd == -1) {
        return -1; // Return from main if get_fd failed
    }

    print_file_size(fd);
    fd_allocate_00126_gxX49(fd);
    print_file_size(fd);


    closebyfd(fd);

    return 0;
}
