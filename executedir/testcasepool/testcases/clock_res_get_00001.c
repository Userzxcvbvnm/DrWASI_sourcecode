
#include <stdio.h>
#include <time.h>

void clock_res_get_00001_FzYMB() {
    printf("Enter function clock_res_get_00001_FzYMB\n");

    struct timespec res;
    clock_getres(CLOCK_REALTIME, &res);

    printf("Clock resolution: %ld.%09ld seconds\n", res.tv_sec, res.tv_nsec);
}

int main() {
    printf("Enter function main\n");

    clock_res_get_00001_FzYMB();

    return 0;
}
