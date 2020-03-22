#include <stdio.h>
#include <stdlib.h>
#include <sys/time.h>
#include "utils.h"

#define MAX_ELEM 1000

void BMMultiply(int n, double* a, double* b, double* c)
{
    int bi=0;
    int bj=0;
    int bk=0;
    int i=0;
    int j=0;
    int k=0;
    // TODO: set block dimension blockSize
    int blockSize=250; 
 
    for(bi=0; bi<n; bi+=blockSize)
        for(bj=0; bj<n; bj+=blockSize)
            for(bk=0; bk<n; bk+=blockSize)
                for(i=0; i<blockSize; i++)
                    for(j=0; j<blockSize; j++)
                        for(k=0; k<blockSize; k++)
                            c[(bi + i) * n + (bj + j)] += a[(bi + i) * n/blockSize + 
                            (bk + k)] * b[(bk + k) * n/blockSize + (bj + j)];
}
 
int main(void)
{
    int n;
    double* A;
    double* B;
    double* C;
    int numreps = 1;
    int i=0;
    int j=0;
    struct timeval tv1, tv2;
    struct timezone tz;
    double elapsed = 0.0;
    // TODO: set matrix dimension n
    n = MAX_ELEM;
    // allocate memory for the matrices
 
    // TODO: allocate matrices A, B & C
    ///////////////////// Matrix A //////////////////////////
    // TODO ...
	A = (double *) malloc (MAX_ELEM * MAX_ELEM * sizeof(double));
	DIE(A == NULL, "could not allocate matrix A\n");
	
    ///////////////////// Matrix B ////////////////////////// 
    // TODO ...
	B = (double *) malloc (MAX_ELEM * MAX_ELEM * sizeof(double));
	DIE(B == NULL, "could not allocate matrix B\n");    
	
    ///////////////////// Matrix C //////////////////////////
    // TODO ...
	C = (double *) malloc (MAX_ELEM * MAX_ELEM * sizeof(double));
	DIE(C == NULL, "could not allocate matrix C\n");
 
    // Initialize matrices A & B
    for(i=0; i<n; i++)
    {
        for(j=0; j<n; j++)
        {
            A[i * MAX_ELEM + j] = 1;
			B[i * MAX_ELEM + j] = 2;
        }
    }
 
    //multiply matrices
 
    printf("Multiply matrices %d times...\n", numreps);
    for (i=0; i<numreps; i++)
    {
        gettimeofday(&tv1, &tz);
        BMMultiply(n,A,B,C);
        gettimeofday(&tv2, &tz);
        elapsed += (double) (tv2.tv_sec-tv1.tv_sec) + (double) (tv2.tv_usec-tv1.tv_usec) * 1.e-6;
    }
    printf("Time = %lf \n",elapsed);
 
    //deallocate memory for matrices A, B & C
    // TODO ...
	
	free(A);
    free(B);
    free(C);
	
    return 0;
}