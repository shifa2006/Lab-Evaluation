#!/usr/bin/env python3

import csv
from pathlib import Path

import matplotlib.pyplot as plt

RESULTS_DIR = Path("results")
GRAPHS_DIR = Path("graphs")
GRAPHS_DIR.mkdir(parents=True, exist_ok=True)


def read_csv(filename):
    with open(filename, newline="") as f:
        return list(csv.DictReader(f))


def plot_data_size():
    rows = read_csv(RESULTS_DIR / "data_size_results.csv")

    sizes = [int(r["vector_size"]) for r in rows]
    sequential = [float(r["sequential_time"]) for r in rows]
    openmp = [float(r["openmp_time"]) for r in rows]

    labels = ["100K", "1M", "10M"]
    x = range(len(labels))
    width = 0.35

    plt.figure(figsize=(8, 5))
    plt.bar([i - width / 2 for i in x], sequential,
            width=width, label="Sequential")
    plt.bar([i + width / 2 for i in x], openmp,
            width=width, label="OpenMP")

    plt.xticks(list(x), labels)
    plt.xlabel("Vector Size")
    plt.ylabel("Execution Time (seconds)")
    plt.title("Execution Time vs Vector Size")
    plt.legend()
    plt.tight_layout()

    plt.savefig(GRAPHS_DIR / "execution_time_vs_vector_size.png", dpi=200)
    plt.close()


def plot_threads():
    rows = read_csv(RESULTS_DIR / "thread_results.csv")

    threads = [int(r["threads"]) for r in rows]
    times = [float(r["execution_time"]) for r in rows]

    plt.figure(figsize=(8, 5))
    plt.plot(threads, times, marker="o")

    plt.xlabel("Number of Threads")
    plt.ylabel("Execution Time (seconds)")
    plt.title("Execution Time vs Number of Threads")
    plt.xticks(threads)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()

    plt.savefig(GRAPHS_DIR / "execution_time_vs_threads.png", dpi=200)
    plt.close()


if __name__ == "__main__":
    plot_data_size()
    plot_threads()
    print("Plots generated successfully in graphs/")
