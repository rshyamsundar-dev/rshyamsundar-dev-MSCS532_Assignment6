# MSCS 532 Assignment 6
## Medians, Order Statistics, and Elementary Data Structures

## Overview

This project implements selection algorithms and elementary data structures in Python.

### Part 1
- Deterministic Selection (Median of Medians)
- Randomized Quickselect
- Performance Benchmarking
- Unit Testing

### Part 2
- Dynamic Array
- Matrix
- Stack
- Queue (Circular Array)
- Singly Linked List
- Unit Testing

---

## Project Structure

```
assignment-6-order-statistics/
│
├── part1_selection/
│   ├── deterministic_select.py
│   ├── randomized_select.py
│   └── benchmark_selection.py
│
├── part2_data_structures/
│   ├── dynamic_array.py
│   ├── matrix.py
│   ├── stack.py
│   ├── queue.py
│   └── linked_list.py
│
├── tests/
│   ├── test_selection.py
│   └── test_data_structures.py
│
├── results/
│   └── selection_results.csv
│
├── README.md
└── demo.py
```

---

## Requirements

- Python 3.10 or later

---

## Running the Programs

### Deterministic Selection

```bash
python3 part1_selection/deterministic_select.py
```

### Randomized Quickselect

```bash
python3 part1_selection/randomized_select.py
```

### Benchmark

```bash
python3 -m part1_selection.benchmark_selection
```

### Dynamic Array

```bash
python3 part2_data_structures/dynamic_array.py
```

### Matrix

```bash
python3 part2_data_structures/matrix.py
```

### Stack

```bash
python3 part2_data_structures/stack.py
```

### Queue

```bash
python3 part2_data_structures/queue.py
```

### Linked List

```bash
python3 part2_data_structures/linked_list.py
```

---

## Running Unit Tests

Selection Algorithms

```bash
python3 -m unittest tests/test_selection.py -v
```

Elementary Data Structures

```bash
python3 -m unittest tests/test_data_structures.py -v
```

---

## Summary

The benchmark demonstrates that Randomized Quickselect generally performs faster in practice because of its low pivot-selection overhead, while the Median of Medians algorithm guarantees linear worst-case performance through deterministic pivot selection.

Arrays provide efficient indexed access, whereas linked lists support flexible insertions and deletions. Stacks and queues demonstrate fundamental LIFO and FIFO behaviors that are widely used in software systems.