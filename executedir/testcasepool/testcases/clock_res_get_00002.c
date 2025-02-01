
#include <stdio.h>
#include <time.h>

void clock_res_get_00002_FzYMB() {
    printf("Enter function clock_res_get_00002_FzYMB\n");

    struct timespec res;
    clock_getres(CLOCK_MONOTONIC, &res);

    printf("Clock resolution: %ld.%09ld seconds\n", res.tv_sec, res.tv_nsec);
}

int main() {
    printf("Enter function main\n");

    clock_res_get_00002_FzYMB();

    return 0;
}
