# 1143. Longest Common Subsequence

**Difficulty:** <span style="color:#f39c12"><b>Medium</b></span>  
**Topics:** Dynamic Programming, Memoization

---

## Problem Description

Given two strings `text1` and `text2`, return the length of their longest **common subsequence**. If there is no **common subsequence**, return `0`.

A **subsequence** of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

- For example, `"ace"` is a subsequence of `"abcde"`.

A **common subsequence** of two strings is a subsequence that is common to both strings.

---

## Examples
Example 1:
```
Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.
```
Example 2:
```
Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.
```
Example 3:
```
Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.
```

## Constraints

- `1 <= text1.length, text2.length <= 1000`
- `text1` and `text2` consist of only lowercase English characters.

---

## Approach 1: Top-Down Dynamic Programming(Memoization)

### Intuition

We do a top-down dynamic programming approach. There are two possible cases:
1. We skip the first letter of `text1` 
2. We count the firtst letter of `text1` and skip to the first occurence of the same letter in `text2`.

We use a memoization table `memo` to store the results of subproblems. `memo[i][j]` represents the length of the longest common subsequence of `text1[i:]` and `text2[j:]`.

### Complexity Analysis
Let `M` be the length of `text1` and `N` be the length of `text2`.
- **Time Complexity:** `O(M * N^2)`
 - There are `M * N` subproblems. For each subproblem, we need to find the first occurence of the first letter of `text1` in `text2`, which takes `O(N)` time.
- **Space Complexity:** `O(M * N)`

---

## Approach 2: Improved Top-Down Dynamic Programming(Memoization)

### Intuition

We change the state a bit. 

Now we have two choices: 
1. The letter at `idx1` and `idx2` are the same. We can count them and move to the next letter in both strings.
2. The letter at `idx1` and `idx2` are different. We can skip the letter at `idx1` or the letter at `idx2` and compute the max of the two choices. 

We use a memoization table `memo` to store the results of subproblems. `memo[i][j]` represents the length of the longest common subsequence of `text1[i:]` and `text2[j:]`.

### Complexity Analysis
- **Time Complexity:** `O(M * N)`
 - There are `M * N` subproblems. For each subproblem, it takes `O(1)` time.
- **Space Complexity:** `O(M * N)`

---

## Approach 3: Bottom-Up Dynamic Programming(Table)

### Intuition

We do a bottom-up dynamic programming approach. We use a table `dp` to store the results of subproblems. `dp[i][j]` represents the length of the longest common subsequence of `text1[:i]` and `text2[:j]`. 
We need to pad the table with `0` in the first row and first column. 


### Complexity Analysis
- **Time Complexity:** `O(M * N)`
 - There are `M * N` subproblems. For each subproblem, it takes `O(1)` time.
- **Space Complexity:** `O(M * N)`

---

## Approach 4: Space-Optimized Bottom-Up Dynamic Programming(Table) 

### Intuition

We notice that `dp[i][j]` only depends on `dp[i-1][j-1]`, `dp[i-1][j]`(previous row), and `dp[i][j-1]`(current row). So we can use a 1D table `dp` to store the results of previous row and a variable `prev` to store the value of `dp[i-1][j-1]`.

### Complexity Analysis
- **Time Complexity:** `O(M * N)`
 - There are `M * N` subproblems. For each subproblem, it takes `O(1)` time.
- **Space Complexity:** `O(min(M, N))`


## Implementation

See `solution.py` for the full implementation.
