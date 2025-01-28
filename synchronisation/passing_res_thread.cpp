#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <pthread.h>

// In this program, we want to pass a value result back from the
// thread to the main thread. 
void *fn(void *tid) {
    int value = (rand() % 6) + 1; 
    // use malloc bc we want the value to last beyond the scope
    // of the function 
    int* res = (int*) malloc(sizeof(int));
    *res = value; 
    return res;
}

int main(int argc, char* argv[]) {
    int* final_res; 

    pthread_t p1; 
    srand(time(NULL)); 

    if (pthread_create(&p1, NULL, &fn, NULL)) {
        // error code 
        return -1; 
    }
    if (pthread_join(p1, (void**) &final_res)) {
        // error code 
        return -2; 
    }
    printf("Result = %d", *final_res); 
    return 0;
}