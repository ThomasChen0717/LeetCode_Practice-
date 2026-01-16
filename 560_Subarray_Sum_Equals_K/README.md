# 560. Subarray Sum Equals K

**Difficulty:** <span style="color:#f39c12"><b>Medium</b></span>  
**Topics:** Prefix Sum, HashMap, Array

---

## Problem Description

Given an array of integers `nums` and an integer `k`, return the total number of subarrays whose sum equals to `k`.

A subarray is a contiguous **non-empty** sequence of elements within an array.

---

## Examples
Example 1:
```
Input: nums = [1,1,1], k = 2
Output: 2
```
Example 2:
```
Input: nums = [1,2,3], k = 3
Output: 2
```

## Constraints

- `1 <= nums.length <= 2 * 10^4`
- `1000 <= nums[i] <= 1000`
- `10^7 <= k <= 10^7`

---

## Approach 1: Brute Force 

### Intuition

Iterate over all possible subarrays and check if their sum equals `k`. 


### Complexity Analysis

- **Time Complexity:** `O(n^3)`
- **Space Complexity:** `O(1)`

---

## Approach 2: Using Cumulative Sum 

### Intuition

Use a prefix sum to keep track of the cumulative sum up to all indices possible. 

We check each subarray sum by subtracting the prefix sum at the start of the subarray from the prefix sum at the end of the subarray. 
If the difference equals `k`, then we have found a valid subarray. 

### Complexity Analysis

- **Time Complexity:** `O(n^2)`
- **Space Complexity:** `O(n)`

---

## Approach 3: No Extra Space 

### Intuition

We can optimize the approach 2 by doing inplace sum calculations during the loop.

We keep a running sum in the window and we reset everytime we update the left pointer. 

If the running sum equals `k`, then we have found a valid subarray. 
We increment the count of valid subarrays.


### Complexity Analysis

- **Time Complexity:** `O(n^2)`
- **Space Complexity:** `O(1)`

---

## Approach 4: HashMap

### Intuition

We use a hashmap to store the prefix sum during the loop. We also keep the frequency of each prefix sum. 

We check the subarray sum by subtracting the current sum by the target sum `k`.
If the difference exists in the hashmap, then we have found a valid subarray. 
We increment the count of valid subarrays by the frequency of the difference.

### Complexity Analysis

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(n)`

---

## Implementation

See `solution.py` for the full implementation.
