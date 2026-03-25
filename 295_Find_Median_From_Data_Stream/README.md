# 295. Find Median from Data Stream

**Difficulty:** <span style="color:#e74c3c"><b>Hard</b></span>  
**Topics:** Design, Binary Search, Data Stream, Sorting, Heap (Priority Queue)

---

## Problem Description

The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.

- For example, for `arr = [2,3,4]`, the median is `3`.
- For example, for `arr = [2,3]`, the median is `(2 + 3) / 2 = 2.5`.

Implement the `MedianFinder` class:
- `MedianFinder()` initializes the `MedianFinder` object.
- `void addNum(int num)` adds the integer `num` from the data stream to the data structure.
- `double findMedian()` returns the median of all elements so far. Answers within 10^-5 of the actual answer will be accepted.

---

## Examples

**Example 1:**
```
Input
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
Output
[null, null, null, 1.5, null, 2.0]

Explanation
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3);    // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0
```

---

## Constraints

- `-10^5 <= num <= 10^5`
- There will be at least one element in the data structure before calling `findMedian`.
- At most `5 * 10^4` calls will be made to `addNum` and `findMedian`.

---

## Approach 1: Insertion Sort with Binary Search

### Intuition

A straightforward way to find the median is to maintain a sorted list of all numbers seen so far. When a new number arrives, we insert it into the correct position to keep the list sorted. The median can then be easily calculated from the middle element(s) of the list.

To efficiently find the correct insertion point for a new number, we can use binary search, which is much faster than a linear scan.

The algorithm is as follows:
1.  Store the numbers in a dynamic array (list in Python).
2.  When `addNum(num)` is called, use binary search to find the position where `num` should be inserted to maintain the sorted order.
3.  Insert the number at that position.
4.  When `findMedian()` is called, access the middle element(s) based on the size of the list.
    - If the list has an odd number of elements (`n`), the median is the element at index `n // 2`.
    - If it has an even number, the median is the average of the elements at indices `n // 2 - 1` and `n // 2`.

### Complexity Analysis

-   **Time Complexity:** `O(N)`
    -   `addNum`: `O(N)`. While binary search (`findPos`) takes `O(log N)` to find the insertion point, the `insert` operation on a list takes `O(N)` time because all subsequent elements need to be shifted.
    -   `findMedian`: `O(1)`. Accessing elements by index is a constant-time operation.
-   **Space Complexity:** `O(N)`, where `N` is the number of elements added so far. We need to store all the numbers.

---

## Approach 2: Two Heaps

### Intuition

The insertion sort approach is too slow because of the `O(N)` insertion cost. We need a more efficient way to find the middle elements without keeping the entire list sorted.

The key insight is that we don't need to sort the whole stream. We only need to separate the numbers into two halves: a "small" half and a "large" half. The median is always determined by the largest number in the small half and the smallest number in the large half.

This is a perfect use case for heaps:
-   A **max-heap** (`lo`) to store the smaller half of the numbers. The top of this heap is the largest value in the small half.
-   A **min-heap** (`hi`) to store the larger half of the numbers. The top of this heap is the smallest value in the large half.

We need to maintain two invariants:
1.  **Balancing:** The sizes of the two heaps should be either equal or differ by at most 1. By convention, the max-heap (`lo`) can have one more element than the min-heap (`hi`).
2.  **Partitioning:** Every number in the max-heap (`lo`) must be less than or equal to every number in the min-heap (`hi`).

**Adding a number (`addNum`):**
1.  Add the new number to the max-heap (`lo`).
2.  To maintain the partitioning invariant, immediately pop the largest element from `lo` and push it onto the min-heap (`hi`).
3.  To maintain the balancing invariant, if the size of `lo` becomes smaller than `hi`, pop the smallest element from `hi` and push it onto `lo`.

**Finding the median (`findMedian`):**
-   If the heaps have different sizes (i.e., `len(lo) > len(hi)`), the total number of elements is odd. The median is the top element of the max-heap (`lo`).
-   If the heaps have the same size, the total number of elements is even. The median is the average of the top elements of both heaps.

*Note: In Python, `heapq` only implements min-heaps. To simulate a max-heap, we store negated values.*

### Complexity Analysis

-   **Time Complexity:**
    -   `addNum`: `O(log N)`. Each heap push and pop operation takes logarithmic time.
    -   `findMedian`: `O(1)`. Accessing the top of the heaps is a constant-time operation.
-   **Space Complexity:** `O(N)`, to store all the numbers in the heaps.

---

## Implementation

See `solution.py` for the full implementation of both approaches.
