# LABORATORY EXPERIMENT REPORT

**Course Title:** Parallel and Grid Computing (PGC)  
**Experiment Title:** Performance Analysis of Parallel Vector Addition using OpenMP  
**Author / Repository Owner:** `shifa2006`  
**Repository:** `https://github.com/shifa2006/PGC-Lab`  
**Date:** 8 October 2026  

---

## 1. Abstract

This laboratory experiment evaluates the performance of parallel vector
addition using the OpenMP programming model in C.

A vector addition operation is performed on vectors containing
10,000,000 elements. OpenMP is used to parallelize the computation by
distributing loop iterations among multiple threads.

The experiment focuses on measuring execution time and analyzing the
effect of different thread configurations on parallel performance.
The implementation demonstrates how a computationally independent
operation such as vector addition can be efficiently parallelized using
shared-memory programming.

The experimental results are used to compare execution performance for
different numbers of threads and to understand the factors that affect
parallel execution, including thread management overhead, processor
resources, memory access, and workload distribution.

---

## 2. Experimental Objectives

The main objectives of this experiment are:

1. Implement vector addition using the OpenMP programming model in C.
2. Understand parallel execution using multiple OpenMP threads.
3. Apply the OpenMP `parallel for` directive to distribute loop iterations.
4. Measure the execution time of parallel vector addition.
5. Compare execution performance for different thread configurations.
6. Analyze the effect of increasing the number of threads on execution
   performance.
7. Understand the overhead and limitations associated with parallel
   execution.

---

## 3. Experimental Configuration

| Parameter | Value |
|---|---|
| Programming Language | C |
| Programming Model | OpenMP |
| Vector Size | 10,000,000 |
| Operation | Vector Addition |
| Threads | 1, 2, 4, and 8 |
| Performance Metric | Execution Time |
| Compiler | GCC |
| OpenMP Flag | `-fopenmp` |

---

## 4. System Architecture & Source Code

### 4.1 Program Description

The experiment uses three dynamically allocated vectors:

- Vector `A`
- Vector `B`
- Vector `C`

The input vectors are initialized and the addition operation is performed
using:

```text
C[i] = A[i] + B[i]
```
## Source Code

The OpenMP implementation is available at:

`src/parallel.c`

The program performs the following operations:

- Allocates memory for the three vectors.
- Initializes vectors A and B.
- Starts the execution timer.
- Performs vector addition using OpenMP.
- Stops the execution timer.
- Displays the execution time and result verification values.
- Releases the allocated memory.

  ---

  ## Repository Structure

`Lab-Evaluation/
├── README.md
├── src/
│   └── parallel.c
├── data/
├── results/
├── graphs/
└── presentation/`
### Directory Description
| Directory |	Description |
|---|---|
| `src/` |	Contains the OpenMP source code |
| `data/` |	Contains experimental data, if applicable |
| `results/` |	Contains execution outputs and screenshots |
| `graphs/` |	Contains performance graphs |
| `presentation/` |	Contains presentation material |

---

## Compilation and Execution

The OpenMP program can be compiled using GCC with OpenMP support.

Compilation :
`
gcc src/parallel.c -o parallel -fopenmp
Execution
./parallel
`

The program displays the vector size, number of threads used,
execution time, and selected vector addition results.

---

## Empirical Data & Benchmarking Results

 ### Performance Results

The execution time was measured for different OpenMP thread
configurations.

| Number of Threads	| Execution Time (s) |
|---|---|
| 1	| 0.029162 sec |
| 2	| 0.015312 sec |
| 4	| 0.008661 sec |
| 8	| 0.023319 sec |

---

## Conclusion

This laboratory experiment provided practical understanding of
parallel vector addition using the OpenMP programming model in C.

A vector size of 10,000,000 elements was used to perform vector
addition. The computation was parallelized using the OpenMP
`parallel for` directive, allowing different loop iterations to be
executed concurrently by multiple threads.

The experiment demonstrated the basic principles of shared-memory
parallel programming, including thread-based workload distribution and
parallel execution. Execution time was measured using
`omp_get_wtime()` to evaluate the performance of the parallel
implementation.

The experiment also showed that increasing the number of threads can
reduce execution time by allowing more operations to be processed
simultaneously. However, the performance improvement is affected by
parallel overhead, processor resources, thread scheduling, and memory
bandwidth.

The recorded execution times and performance graphs provide a clear
comparison of the different thread configurations. This analysis helps
in understanding that efficient parallel programming depends not only
on increasing the number of threads but also on effective workload
distribution and efficient utilization of system resources.

Overall, the experiment provided practical experience with OpenMP,
parallel vector computation, execution-time measurement, performance
evaluation, and analysis of thread-level parallelism.
