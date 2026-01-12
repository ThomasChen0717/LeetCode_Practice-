# 4. Median of Two Sorted Arrays

**Difficulty:** <span style="color:#e74c3c"><b>Hard</b></span>  
**Topics:** Arrays, Binary Search, Divide and Conquer

---

## Problem Description

Given two sorted arrays `nums1` and `nums2` of size `m` and `n` respectively, return the **median** of the two sorted arrays.

The overall run time complexity should be `O(log (m+n))`.

---

## Examples
Example 1:
```
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
```
Example 2:
```
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
```

## Constraints

- `nums1.length == m`
- `nums2.length == n`
- `0 <= m <= 1000`
- `0 <= n <= 1000`
- `1 <= m + n <= 2000`
- `-10^6 <= nums1[i], nums2[i] <= 10^6`

---

## Approach

### Intuition

The classic “merge‐then‐pick‐middle” idea gives O(m+n) time, but the problem demands O(log(m+n)).  
We therefore turn the task into a binary-search problem on the smaller array.  
Key insight: the median splits the combined elements so that every value on the left half is ≤ every value on the right half.  
To find the k-th smallest element (k=(m+n+1)//2) we repeatedly discard halves that cannot contain it:  
- Compare the k//2-th candidates in each array.  
- The smaller candidate and everything before it in its array can be safely discarded, because the k-th element must lie beyond that point.  
- Adjust k by the number of elements removed and repeat until one array is empty or k=1.  
Binary search on the smaller array keeps the search space logarithmic, yielding the required O(log(min(m,n))) complexity.


### Complexity Analysis

- **Time Complexity:** `O(log (m*n))`
- **Space Complexity:** `O(logm+logn) = O(log(m * n))`

---

## Implementation

See `solution.py` for the full implementation.
