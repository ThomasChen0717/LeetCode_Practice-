# 97. Interleaving String

**Difficulty:** <span style="color:#f39c12"><b>Medium</b></span>  
**Topics:** Array, Dynamic Programming, Recursion, Memoization

---

## Problem Description

Given strings `s1`, `s2`, and `s3`, find whether `s3` is formed by an **interleaving** of `s1` and `s2`.

An **interleaving** of two strings `s` and `t` is a configuration where `s` and `t` are divided into `n` and `m` substrings respectively, such that:

- `s = s1 + s2 + ... + sn`
- `t = t1 + t2 + ... + tm`
- `|n - m| <= 1`
- The **interleaving** is `s1 + t1 + s2 + t2 + s3 + t3 + ...` or `t1 + s1 + t2 + s2 + t3 + s3 + ...`

**Note:** `a + b` is the concatenation of strings `a` and `b`.

---

## Examples
Example 1:
![Example 1](https://assets.leetcode.com/uploads/2020/09/02/interleave.jpg)
```
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true
Explanation: One way to obtain s3 is:
Split s1 into s1 = "aa" + "bc" + "c", and s2 into s2 = "dbbc" + "a".
Interleaving the two splits, we get "aa" + "dbbc" + "bc" + "a" + "c" = "aadbbcbcac".
Since s3 can be obtained by interleaving s1 and s2, we return true.
```
Example 2:

```
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false
Explanation: Notice how it is impossible to interleave s2 with any other string to obtain s3.
```
Example 3:

```
Input: s1 = "", s2 = "", s3 = ""
Output: true
```

## Constraints

- `0 <= s1.length, s2.length <= 100`
- `0 <= s3.length <= 200`
- `s1`, `s2`, and `s3` consist of lowercase English letters.

---

## Approach 1: Brute Force Recursion

### Intuition

We recurse on each position of `s3` and check if we can form it by interleaving `s1` and `s2`. 
If we reach the end of `s3`, we know that we have successfully interleaved `s1` and `s2` to form `s3`.

### Complexity Analysis

- **Time Complexity:** `O(2^(n+m))`
- **Space Complexity:** `O(n+m)`

---

## Approach 2: Recursion with Memoization

### Intuition

This is using memoization over approach 1. We notice many states were computed multiple times. 
Therefore, we can use memoization to store the results of these states. 
We define `memo[i][j]` as whether `s3[i+j:]` can be formed by interleaving `s1[i:]` and `s2[j:]`. 

### Complexity Analysis

- **Time Complexity:** `O(n * m)`
- **Space Complexity:** `O(n * m)`

---

## Approach 3: Bottom-Up Dynamic Programming

### Intuition

We can use dynamic programming to solve this problem. We define `dp[i][j]` as whether `s3[:i+j]` can be formed by interleaving `s1[:i]` and `s2[:j]`.

### Complexity Analysis

- **Time Complexity:** `O(n * m)`
- **Space Complexity:** `O(n * m)`

---

## Approach 4: Bottom-Up Dynamic Programming with Space Optimization

### Intuition

We can optimize the space complexity of approach 3 by using a 1D array instead of a 2D array, since we only need the current row and the previous row, which the values we can get by using the value before overwriting.
We define `dp[j]` as whether `s3[:i+j]` can be formed by interleaving `s1[:i]` and `s2[:j]`.

### Complexity Analysis

- **Time Complexity:** `O(n * m)`
- **Space Complexity:** `O(m)`

---

## Implementation

See `solution.py` for the full implementation.
