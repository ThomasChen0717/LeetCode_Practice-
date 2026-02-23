# 179. Largest Number

**Difficulty:** <span style="color:#f39c12"><b>Medium</b></span>  
**Topics:** String, Sorting, Integer

---

## Problem Description

Given a list of non-negative integers `nums`, arrange them such that they form the largest number and return it.

Since the result may be very large, you need to return a string instead of an integer.

---

## Examples
**Example 1:** 
```
Input: nums = [10,2]
Output: "210"
```

**Example 2:**
```
Input: nums = [3,30,34,5,9]
Output: "9534330"
```

## Constraints

- `1 <= nums.length <= 100`
- `0 <= nums[i] <= 10^9`

---

## Approach 1: Quick Sort

### Intuition

This approach adapts the Quick Sort algorithm to sort the numbers based on the custom comparison rule (`a` + `b` > `b` + `a`). The standard Quick Sort partitioning is used, but the comparison logic is swapped with our custom function. After sorting, the numbers are joined to form the largest number string.

### Complexity Analysis
Let `N` be the number of elements in `nums` and `k` be the average number of digits in the numbers.
-   **Time Complexity:** `O(Nk log N)` on average, but `O(N^2k)` in the worst case. 
-   **Space Complexity:** `O(k log N)` for on average, and `O(Nk)` in the worst case.

---

## Approach 2: Merge Sort

### Intuition

Merge Sort is a stable, divide-and-conquer sorting algorithm. Here, we recursively divide the list into halves until each sublist contains a single element. Then, we merge the sublists back together, sorting them according to our custom comparison rule. 

### Complexity Analysis
Let `N` be the number of elements in `nums` and `k` be the average number of digits in the numbers.
-   **Time Complexity:** `O(Nk log N)` in all cases (worst, average, and best).
-   **Space Complexity:** `O(Nk)` to store the temporary arrays required for the merge step.

---

## Approach 3: Heap Sort

### Intuition

This method uses a min-heap (or a max-heap with a modified comparator) to sort the numbers. We can define a custom object that wraps the string representation of the numbers and overrides the less-than (`__lt__`) operator to follow our comparison rule (`a` + `b` > `b` + `a`). By inserting all numbers into the heap and then extracting them one by one, we get the numbers in the desired sorted order.

### Complexity Analysis
Let `N` be the number of elements in `nums` and `k` be the average number of digits in the numbers.
-   **Time Complexity:** `O(Nk log N)`. Building the heap takes `O(N)`, and each of the `N` extractions takes `O(k log N)`.
-   **Space Complexity:** `O(Nk)` to store the elements in the heap.

---

## Approach 4: Tim Sort

### Intuition

Tim Sort is a hybrid algorithm derived from Merge Sort and Insertion Sort. It is the default sorting algorithm in Python. It divides the array into small "runs," sorts them using Insertion Sort, and then merges the runs using a modified Merge Sort. By providing a custom key or using `functools.cmp_to_key` with our comparison function, we can leverage Python's highly optimized `sort()` method to arrange the numbers correctly.

### Complexity Analysis

-   **Time Complexity:** `O(Nk log N)` in the worst case. It performs very well on partially sorted arrays.
-   **Space Complexity:** `O(Nk)` in the worst case for temporary storage during merging.

---

## Implementation

See `solution.py` for the full implementation.
