#include "solve.h"
#include <cuda_runtime.h>

__global__ void parallel_reduction(const float* input, const float* output, int N) {
    // combine halved idx 
    int global_idx = blockIdx.x * blockDim.x + threadIdx.x; 

    __shared__ unsigned long long data[blockDim.x];

    data[threadIdx.x] = (global_idx < N) ? input[global_idx] : 0; 
    __syncthreads();

    for (int stride = blockDim.x / 2; stride > 0; stride >>= 1) {
        __syncthreads();
        if (threadIdx.x < stride) {
            data[threadIdx.x] += data[threadIdx.x + stride];
        }
    }

    if (threadIdx.x == 0) {
        atomicAdd(&output, data[0]);
    }
}

// input, output are device pointers
void solve(const float* input, float* output, int N) {  
    int threadsPerBlock = 256;
    int blocksPerGrid = (N + threadsPerBlock - 1) / threadsPerBlock;

    parallel_reduction<<<blocksPerGrid, threadsPerBlock>>>(input, output, N); 
    cudaDeviceSynchronize();
}