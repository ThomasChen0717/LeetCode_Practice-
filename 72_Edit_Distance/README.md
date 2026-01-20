# 72. Edit Distance

**Difficulty:** <span style="color:#f39c12"><b>Medium</b></span>  
**Topics:** String, Dynamic Programming, Recursion

---

## Problem Description

Given two strings `word1` and `word2`, return the minimum number of operations required to convert `word1` to `word2`.

You have the following three operations permitted on a word:

- Insert a character
- Delete a character
- Replace a character

---

## Examples
Example 1:
```
Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
```
Example 2:
```
Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
```

## Constraints

- `1 <= word1.length, word2.length <= 500`
- `word1` and `word2` consist of only lowercase English letters.

---

## Approach 1: Recursion

### Intuition

We can use recursion to solve this problem. 
We start from the end of both strings and compare the characters. 
If the characters are equal, we move to the previous characters. 
If the characters are not equal, we have three options:
- Insert a character
  - We insert a character in `word1` to match the character in `word2`.
  - We move to the previous character in `word2`.
- Delete a character
  - We delete a character in `word1` to match the character in `word2`.
  - We move to the previous character in `word1`.
- Replace a character
  - We replace a character in `word1` with the character in `word2`.
  - We move to the previous characters in both strings.

### Complexity Analysis
Let `m` be the length of `word1` and `n` be the length of `word2`.
Let `M` be `max(m, n)`.
- **Time Complexity:** `O(3^M)`
- **Space Complexity:** `O(M)`

---

## Approach 2: Top-Down Dynamic Programming

### Intuition

We can use top-down dynamic programming to solve this problem. 
It is similar to the recursive approach, but we use a memoization table to store the results of subproblems.

### Complexity Analysis
Let `m` be the length of `word1` and `n` be the length of `word2`.
Let `M` be `max(m, n)`.
- **Time Complexity:** `O(M * N)`
- **Space Complexity:** `O(M * N)`

---

## Approach 3: Bottom-Up Dynamic Programming

### Intuition

We can use bottom-up dynamic programming to solve this problem. 
We start from the beginning of the strings and compare the characters. 
We use a 2D array `dp` to store the minimum number of operations required to convert `word1[:i]` to `word2[:j]`. 
We initialize `dp[i][0]` to `i` and `dp[0][j]` to `j`.

At each index `i` and `j`, from `1` to `m` and `1` to `n`, we have three options:
- If the characters are equal, the edit distance is the same as the edit distance of the previous characters.
- If the characters are not equal, we have three options:
  - Insert a character
    - We insert a character in `word1` to match the character in `word2`.
    - Meaning that `word1` from `0 - i` is matched with `word2` from `0 - (j - 1)`.
    - So the edit distance is `dp[i][j - 1] + 1`.
  - Delete a character
    - We delete a character in `word1` to match the character in `word2`.
    - Meaning that `word1` from `0 - (i - 1)` is matched with `word2` from `0 - j`.
    - So the edit distance is `dp[i - 1][j] + 1`.
  - Replace a character
    - We replace a character in `word1` with the character in `word2`.
    - Meaning that `word1` from `0 - (i - 1)` is matched with `word2` from `0 - (j - 1)`.
    - So the edit distance is `dp[i - 1][j - 1] + 1`.

    We take the minimum of the three options.

### Complexity Analysis
Let `m` be the length of `word1` and `n` be the length of `word2`.
Let `M` be `max(m, n)`.
- **Time Complexity:** `O(M * N)`
- **Space Complexity:** `O(M * N)`

---

## Implementation

See `solution.py` for the full implementation.
