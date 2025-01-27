#include <sys/types.h>
#include <unistd.h> 
#include <sys/wait.h>

#include <cstdio>

int main(int argc, char *argv[]) {
    int value = 10; 
    pid_t child = fork();

    if (child == 0) {
        // means it is a child process
        value += 10; 
        printf("Child process: value = %d\n", value);
    } else if (child < 0) {
        // forking process was unsuccessful 
    } else {
        // means it is a parent process 
        wait(nullptr);
        printf("Main process: value = %d\n", value);
    }
}