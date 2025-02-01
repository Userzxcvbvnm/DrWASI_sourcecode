
#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>
#include <sys/stat.h>
#include <sys/types.h>

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


void path_create_directory_6iirB(int fd) {
    printf("Enter function path_create_directory_6iirB\n");

    // Create a directory using mkdirat function
    int result = 0;
    if (mkdirat(fd, "NEWDIR", 0777) == -1) {
        printf("Failed to create directory.\n");
        result = -1;
    } else {
        printf("Directory created successfully.\n");
    }


    closebyfd(fd);

    // Check if an error occurred during directory creation
    if (result == -1) {
        return;
    }
}

int main() {
    printf("Enter function main\n");

    // Get file descriptor
    int fd = get_fd("EXAMPLEDIR", O_RDONLY);
    if (fd == -1) {
        return -1;
    }


    // Call path_create_directory_6iirB function
    path_create_directory_6iirB(fd);
    
    return 0;
}
