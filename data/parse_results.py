#!/usr/bin/env python3

import csv
from pathlib import Path

RESULTS_DIR = Path("results")

DATA_SIZE_FILE = RESULTS_DIR / "data_size_results.csv"
THREAD_FILE = RESULTS_DIR / "thread_results.csv"


def read_csv(filename):
    with open(filename, newline="") as f:
        return list(csv.DictReader(f))


def main():
    data_results = read_csv(DATA_SIZE_FILE)
    thread_results = read_csv(THREAD_FILE)

    print("=== Data Size Results ===")
    print(f"{'Vector Size':>12} {'Sequential':>15} {'OpenMP':>15}")

    for row in data_results:
        print(
            f"{int(row['vector_size']):>12,} "
            f"{float(row['sequential_time']):>15.6f} "
            f"{float(row['openmp_time']):>15.6f}"
        )

    print("\n=== Thread Count Results ===")
    print(f"{'Threads':>8} {'Vector Size':>15} {'Time (s)':>15}")

    for row in thread_results:
        print(
            f"{int(row['threads']):>8} "
            f"{int(row['vector_size']):>15,} "
            f"{float(row['execution_time']):>15.6f}"
        )

    # Speedup and efficiency using the 1-thread result.
    t1 = float(thread_results[0]["execution_time"])

    print("\n=== Speedup & Efficiency ===")
    print(f"{'Threads':>8} {'Speedup':>12} {'Efficiency':>15}")

    for row in thread_results:
        threads = int(row["threads"])
        time = float(row["execution_time"])
        speedup = t1 / time
        efficiency = speedup / threads * 100

        print(
            f"{threads:>8} "
            f"{speedup:>12.2f}x "
            f"{efficiency:>14.1f}%"
        )


if __name__ == "__main__":
    main()
