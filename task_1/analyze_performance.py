import sys
import matplotlib.pyplot as plt
from collections import defaultdict

# Read data from standard input
data = sys.stdin.read().strip().split("\n")

# Parse the data
results = []
for line in data:
    matrix_size, threads, exec_time = map(float, line.split())
    results.append((int(matrix_size), int(threads), exec_time))

print(matrix_size)
print(threads)
print(exec_time)
# Group data by matrix size
grouped_data = defaultdict(list)
for matrix_size, threads, exec_time in results:
    grouped_data[matrix_size].append((threads, exec_time))

# Analyze and plot
for matrix_size, values in grouped_data.items():
    values.sort()  # Sort by thread count
    thread_counts = [v[0] for v in values]
    execution_times = [v[1] for v in values]
    base_time = execution_times[0]  # Time for 1 thread
    speedups = [base_time / t for t in execution_times]

    # Plot Speedup vs Number of Threads
    plt.figure(figsize=(10, 6))
    plt.plot(thread_counts, speedups, marker='o', label=f"Matrix Size: {matrix_size}")
    plt.xlabel("Number of Threads")
    plt.ylabel("Speedup")
    plt.title(f"Speedup vs Threads (Matrix Size: {matrix_size})")
    plt.grid(True)
    plt.legend()
    plt.savefig(f"speedup_vs_threads_{matrix_size}.png")
    plt.show()

    # Plot Execution Time vs Number of Threads
    plt.figure(figsize=(10, 6))
    plt.plot(thread_counts, execution_times, marker='o', label=f"Matrix Size: {matrix_size}")
    plt.xlabel("Number of Threads")
    plt.ylabel("Execution Time (s)")
    plt.title(f"Execution Time vs Threads (Matrix Size: {matrix_size})")
    plt.grid(True)
    plt.legend()
    plt.savefig(f"execution_time_vs_threads_{matrix_size}.png")
    plt.show()

# Cross-Matrix Analysis
matrix_sizes = list(grouped_data.keys())
threads = list(set(v[0] for v in grouped_data[matrix_sizes[0]]))  # Threads used
average_speedups = []

# Calculate average speedup for each thread count across all matrix sizes
for t in threads:
    speedup_sum = 0
    count = 0
    for matrix_size in matrix_sizes:
        values = dict(grouped_data[matrix_size])
        if t in values:
            base_time = dict(grouped_data[matrix_size])[1]  # Time for 1 thread
            speedup_sum += base_time / values[t]
            count += 1
    if count > 0:
        average_speedups.append(speedup_sum / count)

# Plot Average Speedup vs Threads
plt.figure(figsize=(10, 6))
plt.plot(threads, average_speedups, marker='o', color='purple', label="Average Speedup")
plt.xlabel("Number of Threads")
plt.ylabel("Average Speedup")
plt.title("Average Speedup vs Threads (Across Matrix Sizes)")
plt.grid(True)
plt.legend()
plt.savefig("average_speedup_vs_threads.png")
plt.show()
