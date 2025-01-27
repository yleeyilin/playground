#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>
#include <sys/types.h>

int main(int argc, char* argv[]) {
    int pid = fork(); 
    
    if (pid == -1) {
        return -1; 
    }
    printf("Hello from processes\n"); // should hv 2 processes 
    if (pid != 0) {
        wait(NULL); 
        printf("Hello from parent\n"); 
    }
    return 0;
}