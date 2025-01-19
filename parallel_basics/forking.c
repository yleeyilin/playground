#include <stdio.h>
#include <unistd.h>

int main(int argc, char *argv[]) {
    char *name = argv[0];
    int child_pid = fork();
    sleep(3);
    if (child_pid == 0) { // child block
        printf("Child of %s is %d\n", name, getpid());
        return 0;
    } else { // parent block
        printf("My child is %d\n", child_pid);
        return 0;
    }
}
