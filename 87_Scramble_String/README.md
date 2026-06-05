# 87. Scramble String

**Difficulty:** <span style="color:#e74c3c"><b>Hard</b></span>  
**Topics:** String, Dynamic Programming

---

## Problem Description

We can scramble a string `s` to get a string `t` using the following algorithm:
1. If the length of the string is 1, stop.
2. If the length of the string is > 1, do the following:
   - Split the string into two non-empty substrings at a random index, i.e., if the string is `s`, divide it into `x` and `y` where `s = x + y`.
   - **Randomly** decide to swap the two substrings or to keep them in the same order. i.e., after this step, `s` may become `s = x + y` or `s = y + x`.
   - Apply step 1 recursively on each of the two substrings `x` and `y`.

Given two strings `s1` and `s2` of the same length, return `true` if `s2` is a scrambled string of `s1`, otherwise, return `false`.

---

## Examples

**Example 1:**
```
Input: s1 = "great", s2 = "rgeat"
Output: true
```
**Explanation:**
One possible scenario is:
"great" --> "gr/eat"
"gr/eat" --> "g/r" / "e/at"
"g/r" / "e/at" --> "r/g" / "e/at" (swap "g" and "r")
"r/g" / "e/at" --> "rgeat"

**Example 2:**
```
Input: s1 = "abcde", s2 = "caebd"
Output: false
```

**Example 3:**
```
Input: s1 = "a", s2 = "a"
Output: true
```

## Constraints

- `s1.length == s2.length`
- `1 <= s1.length <= 30`
- `s1` and `s2` consist of lowercase English letters.

---

## Approach: Bottom-up Dynamic Programming

### Intuition

This problem has optimal substructure and overlapping subproblems, making it a good candidate for dynamic programming. The core idea is to determine if a substring of `s2` can be a scrambled version of a corresponding substring of `s1`.

We can define a 3D DP table, `dp[len][i][j]`, which will be `true` if the substring of `s2` of length `len` starting at index `j` is a scramble of the substring of `s1` of length `len` starting at index `i`, and `false` otherwise.

- **State:** `dp[len][i][j]` = Is `s2.substr(j, len)` a scramble of `s1.substr(i, len)`?

- **Base Case:** For `len = 1`, `dp[1][i][j]` is simply `s1[i] == s2[j]`.

- **Transitions:** For a given length `len`, we can try all possible split points `k` from `1` to `len - 1`. For each split, there are two possibilities for the substrings to match:

  1.  **No Swap:** The first part of the `s1` substring matches the first part of the `s2` substring, AND the second part of `s1` matches the second part of `s2`.
      - `isScramble(s1[i:i+k], s2[j:j+k])` AND `isScramble(s1[i+k:i+len], s2[j+k:j+len])`
      - In terms of our DP table: `dp[k][i][j] && dp[len-k][i+k][j+k]`

  2.  **Swap:** The first part of the `s1` substring matches the *second* part of the `s2` substring, AND the second part of `s1` matches the *first* part of `s2`.
      - `isScramble(s1[i:i+k], s2[j+len-k:j+len])` AND `isScramble(s1[i+k:i+len], s2[j:j+len-k])`
      - In terms of our DP table: `dp[k][i][j+len-k] && dp[len-k][i+k][j]`

If either of these conditions is true for any split point `k`, then `dp[len][i][j]` is true.

We build this DP table from `len = 1` up to `n`. The final answer is `dp[n][0][0]`, which tells us if the entire string `s2` is a scramble of `s1`.

### Complexity Analysis

- **Time Complexity:** `O(N^4)`. We have three nested loops for `len`, `i`, and `j`, and an inner loop for the split point `k`. Each loop runs up to `N` times.
- **Space Complexity:** `O(N^3)` for the 3D DP table.

---

## Implementation

See `solution.c++` for the full implementation.
