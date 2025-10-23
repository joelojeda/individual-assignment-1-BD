import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("results.csv")

for language in df["language"].unique():
    data = df[df["language"] == language]
    plt.plot(data["n"], data["time_per_run_sec"], marker="o", label=language)

plt.title("Matrix Multiplication – Time per Run")
plt.xlabel("Matrix Size (n × n)")
plt.ylabel("Time per Run (s)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

for language in df["language"].unique():
    data = df[df["language"] == language]
    plt.plot(data["n"], data["memory_mb"], marker="s", label=language)

plt.title("Matrix Multiplication – Memory Usage")
plt.xlabel("Matrix Size (n × n)")
plt.ylabel("Memory Used (MB)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
