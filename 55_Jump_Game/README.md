# 55. Jump Game

**Difficulty:** <span style="color:#f39c12"><b>Medium</b></span>  
**Topics:** Array, Dynamic Programming, Greedy  

---

## Problem Description

You are given an integer array `nums`. You are initially positioned at the array's **first index**, and each element in the array represents your maximum jump length at that position.

Return `true` if you can reach the last index, or `false`otherwise.

---

## Examples
Example 1:
```
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
```
Example 2:
```
Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
```

## Constraints

- `1 <= nums.length <= 10^4`
- `0 <= nums[i] <= 10^5`

---

## Approach 1: Top-Down Dynamic Programming

### Intuition

We start from the first index and try to reach the last index. We recursively check if we can reach the last index from the current index. 
If we can reach the last index from the current index, we mark the current index as good.
Otherwise, we mark it as bad. 

We use a memoization array `memo` to store the results of subproblems.
If `memo[i]` is `true`, it means that we can reach the last index from index `i`.
If `memo[i]` is `false`, it means that we cannot reach the last index from index `i`.

### Complexity Analysis

- **Time Complexity:** `O(n^2)`
- **Space Complexity:** `O(n)`

---

## Approach 2: Bottom-Up Dynamic Programming

### Intuition

We start from the last index and iterate backward. For each index, we check if we can reach the last index from the current index.
If we can reach the last index from the current index, we mark the current index as good.
Otherwise, we mark it as bad. 

We use a memoization array `memo` to store the results of subproblems.
If `memo[i]` is `true`, it means that we can reach the last index from index `i`.
If `memo[i]` is `false`, it means that we cannot reach the last index from index `i`.

### Complexity Analysis

- **Time Complexity:** `O(n^2)`
- **Space Complexity:** `O(n)`

---

## Approach 3: Greedy

### Intuition

We start from the last index and iterate backward. For each index, we check if we can reach the last index from the current index.
If we can reach the last index from the current index, we update the last index to the current index.
At the end, if the last index is 0, it means that we can reach the last index from the first index.

--- 
Alternate Intuition

We start from the first index and try to reach the last index. We iterate forward. We keep track of the farthest index we can reach. 
We also keep track of current step end. If we reach the current step end, we update the current step end to the farthest index we can reach. 
If at any point, the current step end exceeds the last index, it means that we can reach the last index. 

### Complexity Analysis

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(1)`

---

## Implementation

See `solution.py` for the full implementation.
