# 5. Longest Palindromic Substring

**Difficulty:** <span style="color:#f39c12"><b>Medium</b></span>  
**Topics:** String, Dynamic Programming  

---

## Problem Description

Given a string `s`, return the longest palindromic substring in `s`.

---

## Examples
Example 1:
```
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
```
Example 2:
```
Input: s = "cbbd"
Output: "bb"
```

## Constraints

- `1 <= s.length <= 1000`
- `s` consists of only digits and English letters.

---

## Approach 1: Brute Force

### Intuition

Iterate over all possible substrings of `s` and check if each substring is a palindrome. 

### Complexity Analysis
Let `n` be the length of `s`.
- **Time Complexity:** `O(n^3)`
- **Space Complexity:** `O(1)`

---

## Approach 2: Dynamic Programming

### Intuition

Use dynamic programming to store whether substrings are palindromes. 
Let `dp[i][j]` be `True` if the substring `s[i:j+1]` is a palindrome, and `False` otherwise. 
Then,
- `dp[i][i] = True` for all `i`
- `dp[i][i+1] = True` if `s[i] == s[i+1]` for all `i`
- `dp[i][j] = dp[i+1][j-1] and s[i] == s[j]` for all `i < j`

### Complexity Analysis
- **Time Complexity:** `O(n^2)`
- **Space Complexity:** `O(n^2)`

---

## Approach 3: Expand Around Center

### Intuition

Iterate over all possible centers of palindromes in `s` and expand outwards to find the longest palindrome.

### Complexity Analysis
- **Time Complexity:** `O(n^2)`
- **Space Complexity:** `O(1)`

---

## Implementation

See `solution.py` for the full implementation.
