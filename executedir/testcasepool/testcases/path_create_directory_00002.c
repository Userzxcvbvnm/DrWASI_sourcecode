
#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <stdlib.h>


void print_path_permissions(const char *path) {
    struct stat path_stat;
    if (stat(path, &path_stat) < 0) {
        perror("Get directory state failed.");
        return;
    }
    mode_t permissions = path_stat.st_mode & (S_IRWXU | S_IRWXG | S_IRWXO);
    printf("Directory '%s' 's permission: %o\n", path, permissions);
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


void path_create_directory_00002_6iirB(int fd) {
    printf("Enter function path_create_directory_00002_6iirB\n");

    // Create a directory using mkdirat function
    int result = 0;
    if (mkdirat(fd, "NEWDIR", 0100) == -1) {
        printf("Failed to create directory.\n");
        result = -1;
    } else {
        printf("Directory created successfully.\n");
    }


    
    print_path_permissions("EXAMPLEDIR/NEWDIR"); 
    closebyfd(fd);


    // Check if an error occurred during directory creation
    if (result == -1) {
        return;
    }
}

int main() {
    printf("Enter function main\n");

    // Get file descriptor
    int fd = get_fd("EXAMPLEDIR", O_RDONLY | O_DIRECTORY);
    if (fd == -1) {
        return -1;
    }


    // Call path_create_directory_00002_6iirB function
    path_create_directory_00002_6iirB(fd);
    
    return 0;
}
