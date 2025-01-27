#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <pthread.h>

void* thread_func(void* arg) {
    printf("Entering thread\n");
    sleep(3);
    printf("Exiting thread\n");
}

int main(int argc, char* argv[]) {
    pthread_t p1, p2; 
    if (pthread_create(&p1, NULL, &thread_func, NULL)) {
        return -1; 
    }
    if (pthread_create(&p2, NULL, &thread_func, NULL)) {
        return -1; 
    }
    pthread_join(p1, NULL); 
    pthread_join(p2, NULL); 
    return 0;
}