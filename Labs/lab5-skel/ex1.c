#include <stdio.h>
#include <string.h>
#include <time.h>
#include <stdlib.h>
#include <sys/time.h>
#include "utils.h"

#define MAX_ELEM 500

int main(int argc, char *argv[]){

	DIE(argc < 2, "usage: ./ex1 <mode>; mode: 0 - unoptimised, \
			1 - optimised, 2 - using pointers");

	int i, j, k;
	// Allocate memory for matrixes

	double *A = (double *) malloc (MAX_ELEM * MAX_ELEM * sizeof(double));
	DIE(A == NULL, "could not allocate matrix A\n");
	
	double *B = (double *) malloc (MAX_ELEM * MAX_ELEM * sizeof(double));
	DIE(B == NULL, "could not allocate matrix B\n");    
	
	double *C = (double *) malloc (MAX_ELEM * MAX_ELEM * sizeof(double));
	DIE(C == NULL, "could not allocate matrix C\n");

	srand(42);
	// Populate matrixes

	for (i = 0; i != MAX_ELEM*MAX_ELEM; ++i){
	A[i] = (double)rand() / RAND_MAX * 2.0 - 1.0;
	B[i] = (double)rand() / RAND_MAX * 2.0 - 1.0;
	}

	// Compute matrix product
	// 0 - unoptimised

	if(strcmp(argv[1], "0") == 0 ) {
		for (i = 0; i != MAX_ELEM; ++i) {
			for (j = 0; j != MAX_ELEM; ++j) {
				for (k = 0; k != MAX_ELEM; ++k) {
					C[i * MAX_ELEM + j] += A[i * MAX_ELEM + j] * B[k * MAX_ELEM + j];
				}
			}
		}
	}

	// 1 - optimised
	if(strcmp(argv[1], "1") == 0 ) {
		for (i = 0; i != MAX_ELEM; ++i) {
			for (j = 0; j != MAX_ELEM; ++j) {
				register double suma = 0.0;
				for (k = 0; k != MAX_ELEM; ++k) {
						suma += A[i * MAX_ELEM + j] * B[k * MAX_ELEM + j];
				}
				C[i * MAX_ELEM + j] = suma;
			}
		}
	}

	// 2 - using pointers
	if(strcmp(argv[1], "2") == 0 ) {
		for(i = 0; i < MAX_ELEM; i++){
			double *orig_pa = &A[MAX_ELEM * i];
			for(j = 0; j < MAX_ELEM; j++){
				double *pa = orig_pa;
				double *pb = &B[j];
				register double suma = 0;
				for(k = 0; k < MAX_ELEM; k++){
					suma += *pa * *pb;
					pa++;
					pb += MAX_ELEM;
				}
				C[i * MAX_ELEM + j] = suma;
			}
		}
	}


	free(A);
	free(B);
	free(C);
	return 0;
}