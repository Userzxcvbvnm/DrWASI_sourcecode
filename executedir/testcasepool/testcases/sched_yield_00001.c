
#include <stdio.h>
#include <sched.h>

void sched_yield_00001_rZHC4() {
    printf("Enter function sched_yield_00001_rZHC4\n");

    int ret = sched_yield();
    
    if(ret == 0) {
        printf("sched_yield_00001 returned successfully\n");
    } else {
        printf("sched_yield_00001 failed\n");
    }
}

int main() {
    printf("Enter function main\n");

    sched_yield_00001_rZHC4();

    return 0;
}
