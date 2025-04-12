#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <omp.h>

// suppose u hv N int stored in array A
// you want to find numbers that are at most 10% less than max 
// in a shared memory machine 
int main(int argc, char* argv[]) {
    // Step 1: Parallel max using OpenMP reduction
    max_val = -∞
    #pragma omp parallel for reduction(max:max_val)
    for (int i = 0; i < N; i++) {
        if (A[i] > max_val) max_val = A[i];
    }

    // Step 2: Filter values > 0.9 * max_val
    threshold = 0.9 * max_val

    #pragma omp parallel for
    for (int i = 0; i < N; i++) {
        if (A[i] > threshold) {
            #pragma omp critical
            output.push_back(A[i]);
        }
    }
    return 0;
}