
#include <stdio.h>
#include <time.h>

void clock_time_get_obtwo() {
    printf("Enter function clock_time_get_obtwo\n");

    struct timespec ts;
    if(clock_gettime(CLOCK_REALTIME, &ts) == -1) {
        perror("clock_gettime error");
        return;
    }

    printf("Current time: %ld seconds, %ld nanoseconds\n", ts.tv_sec, ts.tv_nsec);
}

int main() {
    printf("Enter function main\n");

    clock_time_get_obtwo();

    return 0;
}
