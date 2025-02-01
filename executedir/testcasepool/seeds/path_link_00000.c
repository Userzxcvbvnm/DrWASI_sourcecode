
#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>

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

void path_link_Nan21(int fd) {
    printf("Enter function path_link_Nan21\n");
    
    int dir_fd = get_fd("exampledir", O_RDONLY);
    if (dir_fd == -1) {
        return;
    }
    
    char target_path[] = "path/to/targetfile";
    char link_path[] = "path/to/linkfile";
    
    int result = linkat(dir_fd, target_path, dir_fd, link_path, 0);
    
    if (result == -1) {
        perror("linkat failed");
    } else {
        printf("Hard link creation successful\n");
    }

    closebyfd(dir_fd);
}

int main() {
    printf("Enter function main\n");
    
    int fd = get_fd("examplefile", O_RDONLY);
    if (fd == -1) {
        return 1;
    }
    
    path_link_Nan21(fd);
    
    closebyfd(fd);
    
    return 0;
}
