#include "solve.h"
#include <cuda_runtime.h>

__global__ void relu_kernel(const float* input, float* output, int N) {
    int global_idx = blockIdx.x * blockDim.x + threadIdx.x;
    if (global_idx < N) {
        output[global_idx] =  input[global_idx] < 0.0 ? 0.0 : input[global_idx]; 
    }
}

// input, output are device pointers (i.e. pointers to memory on the GPU)
void solve(const float* input, float* output, int N) {
    int threadsPerBlock = 256;
    int blocksPerGrid = (N + threadsPerBlock - 1) / threadsPerBlock;

    relu_kernel<<<blocksPerGrid, threadsPerBlock>>>(input, output, N);
    cudaDeviceSynchronize();
}
