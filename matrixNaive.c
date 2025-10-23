#include <stdio.h>
#include <stdlib.h>
#include <sys/time.h>
#include <time.h>

void setMatrixZero(double *M, int n) {
  for (int i = 0; i < n * n; i++) {
    M[i] = 0.0;
  }
}

void randMatrix(double *M, int n) {
  for (int i = 0; i < n * n; i++) {
    M[i] = (double)rand() / RAND_MAX;
  }
}

void multNaive(double *a, double *b, double *c, int n) {
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
      for (int k = 0; k < n; k++) {
        c[i * n + j] += a[i * n + k] * b[k * n + j];
      }
    }
  }
}

int main(int argc, char *argv[]) {
  if (argc < 3) {
    fprintf(stderr, "Usage: %s <n> <runs>\n", argv[0]);
    return 1;
  }

  int n = atoi(argv[1]);
  int runs = atoi(argv[2]);

  srand((unsigned int)time(NULL));

  double memoryUsed = (3.0 * n * n * sizeof(double)) / (1024.0 * 1024.0);

  double *a = (double*)malloc(n * n * sizeof(double));
  double *b = (double*)malloc(n * n * sizeof(double));
  double *c = (double*)malloc(n * n * sizeof(double));

  struct timeval start, stop;
  gettimeofday(&start, NULL);

  for (int i = 0; i < runs; i++) {
    randMatrix(a, n);
    randMatrix(b, n);
    setMatrixZero(c, n);
    multNaive(a, b, c, n);
  }

  gettimeofday(&stop, NULL);
  double timeDiff = (stop.tv_sec - start.tv_sec) + 1e-6 * (stop.tv_usec - start.tv_usec);

  printf("C: n=%d, runs=%d, time=%.3fs, timePerRun=%.3fs, memoryUsed=%.2fMB\n",
         n, runs, timeDiff, timeDiff / runs, memoryUsed);

  free(a);
  free(b);
  free(c);

  return 0;
}
