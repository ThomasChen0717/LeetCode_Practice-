# 424. Longest Repeating Character Replacement

**Difficulty:** <span style="color:#f39c12"><b>Medium</b></span>  
**Topics:** Array, Sliding Window, Binary Search

---

## Problem Description

You are given a string `s` and an integer `k`. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most `k` times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

---

## Examples
Example 1:
```
Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
```
Example 2:
```
Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.
```

## Constraints

- `1 <= s.length <= 10^5`
- `s` consists of only uppercase English letters.
- `0 <= k <= s.length`

---

## Approach 1: Sliding Window + Binary Search

### Intuition

We use a binary search method on the possible substring length. 
For each length `mid`, we check if there exists a substring of length `mid` that can be made into a substring of the same letter by performing at most `k` operations. This check is done using a sliding window approach. 

### Complexity Analysis
Let 
- `n` be the length of the input string `s`. 
- `m` be the number of unique characters in the string `s`.
- **Time Complexity:** `O(n log n)`
- **Space Complexity:** `O(m)`

---

## Approach 2: Sliding Window Slow

### Intuition

We use a sliding window approach to find the longest substring of the same letter. 
We first find the unique characters in the string `s`.  
For each unique character, we use a sliding window approach to find the longest substring of the same letter. 

### Complexity Analysis
Let 
- `n` be the length of the input string `s`. 
- `m` be the number of unique characters in the string `s`.
- **Time Complexity:** `O(nm)`
- **Space Complexity:** `O(m)`

---

## Approach 3: Sliding Window Fast

### Intuition

We notice that once we've found a current max window length, we never need to shrink the window. 
We only need to move the window to the right and try to find a longer window. 
We keep track of the maximum frequency of any character in the current window. 
If the window size minus the maximum frequency is greater than `k`, we shrink the window from the left, meaning our attemt to expand the window failed so we fall back to the current max window length.  
Return the current max window length.

### Complexity Analysis
Let 
- `n` be the length of the input string `s`. 
- `m` be the number of unique characters in the string `s`.
- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(m)`

---

## Implementation

See `solution.py` for the full implementation.
