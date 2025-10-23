import sys
import time
import random
import os
import psutil

def init_matrix_zero(n):
    return [[0.0 for _ in range(n)] for _ in range(n)]

def set_matrix_zero(M):
    n = len(M)
    for i in range(n):
        for j in range(n):
            M[i][j] = 0.0

def rand_matrix(M):
    n = len(M)
    for i in range(n):
        for j in range(n):
            M[i][j] = random.random()

def mult_naive(a, b, c):
    n = len(a)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                c[i][j] += a[i][k] * b[k][j]

def main():
    if len(sys.argv) < 3:
        print("Usage: python matrix_naive.py <n> <runs>")
        sys.exit(1)

    n = int(sys.argv[1])
    runs = int(sys.argv[2])

    process = psutil.Process(os.getpid())
    memory_start = process.memory_info().rss

    a = init_matrix_zero(n)
    b = init_matrix_zero(n)
    c = init_matrix_zero(n)

    memory_stop = process.memory_info().rss

    time_start = time.time()

    for _ in range(runs):
        rand_matrix(a)
        rand_matrix(b)
        set_matrix_zero(c)
        mult_naive(a, b, c)

    time_stop = time.time()

    memory_diff = (memory_stop - memory_start) / (1024 * 1024)
    time_diff = time_stop - time_start

    print(f"Python: n={n}, runs={runs}, time={time_diff:.3f}s, "
          f"timePerRun={time_diff/runs:.3f}s, memoryUsed={memory_diff:.2f}MB")

if __name__ == "__main__":
    main()
