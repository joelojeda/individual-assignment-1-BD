#!/bin/bash

OUTFILE="results.csv"
RUNS=10
SIZES=(128 256 512 1024)
PYTHON_FILE="matrix_naive.py"
JAVA_FILE="MatrixNaive.java"
JAVA_CLASS="MatrixNaive"
C_FILE="matrixNaive.c"
C_EXEC="matrixNaive"

echo "language,n,runs,time_sec,time_per_run_sec,memory_mb" >"$OUTFILE"

javac "$JAVA_FILE"
gcc "$C_FILE" -o "$C_EXEC"

for n in "${SIZES[@]}"; do
  echo -e "\n--- Running scripts for n=$n ---"

  echo "[C]"
  OUTPUT=$(./$C_EXEC $n $RUNS)
  echo "$OUTPUT"
  TIME=$(echo "$OUTPUT" | grep -oP 'time=\K[\d.]+')
  TIMEPER=$(echo "$OUTPUT" | grep -oP 'timePerRun=\K[\d.]+')
  MEM=$(echo "$OUTPUT" | grep -oP 'memoryUsed=\K[\d.]+')
  echo "C,$n,$RUNS,$TIME,$TIMEPER,$MEM" >>"$OUTFILE"

  echo "[Java]"
  OUTPUT=$(java "$JAVA_CLASS" $n $RUNS)
  echo "$OUTPUT"
  TIME=$(echo "$OUTPUT" | grep -oP 'time=\K[\d.]+')
  TIMEPER=$(echo "$OUTPUT" | grep -oP 'timePerRun=\K[\d.]+')
  MEM=$(echo "$OUTPUT" | grep -oP 'memoryUsed=\K[\d.]+')
  echo "Java,$n,$RUNS,$TIME,$TIMEPER,$MEM" >>"$OUTFILE"

  echo "[Python]"
  OUTPUT=$(python3 "$PYTHON_FILE" $n $RUNS)
  echo "$OUTPUT"
  TIME=$(echo "$OUTPUT" | grep -oP 'time=\K[\d.]+')
  TIMEPER=$(echo "$OUTPUT" | grep -oP 'timePerRun=\K[\d.]+')
  MEM=$(echo "$OUTPUT" | grep -oP 'memoryUsed=\K[\d.]+')
  echo "Python,$n,$RUNS,$TIME,$TIMEPER,$MEM" >>"$OUTFILE"
done
