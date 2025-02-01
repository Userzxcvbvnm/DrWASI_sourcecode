
#include <stdio.h>
#include <stdlib.h>
#include <wasi/api.h>

void random_get_00001_k12jl() {
    printf("Enter random_get_00001_k12jl.\n");
    unsigned int random_number;
    __wasi_random_get(&random_number, sizeof(random_number));
    printf("Random number: %u\n", random_number);
    printf("Leave random_get_00001.\n");
    return;
}

int main() {
    printf("Enter function main\n");
    random_get_00001_k12jl();
    
    return 0;
}

