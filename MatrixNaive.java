import java.util.Random;

public class MatrixNaive {
  static double[][] initMatrixZero(int n) {
    double[][] M = new double[n][n];
    setMatrixZero(M);
    return M;
  }

  static void setMatrixZero(double[][] M) {
    int n = M.length;
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < n; j++) {
        M[i][j] = 0;
      }
    }
  }

   static void randMatrix(double[][] M) {
    Random random = new Random();
    int n = M.length;
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < n; j++) {
        M[i][j] = random.nextDouble();
      }
    }
  }

 static void multNaive(double[][] a, double[][] b, double[][] c){
    int n = a.length;
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < n; j++) {
        for (int k = 0; k < n; k++) {
          c[i][j] += a[i][k] * b[k][j];
        }
      }
    }
  }

	public static void main(String[] args) {
    if (args.length < 2) {
      System.err.println("Usage: java matrixNaive <n> <runs>");
      System.exit(1);
    }

    int n = Integer.parseInt(args[0]);
    int runs = Integer.parseInt(args[1]);

    Runtime runtime = Runtime.getRuntime();
    double memoryStart = runtime.totalMemory() - runtime.freeMemory();

    double[][] a = initMatrixZero(n);
    double[][] b = initMatrixZero(n);
    double[][] c = initMatrixZero(n);

    double memoryStop = runtime.totalMemory() - runtime.freeMemory();

		long timeStart = System.currentTimeMillis();

    for(int i = 0; i < runs; i++){
      randMatrix(a);
      randMatrix(b);
      setMatrixZero(c);
      multNaive(a, b, c);
    }

		long timeStop = System.currentTimeMillis();

    double memoryDiff = (memoryStop - memoryStart) / (1024 * 1024);
    double timeDiff = ((timeStop - timeStart) * 1e-3);

    System.out.printf("Java: n=%d, runs=%d, time=%.3fs, timePerRun=%.3fs, memoryUsed=%.2fMB\n", n, runs, timeDiff, timeDiff/runs, memoryDiff);
	}
}

