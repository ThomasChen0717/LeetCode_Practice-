# 40. Combination Sum II

**Difficulty:** <span style="color:#f39c12"><b>Medium</b></span>  
**Topics:** Array, Backtracking, Sorting

---

## Problem Description

Given a collection of candidate numbers (`candidates`) and a target number (`target`), find all unique combinations in `candidates` where the candidate numbers sum to `target`.

Each number in `candidates` may only be used **once** in the combination.

**Note**: The solution set must not contain duplicate combinations.

---

## Examples
Example 1:
```
Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
```
Example 2:
```
Input: candidates = [2,5,2,1,2], target = 5
Output: 
[
[1,2,2],
[5]
]
```
 

## Constraints

- `1 <= candidates.length <= 100`
- `1 <= candidates[i] <= 50`
- `1 <= target <= 30`

---

## Approach: Backtracking

### Intuition

We first sort the candidates array. This allows us to skip over duplicate numbers in a more efficient manner. 
We then use backtracking to find all unique combinations that sum up to the target. 
For each number in the candidates array, we have two choices: either include it in the current combination or exclude it. 
We recursively explore both choices, while maintaining the sum of the current combination. 
If the sum exceeds the target, we backtrack. If the sum equals the target, we add the current combination to the result.

### Complexity Analysis
Let `N` be the length of the candidates array.
- **Time Complexity:** `O(2^N)`
- **Space Complexity:** `O(N)`

---

## Implementation

See `solution.py` for the full implementation.
