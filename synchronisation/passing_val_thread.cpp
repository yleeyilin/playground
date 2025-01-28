#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <pthread.h>

int arr[10] = { 2, 3, 5, 7, 11, 13, 17, 19, 23, 29};

void *fn(void* arg) {
    sleep(1);
    size_t ptr = (size_t) arg;
    printf("Value here: %d\n", arr[ptr]);
    pthread_exit(NULL);
}

int main(int argc, char* argv[]) {
    pthread_t pthreads[10]; 
    
    for (size_t i = 0; i < 10; i++) {
        // NOTE: (void *) creates a temporary void* pointer holding the integer value of i
        if (pthread_create(&pthreads[i], NULL, &fn, (void *)i)) {
            perror("Failed to create thread!"); 
        }
    }
    for (size_t i = 0; i < 10; i++) {
        if (pthread_join(pthreads[i], NULL)) {
            perror("Failed to join thread!"); 
        }
    }
    return 0;
}