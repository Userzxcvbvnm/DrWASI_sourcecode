
#include <stdio.h>
#include <time.h>

void clock_time_get_00002_obtwo() {
    printf("Enter function clock_time_get_00002_obtwo\n");

    struct timespec ts;
    if(clock_gettime(CLOCK_MONOTONIC, &ts) == -1) {
        perror("clock_gettime error");
        return;
    }

    printf("Current time: %lld seconds, %ld nanoseconds\n", ts.tv_sec, ts.tv_nsec);
}

int main() {
    printf("Enter function main\n");

    clock_time_get_00002_obtwo();

    return 0;
}
