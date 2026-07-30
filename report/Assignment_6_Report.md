# Assignment 6: Medians, Order Statistics, and Elementary Data Structures

## Introduction

This assignment examines selection algorithms and elementary data structures. The first part focuses on finding the $k^{th}$ smallest element in an unsorted array using deterministic and randomized selection algorithms. The second part implements common data structures, including a dynamic array, matrix, stack, queue, and singly linked list.

The implementations were written in Python and tested using the built-in `unittest` framework. The selection algorithms were also benchmarked using random, sorted, reverse-sorted, and duplicate-heavy input distributions.

---

# Part 1: Selection Algorithms

## Order Statistics

An order statistic is an element's position in a sorted version of a collection. For example, the smallest element is the first order statistic, while the median is the middle order statistic.

Sorting the complete array and selecting an element requires:

$$O(nlogn)$$

time. Selection algorithms avoid fully sorting the input and can find the requested element in linear time.

The implementations in this project use zero-based indexing. Therefore:

* `k = 0` returns the smallest element.
* `k = len(values) - 1` returns the largest element.
* `k = len(values) // 2` returns the middle element.

---

## Deterministic Selection: Median of Medians

The deterministic selection implementation uses the Median of Medians algorithm. Its purpose is to guarantee linear running time even when the input arrangement is unfavorable.

### Implementation Process

The algorithm performs the following steps:

1. Divide the array into groups of at most five elements.
2. Sort each small group.
3. Extract the median of each group.
4. Recursively select the median of those medians.
5. Use that result as the partition pivot.
6. Divide the input into values lower than, equal to, and higher than the pivot.
7. Continue recursively only in the partition containing index $k$.

The implementation uses three-way partitioning:

```
lower = []
equal = []
higher = []

for value in values:
    if value < pivot:
        lower.append(value)
    elif value > pivot:
        higher.append(value)
    else:
        equal.append(value)
```

The separate `equal` partition is necessary for arrays containing duplicate values. Without it, repeated pivot values could cause incorrect indexing or unnecessary recursive calls.

### Worst-Case Time Complexity

The array is divided into groups of five. Finding the medians of those groups requires linear work.

The algorithm then recursively finds the median of approximately $n/5$ group medians:

T(n/5)

The selected pivot guarantees that a fixed fraction of elements can be discarded. The largest recursive partition contains at most approximately $7n/10$ elements.

The recurrence is:

T(n)≤T(n/5)+T(7n/10)+O(n)

The recursive problem sizes add to:

n/5 + 7n/10 = 9n/10

Because the total recursive size is less than $n$, the recurrence resolves to:

T(n) = O(n)

Therefore, Median of Medians provides worst-case linear-time selection.

### Space Complexity

The implementation creates new lists for the lower, equal, and higher partitions. It also creates groups and a list of group medians.

The auxiliary space complexity is:

O(n)

An in-place implementation could reduce memory use, but it would be more complex.

---

## Randomized Quickselect

Randomized Quickselect uses the partitioning idea from Quicksort but only recursively processes the side containing the desired order statistic.

### Implementation Process

The algorithm performs the following steps:

1. Randomly select a pivot from the current input.
2. Divide the values into lower, equal, and higher partitions.
3. Compare $k$ with the partition sizes.
4. Recursively process only the relevant partition.
5. Return the pivot when $k$ falls inside the equal partition.

A random pivot reduces the likelihood of repeatedly producing unbalanced partitions.

### Expected Time Complexity

If the pivot divides the array into reasonably balanced partitions, the recurrence is similar to:

T(n) = T(n/2) + O(n)

This resolves to:

T(n) = O(n)

Random pivot selection makes balanced or moderately balanced partitions likely over repeated calls. Therefore, the expected running time is:

O(n)

### Worst-Case Time Complexity

The worst case occurs when the pivot repeatedly becomes the smallest or largest value. The recurrence then becomes:

T(n) = T(n - 1) + O(n)

This resolves to:
    
O(n^2)

The randomized implementation does not prevent this outcome completely, but it makes repeated worst-case partitions unlikely.

### Space Complexity

Like the deterministic algorithm, the randomized implementation creates lower, equal, and higher lists.

Its auxiliary space complexity is:

O(n)

The randomized algorithm has less pivot-selection overhead than Median of Medians and is generally faster in practice.

---

# Correctness and Edge-Case Handling

Both selection algorithms validate their inputs before execution.

The implementations handle:

* Empty arrays
* Invalid negative values of $k$
* Values of $k$ outside the valid range
* Incorrect input types
* Single-element arrays
* Sorted arrays
* Reverse-sorted arrays
* Duplicate values
* Arrays where every value is identical

The public functions copy the input array before processing it. This prevents the algorithms from changing the caller's original data.

A total of 12 selection tests were executed successfully.

---

# Empirical Performance Analysis

## Experimental Method

The deterministic and randomized algorithms were tested on four input distributions:

* Random
* Sorted
* Reverse-sorted
* Duplicate-heavy

The tested input sizes were:

100, 500, 1000, 5000, 10000

For every test:

1. The median index was selected using `k = size // 2`.
2. Each algorithm was executed five times.
3. Execution time was measured using `time.perf_counter()`.
4. The result was verified against `sorted(values)[k]`.
5. Average, minimum, and maximum execution times were recorded.
6. The results were saved to `results/selection_results.csv`.

A fixed random seed of `532` was used to improve repeatability.

---

## Selected Benchmark Results

### Random Input

| Input Size | Median of Medians | Randomized Quickselect |
| ---------: | ----------------: | ---------------------: |
|        100 |       0.029442 ms |            0.017367 ms |
|        500 |       0.153317 ms |            0.151500 ms |
|      1,000 |       0.574075 ms |            0.112191 ms |
|      5,000 |       1.376859 ms |            0.559150 ms |
|     10,000 |       2.975483 ms |            1.075625 ms |

### Sorted Input

| Input Size | Median of Medians | Randomized Quickselect |
| ---------: | ----------------: | ---------------------: |
|        100 |       0.023292 ms |            0.013400 ms |
|        500 |       0.105383 ms |            0.048983 ms |
|      1,000 |       0.218292 ms |            0.107825 ms |
|      5,000 |       1.257942 ms |            0.469742 ms |
|     10,000 |       2.292734 ms |            0.870817 ms |

### Reverse-Sorted Input

| Input Size | Median of Medians | Randomized Quickselect |
| ---------: | ----------------: | ---------------------: |
|        100 |       0.025358 ms |            0.012233 ms |
|        500 |       0.106983 ms |            0.055025 ms |
|      1,000 |       0.225358 ms |            0.116925 ms |
|      5,000 |       1.072850 ms |            0.565083 ms |
|     10,000 |       2.178850 ms |            1.231859 ms |

### Duplicate-Heavy Input

| Input Size | Median of Medians | Randomized Quickselect |
| ---------: | ----------------: | ---------------------: |
|        100 |       0.020283 ms |            0.008034 ms |
|        500 |       0.052467 ms |            0.046983 ms |
|      1,000 |       0.100700 ms |            0.093992 ms |
|      5,000 |       0.550325 ms |            0.489392 ms |
|     10,000 |       1.039241 ms |            0.606708 ms |

---

## Interpretation of Results

Randomized Quickselect was faster than Median of Medians in almost every benchmark. The difference became clearer as the input size increased.

For random input with 10,000 elements, Median of Medians required approximately `2.975483 ms`, while Randomized Quickselect required approximately `1.075625 ms`.

This difference is caused by the deterministic algorithm's pivot-selection overhead. Median of Medians must divide the data into groups, sort each group, collect the medians, and recursively select another median before partitioning the original array.

Randomized Quickselect avoids this extra work. It selects a pivot directly using `random.choice`, which has much lower constant overhead.

Sorted and reverse-sorted inputs did not cause serious degradation in Randomized Quickselect because the pivot was randomly selected rather than always chosen from a fixed position.

Duplicate-heavy arrays were processed efficiently by both algorithms. The three-way partition prevented repeated values equal to the pivot from being processed recursively.

The results are consistent with the theoretical analysis:

* Median of Medians provides guaranteed $O(n)$ worst-case performance.
* Randomized Quickselect provides expected $O(n)$ performance.
* Randomized Quickselect is usually faster in practical execution.
* Median of Medians provides a stronger worst-case guarantee but has higher constant overhead.

---

# Part 2: Elementary Data Structures

## Dynamic Array

The dynamic array stores elements in an internal fixed-capacity list. When the array becomes full, its capacity is doubled.

The resize operation creates a larger storage array and copies the existing elements into it.

### Supported Operations

* Append
* Insert
* Delete
* Access
* Update
* Display
* Length

### Complexity Analysis

| Operation                 |  Time Complexity |
| ------------------------- | ---------------: |
| Access                    |           $O(1)$ |
| Update                    |           $O(1)$ |
| Append                    | Amortized $O(1)$ |
| Insert at arbitrary index |           $O(n)$ |
| Delete at arbitrary index |           $O(n)$ |
| Resize                    |           $O(n)$ |

Appending is normally constant time. A resize requires linear time, but resizing does not occur during every append. Therefore, the amortized append complexity remains $O(1)$.

### Practical Applications

Dynamic arrays are appropriate when:

* Fast indexed access is required.
* Elements are mostly added at the end.
* The collection size changes over time.
* Memory locality is important.

Examples include application records, tables, buffers, and collections of values.

---

## Matrix

The matrix implementation uses nested lists to represent rows and columns.

### Supported Operations

* Create a matrix with a default value
* Access a value
* Update a value
* Insert a row
* Delete a row
* Display the matrix

### Complexity Analysis

| Operation           | Time Complexity |
| -------------------- | ---------------: |
| Access an element    |           $O(1)$ |
| Update an element    |           $O(1)$ |
| Traverse the matrix  |          $O(rc)$ |
| Insert a row         |           $O(r)$ |
| Delete a row         |           $O(r)$ |

Here, $r$ represents the number of rows and $c$ represents the number of columns.

### Practical Applications

Matrices are commonly used in:

* Image processing
* Scientific computing
* Graph adjacency matrices
* Machine-learning datasets
* Game boards
* Numerical analysis

---

## Stack

The stack uses a Python list as its underlying array. It follows the last-in, first-out principle.

### Supported Operations

* Push
* Pop
* Peek
* Check whether empty
* Return size
* Display contents

### Complexity Analysis

| Operation   |  Time Complexity |
| ----------- | ---------------: |
| Push        | Amortized $O(1)$ |
| Pop         |           $O(1)$ |
| Peek        |           $O(1)$ |
| Check empty |           $O(1)$ |
| Size        |           $O(1)$ |

### Practical Applications

Stacks are commonly used for:

* Function-call management
* Undo and redo systems
* Expression evaluation
* Syntax parsing
* Depth-first search
* Browser navigation history

An array-backed stack is simple, efficient, and has low overhead.

---

## Circular Queue

The queue implementation uses a fixed-capacity circular array. It follows the first-in, first-out principle.

A circular queue avoids deleting elements from index zero. Removing from the front of a normal list would shift all remaining elements and require $O(n)$ time.

The circular queue uses:

* `front` to identify the next value to remove
* `rear` to identify the next insertion position
* `size` to track the number of stored elements
* Modular arithmetic to wrap indexes to the beginning of the array

### Supported Operations

* Enqueue
* Dequeue
* Peek
* Check whether empty
* Check whether full
* Display contents

### Complexity Analysis

| Operation   | Time Complexity |
| ----------- | ---------------: |
| Enqueue     |           $O(1)$ |
| Dequeue     |           $O(1)$ |
| Peek        |           $O(1)$ |
| Check empty |           $O(1)$ |
| Check full  |           $O(1)$ |

### Practical Applications

Queues are used in:

* Request processing
* Task scheduling
* Message systems
* Printer queues
* Breadth-first search
* Customer-service systems
* Network packet handling

The circular array provides constant-time queue operations without shifting elements.

---

## Singly Linked List

The singly linked list contains nodes. Each node stores a value and a reference to the next node.

The list stores a reference to its first node through the `head` field.

### Supported Operations

* Insert at the beginning
* Insert at the end
* Delete by value
* Search
* Traverse

### Complexity Analysis

| Operation           | Time Complexity |
| -------------------- | ---------------: |
| Insert at beginning  |           $O(1)$ |
| Insert at end        |           $O(n)$ |
| Search               |           $O(n)$ |
| Delete by value      |           $O(n)$ |
| Traverse             |           $O(n)$ |

The current implementation does not maintain a tail pointer. Therefore, inserting at the end requires traversing the complete list.

Adding a tail pointer would reduce end insertion to O(1).

### Practical Applications

Linked lists can be used for:

* Dynamic collections
* Graph adjacency lists
* Memory-management systems
* Hash-table collision chains
* Navigation structures
* Implementing stacks and queues

---

# Arrays Versus Linked Lists

Arrays and linked lists provide different performance characteristics.

## Arrays

Advantages:

* Constant-time indexed access
* Better memory locality
* Lower per-element overhead
* Simple traversal
* Usually faster in practice

Disadvantages:

* Middle insertion and deletion require shifting elements
* Resizing may require copying the complete array
* Contiguous storage is required

## Linked Lists

Advantages:

* Nodes do not require contiguous storage
* Inserting at the beginning is constant time
* Known nodes can be linked or unlinked without shifting other elements
* The structure can grow one node at a time

Disadvantages:

* Indexed access requires traversal
* Every node requires an additional reference
* Poorer cache locality
* Search is linear
* More implementation complexity

Arrays are preferable when indexed access and memory locality matter. Linked lists are preferable when frequent structural changes occur and direct indexed access is not required.

---

# Stack and Queue Implementation Trade-Offs

Stacks can be implemented using arrays or linked lists.

An array-backed stack provides:

* Constant-time push and pop
* Better memory locality
* Lower node overhead
* Simpler implementation

A linked-list stack also provides constant-time push and pop when operations occur at the head, but each node requires extra memory for a reference.

Queues can also use arrays or linked lists.

A circular array queue provides constant-time enqueue and dequeue but has a fixed capacity unless resizing is added.

A linked-list queue can grow dynamically and provides constant-time operations when both front and rear pointers are maintained. However, it uses additional memory for links and has poorer cache locality.

---

# Testing

The project uses Python's `unittest` framework.

The selection test suite contains 12 tests. The data-structure test suite contains 4 tests.

The complete test command is:

```
python3 -m unittest discover -s tests -v
```

The final execution result was:

```text
Ran 16 tests in 0.000s

OK
```

The tests verify:

* Correct selection results
* Duplicate handling
* Invalid input handling
* Boundary conditions
* Preservation of the original array
* Dynamic-array insertion and deletion
* Stack push and pop behavior
* Queue enqueue and dequeue behavior
* Linked-list insertion, search, and deletion

---

# Demonstration Program

The `demo.py` file runs all algorithms and data structures in one program.

It demonstrates:

* Deterministic selection
* Randomized Quickselect
* Dynamic-array operations
* Matrix operations
* Stack operations
* Circular-queue operations
* Singly linked-list operations

The final demonstration completed successfully and both selection algorithms returned the correct result.

---

# Conclusion

This assignment demonstrated that selection does not require sorting an entire array. Median of Medians guarantees worst-case linear time, while Randomized Quickselect provides expected linear time with lower practical overhead.

The empirical results showed that Randomized Quickselect was consistently faster for the tested inputs. Median of Medians remained valuable because of its deterministic worst-case guarantee.

The elementary data-structure implementations demonstrated how storage organization affects operation complexity. Dynamic arrays provide fast indexed access, stacks support last-in, first-out processing, queues support first-in, first-out processing, and linked lists allow flexible node-based storage.

The project also showed that theoretical complexity and practical performance must both be considered. Algorithms with the same asymptotic complexity may perform differently because of constant factors, memory allocation, pivot-selection work, and implementation design.

---

# References

Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2022). *Introduction to algorithms* (4th ed.). MIT Press.

Hoare, C. A. R. (1961). Algorithm 65: Find. *Communications of the ACM, 4*(7), 321–322. https://doi.org/10.1145/366622.366647

Knuth, D. E. (1998). *The art of computer programming: Sorting and searching* (2nd ed., Vol. 3). Addison-Wesley.

Sedgewick, R., & Wayne, K. (2011). *Algorithms* (4th ed.). Addison-Wesley.