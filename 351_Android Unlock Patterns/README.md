# 351. Android Unlock Patterns

**Difficulty:** <span style="color:#f39c12"><b>Medium</b></span>  
**Topics:** Backtracking, DP/Memoization
---

## Problem Description

Android devices have a special lock screen with a `3 x 3` grid of dots. Users can set an "unlock pattern" by connecting the dots in a specific sequence, forming a series of joined line segments where each segment's endpoints are two consecutive dots in the sequence. A sequence of `k` dots is a **valid** unlock pattern if both of the following are true:

- All the dots in the sequence are **distinct**.

- If the line segment connecting two consecutive dots in the sequence passes through the **center** of any other dot, the other dot **must have previously appeared** in the sequence. No jumps through the center non-selected dots are allowed.
    - For example, connecting dots `2` and `9` without dots `5` or `6` appearing beforehand is valid because the line from dot `2` to dot `9` does not pass through the center of either dot `5` or `6`.
    - However, connecting dots `1` and `3` without dot `2` appearing beforehand is invalid because the line from dot `1` to dot `3` passes through the center of dot `2`.

Here are some example valid and invalid unlock patterns:

![Valid Unlock Pattern](android_unlock_pattern.png)

- The 1st pattern `[4,1,3,6]` is invalid because the line connecting dots `1` and `3` pass through dot `2`, but dot `2` did not previously appear in the sequence.
- The 2nd pattern `[4,1,9,2]` is invalid because the line connecting dots `1` and `9` pass through dot `5`, but dot `5` did not previously appear in the sequence.
- The 3rd pattern `[2,4,1,3,6]` is valid because it follows the conditions. The line connecting dots `1` and `3` meets the condition because dot `2` previously appeared in the sequence.
- The 4th pattern `[6,5,4,1,9,2]` is valid because it follows the conditions. The line connecting dots `1` and `9` meets the condition because dot `5` previously appeared in the sequence.

Given two integers `m` and `n`, return the **number of unique and valid unlock patterns** of the Android grid lock screen that consist of **at least** `m` keys and **at most** `n` keys.

Two unlock patterns are considered **unique** if there is a dot in one sequence that is not in the other, or the order of the dots is different.

---

## Examples
Example 1:
```
Input: m = 1, n = 1
Output: 9
```
Example 2:
```
Input: m = 1, n = 2
Output: 65
```

## Constraints

- `1 <= m, n <= 9`

---

## Approach 1: Naive Backtracking

### Intuition
We enumerate all single moves(moves that do not pass through any other dot) and all skip moves(moves that pass through one dot). We do backtracking starting from each of the nine dots. For each dot, we mark it as visited and recursively visit all the dots that are not visited yet. We stop the recursion when the number of visited dots is greater than `n`. We increment valid_patterns when the pattern length is at least `m`.

### Complexity Analysis
Let `n` be the maximum numbers of keys allowed in the pattern.
- **Time Complexity:** `O(9 * 8^n)` Run backtrack on each of the 9 dots. For each dot, we have at most 8 choices to choose from and at most a depth of `n`.
- **Space Complexity:** `O(n)` because of the recursion stack.
---

## Approach 2: Optimized Backtracking

### Intuition
We can optimize the backtracking by precomputing the skip moves. We use a 2D array `skip` to store the skip moves. `skip[i][j]` is the dot that must be visited between dot `i` and dot `j`. For example, `skip[1][3] = 2` because we must visit dot `2` between dot `1` and dot `3`.

We also notice that the backtracking pattern for all edge points, all corner points and the center are identical. So we can replace the nine calls to `CountPatternsFromDot` with three calls: 
1. A call for the corner points
1. A call for the edge points
1. A call for the center point

### Complexity Analysis
- **Time Complexity:** `O(3 * 8^n)` Run backtrack on each of the 3 groups. For each group, we have at most 8 choices to choose from and at most a depth of `n`.
- **Space Complexity:** `O(n)` because of the recursion stack.
---

## Approach 3: DP/Memoization

### Intuition
We can use dynamic programming to memoize the results of subproblems. We use a 2D array `dp` to store the number of valid patterns starting from number `i` with `j` being a 9-bit number that records which numbers have been visited. `dp[i][j]` is the number of valid patterns starting from number `i` with `j` being the visited numbers. We initialize the `dp` to be filled with `-1`. 

We defined helper methods for bit manipulating the visited number.

### Complexity Analysis
- **Time Complexity:** `O(1)` 
Due to memoization, the time complexity of the algorithm is bounded by the total time required to fill the `dp` array. The total size of dp is `10×(1<<10)` or `10240`. So, the overall time complexity of the algorithm is `O(10240)`, which can be simplified to `O(1)`.
- **Space Complexity:** `O(n)` because of the recursion stack.

## Implementation

See `solution.py` for the full implementation.
