# 3. Longest Substring Without Repeating Characters

**Difficulty:** <span style="color:#f39c12"><b>Medium</b></span>  
**Topics:** Sliding Window, String

---

## Problem Description

Given a string `s`, find the length of the **longest** substring without duplicate characters.

---

## Examples
Example 1:
```
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.
```
Example 2:
```
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
```
Example 3:
```
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
```

## Constraints

- `0 <= s.length <= 5 * 10^4`
- `s` consists of English letters, digits, symbols and spaces.

---

## Approach 1: Brute Force 

### Intuition

Simply check all substrings of `s` to see if they contain duplicate characters. 
If they do not, update the maximum length of the substring without duplicate characters.
Check all substrings by iterating over the string `s` and again from beginning to the current index.

### Complexity Analysis
Let `n` be the length of the string `s` and `m` be the size of the character set.
- **Time Complexity:** `O(n^3)`
- **Space Complexity:** `O(min(n, m))` 

---

## Approach 2: Sliding Window 

### Intuition

Use a sliding window to keep track of the current substring without duplicate characters.
Expand the window by moving the right pointer to the right if the character at the right pointer is not in the current window.
If the character is in the current window, move the left pointer to the right until the character is no longer in the current window.
Update the maximum length of the substring without duplicate characters.

### Complexity Analysis
- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(min(n, m))` 

## Approach 3: Sliding Window Optimized 

### Intuition

Same as Approach 2, but we keep in the hashmap the index of the character plus 1. 
If the character is in the current window, move the left pointer to the right of the index in the hashmap. 
This is because we want the left pointer to be at the next character after the last occurrence of the character in the current window.

### Complexity Analysis
- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(min(n, m))` 


## Implementation

See `solution.py` for the full implementation.
