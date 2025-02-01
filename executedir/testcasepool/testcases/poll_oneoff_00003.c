
#include <stdio.h>
#include <unistd.h>
#include <sys/poll.h>

void poll_oneoff_00003_RqhLk() {
    printf("Enter function poll_oneoff_00003_RqhLk\n");
    
    struct pollfd fds[1];
    int ret;

    fds[0].fd = STDIN_FILENO;
    fds[0].events = POLLIN;

    printf("Waiting for input...\n");
    ret = poll(fds, 1, 1000);

    if (ret > 0){
        printf("Input received\n");
    } else {
        printf("Error in polling\n");
    }
}

int main() {
    printf("Enter function main\n");
    
    poll_oneoff_00003_RqhLk();

    return 0;
}
