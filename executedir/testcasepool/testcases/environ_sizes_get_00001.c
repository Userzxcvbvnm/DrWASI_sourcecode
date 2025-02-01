
#include <stdio.h>
#include <stdlib.h>

void environ_sizes_get_00001_IOW9P() {
    printf("Enter function environ_sizes_get_00001_IOW9P\n");

    extern char **environ;
    int i = 0;
    while (environ[i] != NULL) {
        i++;
    }

    printf("Number of environment variables: %d\n", i);
}

int main() {
    printf("Enter function main\n");

    environ_sizes_get_00001_IOW9P();

    return 0;
}
