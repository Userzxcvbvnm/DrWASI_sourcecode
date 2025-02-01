
#include <stdio.h>
#include <stdlib.h>

void environ_get_00001_0nb6x() {
    printf("Enter function environ_get_00001_0nb6x\n");

    char* env_var = getenv("SOME_ENV_VARIABLE");
    if(env_var != NULL) {
        printf("Value of SOME_ENV_VARIABLE: %s\n", env_var);
    } else {
        printf("SOME_ENV_VARIABLE not found in the environment\n");
    }
}

int main() {
    printf("Enter function main\n");

    environ_get_00001_0nb6x();

    return 0;
}
