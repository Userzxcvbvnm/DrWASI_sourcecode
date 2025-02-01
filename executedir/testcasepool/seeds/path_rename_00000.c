
#include <stdio.h>
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

void path_rename_gApN2(int fd) {
    printf("Enter function path_rename_gApN2\n");
    char old_path[] = "old_file.txt";
    char new_path[] = "new_file.txt";
    
    if(renameat(fd, old_path, fd, new_path) == 0) {
        printf("File or directory renamed successfully.\n");
    } else {
        printf("Error renaming file or directory.\n");
    }
}

int main() {
    int fd = get_fd("EXAMPLEFILE", O_RDONLY);
    if (fd == -1) {
        return -1;
    }
    
    path_rename_gApN2(fd);
    
    closebyfd(fd);
    
    return 0;
}
