
#include <stdio.h>
#include <dirent.h>
#include <fcntl.h>
#include <unistd.h>


#include <errno.h>
#include <string.h>

void fd_readdir_00001_sYQM0(int fd) {
    printf("Enter function fd_readdir_00001_sYQM0\n");

    DIR *directory;
    struct dirent *entry;
    directory = fdopendir(fd);

    if (directory == NULL) {
        printf("fdopendir failed.\n");
        return;
    }

    while ((entry = readdir(directory)) != NULL) {
        printf("Get dir content:%s\n", entry->d_name);
    }

    printf("Print dir content finished.\n");
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
    int fd = get_fd("EXAMPLEDIR", O_RDONLY | O_DIRECTORY);
    if (fd == -1) {
        return 1;
    }

    fd_readdir_00001_sYQM0(fd);

    closebyfd(fd);

    return 0;
}
