# 912: Sort an Array

**Difficulty:** <span style="color:#f39c12"><b>Medium</b></span>  
**Topics:** Sorting, Array 

---

## Problem Description

Given an array of integers `nums`, sort the array in ascending order and return it.

You must solve the problem **without using any built-in** functions in `O(nlog(n))` time complexity and with the smallest space complexity possible.

---

## Examples
Example 1:
```
Input: nums = [5,2,3,1]
Output: [1,2,3,5]
Explanation: After sorting the array, the positions of some numbers are not changed (for example, 2 and 3), while the positions of other numbers are changed (for example, 1 and 5).
```
Example 2:
```
Input: nums = [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]
Explanation: Note that the values of nums are not necessarily unique.
```

## Constraints

- `1 <= nums.length <= 5 * 10^4`
- `-5 * 10^4 <= nums[i] <= 5 * 10^4`

---

## Approach 1: Merge Sort

### Intuition

Merge sort is a divide-and-conquer algorithm that sorts an array by recursively dividing it into two halves, sorting each half, and then merging the sorted halves back together.

### Complexity Analysis

- **Time Complexity:** `O(n log n)`
- **Space Complexity:** `O(n)`

---

## Approach 2: Heap Sort

### Intuition

Heap sort is a comparison-based sorting algorithm that uses a binary heap data structure. 
It works by first building a max heap from the input array, then repeatedly extracting the maximum element from the heap and placing it at the end of the array. 
Heapify the remaining elements to maintain the max heap property.
This process is repeated until the heap is empty, resulting in a sorted array.

### Complexity Analysis

- **Time Complexity:** `O(n log n)`
- **Space Complexity:** `O(logn)`

---

## Approach 3: Counting Sort

### Intuition

Counting sort is a non-comparison-based sorting algorithm that works by counting the occurrences of each element in the input array and using those counts to determine the sorted order.

### Complexity Analysis
Let 
- `n` be the length of the input array `nums`.
- `k` be the range of the input array `nums`.
- **Time Complexity:** `O(n + k)`
- **Space Complexity:** `O(n)`

---

## Approach 4: Radix Sort

### Intuition

Radix sort is a non-comparison-based sorting algorithm that works by sorting the elements digit by digit. 
It starts by sorting the elements based on the least significant digit, and then moves to the more significant digits. 
Radix sort is efficient for sorting integers or strings with a fixed number of digits. 
We use counting sort as the subroutine to sort the digits.

### Complexity Analysis
Let 
- `n` be the length of the input array `nums`.
- `d` be the number of digits in the maximum number in the input array `nums`.
- `b` be the base of the numbering system used to represent the numbers in the input array `nums`.
- **Time Complexity:** `O(d(n + b))`
- **Space Complexity:** `O(n + b)`

---

See `solution.py` for the full implementation.
