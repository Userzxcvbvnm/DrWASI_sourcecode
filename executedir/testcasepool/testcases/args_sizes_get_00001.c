
#include <stdio.h>
#include <string.h>

void args_sizes_get_00001_EPK8r(int argc, char *argv[]) {
    printf("Enter function args_sizes_get_00001_EPK8r\n");
    
    for (int i = 0; i < argc; i++) {
        printf("Argument %d size: %lu\n", i, strlen(argv[i]));
    }
}

int main(int argc, char *argv[]) {
    printf("Enter function main\n");
    
    args_sizes_get_00001_EPK8r(argc, argv);
    
    return 0;
}
