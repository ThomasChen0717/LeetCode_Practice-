# 658. Find K Closest Elements

**Difficulty:** <span style="color:#f39c12"><b>Medium</b></span>  
**Topics:** <Binary Search, Sliding Window, Sorting>  

---

## Problem Description

<Problem Description>

Given a sorted integer array `arr`, two integers `k` and `x`, return the `k` closest integers to `x` in the array. The result should also be sorted in ascending order.


An integer `a` is closer to `x` than an integer `b` if:

```
|a - x| < |b - x|, or
|a - x| == |b - x| and a < b
```
---

## Examples
Example1: 
```
Input: arr = [1,2,3,4,5], k = 4, x = 3

Output: [1,2,3,4]
```
Example2: 
```
Input: arr = [1,1,2,3,4,5], k = 4, x = -1

Output: [1,1,2,3]
```

## Constraints

- `1 <= k <= arr.length`
- `1 <= arr.length <= 10^4`
- `arr` is sorted in ascending order.
- `-10^4 <= arr[i], x <= 10^4`
---

## Approach 1: Sorting

### Intuition
Sort the array based on the absolute difference between each element and `x`. Then, return the first `k` elements of the sorted array. Sort the result in ascending order.
### Complexity Analysis
Given `N` as the length of `arr`,
- **Time Complexity:** `O(N log N + k log k)`
    
    - Sorting the array takes `O(N log N)` time.
    - Sorting the result takes `O(k log k)` time.
- **Space Complexity:** `O(N)`
    
    - Storing the sorted array takes `O(N)` space.

---

### Approach 2: Binary Search + Sliding Window 

### Intuition
Use binary search to find the closest element to `x` in the array. Then, use a sliding window to find the `k` closest elements to `x`. Sort the result in ascending order.
### Complexity Analysis
Given `N` as the length of `arr`,
- **Time Complexity:** `O(log N + k)`
    
    - Binary search takes `O(log N)` time.
    - Sliding window takes `O(k)` time.
- **Space Complexity:** `O(1)`
---

### Approach 3: Binary Search 

### Intuition
Use binary search to directly find the left boundary of the result array. 

### Key Observations
- If there needs to be `k` elements in the result, the left boundary of the result have an upper bound of `len(arr) - k`. 
- Consider `mid` and `mid + k`. Only one of them could possibly be in the final answer. 
    - If `mid` is closer to `x` than `mid + k`, then the left boundary must be before `mid + k`. Otherwise, the left boundary must be after `mid`. 


### Complexity Analysis
Given `N` as the length of `arr`,
- **Time Complexity:** `O(log N + k)`
    
    - Binary search takes `O(log N)` time.
    - Sliding window takes `O(k)` time.
- **Space Complexity:** `O(1)`
---

## Implementation

See `solution.py` for the full implementation.