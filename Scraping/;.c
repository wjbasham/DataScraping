#include <stdio.h>
#include <math.h>
#include <mpi.h>

#define N 1000000

long a[N], b[N];
int count = 0;
long calcDot(long a[], long b[]){
        int i = 0;
        int size, rank;
        long z;
        MPI_Comm_size(MPI_COMM_WORLD, &size);
        MPI_Comm_rank(MPI_COMM_WORLD, &rank);
        for(i; i <= N; i+= size){
                z+= a[i] * b[i];
        }
        printf("this is process %d out of %d and z is: %ld\n", rank, size, z);

        return z;
}

int main(int argc, char* argv[]){
int i, chunk = 100;
        int rank, size;
        long asize, bsize;
        asize = 0;
        bsize = 0;
        MPI_Init(&argc, &argv);
        MPI_Comm_rank(MPI_COMM_WORLD, &rank);
        MPI_Comm_size(MPI_COMM_WORLD, &size);
        printf("this is process %d out of %d\n", rank, size);
        if(rank == 0){
                printf("rank is 0\n");
                for(i = 0; i<N; i++){
                        a[i] = i;
                        asize++;
                        b[i] = N-i;
                        bsize++;
                }
                printf("the asize is %ld the bsize is %ld\n", asize, bsize);
                printf(" at a[0] is %ld\n", a[0]);
        }
        MPI_Bcast(&a, N, MPI_LONG, 0, MPI_COMM_WORLD);
        MPI_Bcast(&b, N, MPI_LONG, 0, MPI_COMM_WORLD);
        long z = 0;
        long holder = 0;
        for(i = 0; i <= N; i+= size){
                holder += a[i] * b[i];
        }

        MPI_Reduce(&holder, &z, 1, MPI_LONG, MPI_SUM, 0, MPI_COMM_WORLD);
        if(rank == 0){
                printf("The dot product is %ld\n", z);
        }
        MPI_Finalize();
        return 0;
}
                                                              58,1          Bot
