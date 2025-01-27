#include <sys/types.h>
#include <pthread.h> 
#include <cstdlib>
#include <stdio.h>


int val = 10; 

void *fn(void * threadid) {
    size_t tid = (size_t)threadid;
    val += 10;
    printf("The value now in the thread is %d", val);
    pthread_exit(NULL); 
}

int main(int argc, char *argv[]) {
    constexpr size_t NUM_THREADS = 1; 
    pthread_t threads[NUM_THREADS];

    for (size_t i = 0; i < NUM_THREADS; i++) {
        int thread = pthread_create(&threads[i], NULL, fn, (void *)i); 
        if (thread) { // will be null if it is fine 
            printf("NOT_HERE");
            exit(-1);
        }
    }

    printf("The final value now is %d", val);
    pthread_exit(NULL); // terminates the main thread, while allowing other child threads to run 
}