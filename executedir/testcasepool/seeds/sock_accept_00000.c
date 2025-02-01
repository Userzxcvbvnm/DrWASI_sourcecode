
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <fcntl.h>

int get_fd(const char *filename, int flags) {
    int fd = open(filename, flags);
    return fd;
}

int sock_accept_3fmOr() {
    struct sockaddr_in address;
    // code here
}

int main() {
    int fd = get_fd("EXAMPLEFILE", O_RDONLY);
    // code here
    return 0;
}
