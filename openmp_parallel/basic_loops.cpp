#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <omp.h>

// g++ -fopenmp -o basic_loops basic_loops.cpp
int main(int argc, char* argv[]) {
    #pragma omp parallel for
    for (int i = 0; i < 10; i++) {
        printf("loop %d\n", i);
        sleep(1);
    }
    return 0;
}
