# 2484. Count Palindromic Subsequences

**Difficulty:** <span style="color:#e74c3c"><b>Hard</b></span>  
**Topics:** String, Dynamic Programming

---

## Problem Description

Given a string of digits `s`, return the number of palindromic subsequences of `s` having length 5. Since the answer may be very large, return it modulo `10^9 + 7`.

Note:
- A string is palindromic if it reads the same forward and backward.
- A subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.

---

## Examples

**Example 1:**
```
Input: s = "103301"
Output: 2
```
**Explanation:** 
There are 6 possible subsequences of length 5: "10330","10331","10301","10301","13301","03301". 
Two of them (both equal to "10301") are palindromic.

**Example 2:**
```
Input: s = "0000000"
Output: 21
```
**Explanation:** All 21 subsequences of length 5 are "00000", which is palindromic.

**Example 3:**
```
Input: s = "9999900000"
Output: 2
```
**Explanation:** The only two palindromic subsequences are "99999" and "00000".

## Constraints

- `1 <= s.length <= 10^4`
- `s` consists of digits.

---

## Approach 1: Backtracking

### Intuition

The most straightforward way to solve this is to generate all possible subsequences of length 5, check if each one is a palindrome, and count them.

This can be implemented using a recursive backtracking function. The function would explore all paths to build subsequences of length 5. Once a subsequence of length 5 is formed, a helper function checks if it reads the same forwards and backward. 

While this approach is logically correct, it is highly inefficient. The number of subsequences to check is enormous, leading to a time complexity that is exponential. Given the constraint `s.length <= 10^4`, this approach will result in a "Time Limit Exceeded" error.

### Complexity Analysis

- **Time Complexity:** Exponential, far too slow for the given constraints.
- **Space Complexity:** `O(N)` for the recursion stack depth in the worst case.

---

## Approach 2: Dynamic Programming

### Intuition

A palindromic subsequence of length 5 must have the structure `ab_ba`, where `a` and `b` are digits and `_` is the middle element. The core idea is to iterate through every possible middle element of the palindrome and, for each one, count the valid pairs that can form the "wings" of the palindrome.

Let's fix the middle element at index `i` (`s[i]`). We need to find the number of subsequences `ab` in the prefix `s[0...i-1]` and the number of subsequences `ba` in the suffix `s[i+1...n-1]`. The total number of palindromes with `s[i]` as the center is the sum of `(count of "ab" on the left) * (count of "ba" on the right)` over all possible pairs of digits `a` and `b`.

To do this efficiently, we can use dynamic programming with prefix and suffix counts:

1.  **Suffix Counts (`suffix` array):** We precompute the number of two-digit subsequences. Let `suffix[i][d1][d2]` be the count of subsequences `d1, d2` in the suffix of the string starting from index `i`. We can compute this by iterating backward from the end of the string. For each character `s[i]`, we can form new pairs with all the single digits that appear to its right.

2.  **Prefix Counts and Main Loop:** We iterate through the string from left to right, treating each character `s[i]` as the potential middle element of the palindrome.
    - We maintain a `prefix` table where `prefix[d1][d2]` stores the count of `d1, d2` subsequences in the string to the left of `s[i]`.
    - In each iteration `i`, we calculate the contribution to the total result. For every pair of digits `(a, b)`, we multiply the number of `ab` prefixes found so far (`prefix[a][b]`) by the number of `ba` suffixes available in `s[i+1:]` (which is `suffix[i+1][b][a]`).
    - After calculating the result for the current middle element `s[i]`, we update the `prefix` table for the *next* iteration by incorporating `s[i]` to form new pairs with the single digits seen to its left.

This method avoids redundant calculations by building up counts of pairs and allows us to find the total in a single pass after one pre-computation pass.

### Complexity Analysis

- **Time Complexity:** `O(N * C^2)`, where `N` is the length of the string and `C` is the number of possible characters (10 for digits). The suffix pre-computation takes `O(N*C^2)` and the main loop also takes `O(N*C^2)`. Since `C` is a small constant, the complexity is effectively linear, `O(N)`.
- **Space Complexity:** `O(N * C^2)` to store the suffix counts. This is also effectively `O(N)`. 

---

## Implementation

See `solution.py` for the full implementation of both approaches.
