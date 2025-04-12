#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <mpi.h>

// suppose u hv N int stored in array A
// you want to find numbers that are at most 10% less than max 
// in a distributed memory machine 
int main(int argc, char* argv[]) {
    // init mpi env 
    MPI_Init(&argc, &argv);

    int rank, size;
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    // Step 1: Local maximum
    local_max = -∞
    for (int i = 0; i < local_N; i++) {
        if (A_local[i] > local_max) local_max = A_local[i];
    }

    // Step 2: Global maximum
    MPI_Reduce(&local_max, &global_max, 1, MPI_INT, MPI_MAX, 0, MPI_COMM_WORLD)
    MPI_Bcast(&global_max, 1, MPI_INT, 0, MPI_COMM_WORLD)

    // Step 3: Local filtering
    threshold = 0.9 * global_max
    local_output = []
    for (int i = 0; i < local_N; i++) {
        if (A_local[i] > threshold) {
            local_output.push_back(A_local[i]);
        }
    }

    // Step 4: Gather results at root
    MPI_Gather(local_output, ..., root)
    return 0;
}