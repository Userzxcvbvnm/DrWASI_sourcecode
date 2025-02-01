
#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <stdlib.h>


void path_filestat_get_00001_1d3ff(const char *filename) {
    printf("Enter function path_filestat_get_00001_1d3ff\n");

    struct stat file_stat;
    if (stat(filename, &file_stat) == -1) {
        printf("Error getting file status.\n");
        return;
    }

    printf("File Size: %lld bytes\n", (long long)file_stat.st_size);
    printf("File Permissions: %o\n", file_stat.st_mode & 0777);
    printf("File Owner ID: %d\n", file_stat.st_uid);
    printf("File Group ID: %d\n", file_stat.st_gid);
    printf("Last Access Time: %lld\n", (long long)file_stat.st_atime);
    printf("Last Modification Time: %lld\n", (long long)file_stat.st_mtime);
    printf("Last Status Change Time: %lld\n", (long long)file_stat.st_ctime);

    printf("Leave path_filestat_get_00001.\n");
}

int main() {
    printf("Enter function main\n");
    path_filestat_get_00001_1d3ff("EXAMPLEDIR");
    return 0;
}
