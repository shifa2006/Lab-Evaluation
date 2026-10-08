# Lab Evaluation

## Overview

This repository contains the implementation and performance evaluation of
parallel vector addition using OpenMP.

The experiment demonstrates how a large vector addition operation can be
parallelized using multiple threads. The execution performance is evaluated
by measuring the execution time for different numbers of threads.

The experiment focuses on understanding parallel execution, OpenMP directives,
thread-level parallelism, and performance improvement obtained through
parallel processing.

---

## Objective

The main objectives of this experiment are:

- To implement vector addition using OpenMP.
- To understand parallel execution using multiple threads.
- To study the effect of thread count on execution time.
- To measure and compare the performance of parallel execution.
- To analyze the performance improvement obtained through OpenMP.

---

## Experiment

### Parallel Vector Addition using OpenMP

In this experiment, three vectors `A`, `B`, and `C` are used.

The input vectors `A` and `B` are initialized with values, and the addition
operation is performed as:

```text
C[i] = A[i] + B[i]
```
---

### Experimental Configuration

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

## Methodology

The experiment was performed using the following steps:

-  Three vectors of size 10,000,000 were allocated dynamically.
- The input vectors A and B were initialized.
- The vector addition operation was implemented using an OpenMP
parallel loop.
- Different thread configurations were used for performance evaluation.
- The execution time of the parallel vector addition was measured using
omp_get_wtime().
- The execution time values were recorded for comparison.
- Performance graphs were generated to analyze the effect of thread count
on execution time.

---

## Repository Structure

```hash
Lab-Evaluation/
├── README.md
├── src/
├── data/
├── results/
├── graphs/
└── presentation/
```
### Folder Description

- ` src/ ` - Contains the OpenMP source code.
- `data/ `- Contains input data or experimental data if required.
- `results/ `- Contains recorded execution results and screenshots.
- `graphs/ `- Contains performance graphs.
- `presentation/` - Contains the presentation used for the lab evaluation.

  ---

## Source Code

The complete OpenMP implementation is available in:

`src/parallel.c`

The program performs parallel vector addition and measures the execution
time of the parallel section.

The OpenMP parallelization is implemented using the parallel for
directive, which distributes loop iterations among the available threads.

---

## Compilation and Execution

The program can be compiled using GCC with OpenMP support:

`gcc src/parallel.c -o parallel -fopenmp`

The program can then be executed using:

`./parallel`

The program displays:

- Vector size
- Number of threads used
- Execution time
- First result of the vector addition
- Last result of the vector addition

---

## Results

The program produced the following type of output:
```text
Parallel Vector Addition using OpenMP
Vector Size: 10000000
Threads Used: 8
Execution Time: 0.023319 seconds
First Result: C[0] = 0
Last Result: C[9999999] = 29999997
```


The actual execution time depends on the system configuration and the
number of threads used during execution.

### Result Screenshot
<img width="943" height="307" alt="parallel_Thread- 1" src="https://github.com/user-attachments/assets/7b1c8163-2c5e-467d-a614-ccb9c4d851e5" />
<img width="955" height="302" alt="parallel_Thread- 2" src="https://github.com/user-attachments/assets/15d55d28-5d46-4457-a76e-5a04c6e6faef" />
<img width="952" height="313" alt="parallel_Thread- 4" src="https://github.com/user-attachments/assets/5d8ab829-6cac-4fc8-a654-6b350ba0eec8" />
<img width="957" height="305" alt="parallel_Thread- 8" src="https://github.com/user-attachments/assets/8281d43f-8149-4624-ba97-64364cf1d18b" />

---

## Performance Analysis

The performance of the OpenMP implementation was evaluated by changing
the number of threads.

|Number of Threads |	Execution Time|
|----|----|
|1	| 0.029162 sec |
|2	| 0.015312 sec |
|4	|0.008661 sec |
|8	|0.023319 sec |

The execution time values are used to study how increasing the number of
threads affects the performance of vector addition.

In general, parallel execution can reduce computation time because
multiple loop iterations can be processed simultaneously. However, the
performance improvement depends on factors such as thread management
overhead, processor resources, memory access, and workload distribution.

---

## Performance Graphs

The graphs generated from the experimental results are available in the
graphs/ directory.

### Execution Time vs Number of Threads

This graph shows how execution time changes as the number of OpenMP
threads increases.

<img width="1367" height="567" alt="Execution Time Graph LE" src="https://github.com/user-attachments/assets/d7f6eca5-b91c-4f1c-aceb-1d57fd17ceb1" />


### Performance Comparison

This graph provides a visual comparison of the measured execution
performance for different thread configurations.

#### Efficiency graph

<img width="1336" height="588" alt="Efficiency Graph LE" src="https://github.com/user-attachments/assets/531029e4-2d87-4c62-bd17-3993ae243698" />

##### Speedup graph 

<img width="697" height="597" alt="Speedup graph LE" src="https://github.com/user-attachments/assets/9166eb9d-6e21-492c-adc6-6201ddfaba0f" />

---

## Key Observations

- OpenMP provides a simple approach to parallel programming using
compiler directives.
- The `parallel for`directive distributes loop iterations among multiple
threads.
- Vector addition is suitable for parallel execution because each
element can be calculated independently.
- Increasing the number of threads can reduce execution time when
sufficient processor resources are available.
- Performance improvement is not always proportional to the number of
threads.
- Thread management and scheduling introduce additional overhead.
- Memory access and bandwidth can also affect the performance of vector
operations.
- The measured execution time provides a practical way to compare
different thread configurations.
- The experiment demonstrates the practical use of OpenMP for
data-parallel computation.
- The performance graphs make it easier to observe the effect of
thread count on execution time.

---

## Conclusion

This experiment provided practical understanding of parallel vector
addition using OpenMP.

A large vector of 10,000,000 elements was created and the addition of
two input vectors was performed using multiple OpenMP threads. The
parallel for directive was used to distribute the vector addition
operation among the available threads.

The experiment demonstrated how a computationally repetitive operation
can be divided into smaller independent tasks and executed concurrently.
The execution time was measured for different thread configurations to
evaluate the performance of parallel execution.

The performance analysis showed that changing the number of threads has
a direct effect on execution time. Increasing the number of threads can
improve performance by allowing multiple operations to execute
simultaneously. However, the improvement is limited by factors such as
thread management overhead, processor resources, memory access, and
workload distribution.

Overall, the experiment demonstrates the effectiveness of OpenMP for
parallel data processing and provides practical experience in thread
parallelism, execution-time measurement, and performance analysis.
