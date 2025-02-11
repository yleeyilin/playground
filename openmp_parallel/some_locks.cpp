#include <omp.h>
#include <stdio.h>

int main() {
    int sum = 0;
    omp_lock_t lock;

    omp_init_lock(&lock);

    #pragma omp parallel
    {
        int local_sum = 0;

        #pragma omp for
        for (int i = 0; i < 10000000; i++) {
            local_sum += i;
        }

        omp_set_lock(&lock);
        sum += local_sum;
        omp_unset_lock(&lock);
    }

    omp_destroy_lock(&lock);

    printf("Sum = %d\n", sum);
    return 0;
}
