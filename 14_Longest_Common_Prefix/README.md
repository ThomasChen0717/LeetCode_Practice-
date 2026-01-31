# 14. Longest Common Prefix

**Difficulty:** <span style="color:#2ecc71"><b>Easy</b></span>  
**Topics:** String, Array

---

## Problem Description

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string `""`.

---

## Examples
Example 1:
```
Input: strs = ["flower","flow","flight"]
Output: "fl"
```
Example 2:
```
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
```

## Constraints

- `1 <= strs.length <= 200`
- `0 <= strs[i].length <= 200`
- `strs[i]` consists of only lowercase English letters.

---

## Approach 1: Horizontal Scanning

### Intuition

We compute the common prefix of the first two strings in the array, and then find the common prefix of the result and the third string, and so on. 

We can early stop the process if the common prefix of the current two strings is empty, meaning that there is no common prefix among the first `i` strings, and thus no common prefix across all strings.

### Complexity Analysis
Let `n` be the number of strings in the array, and `m` be the length of the longest string in the array.
- **Time Complexity:** `O(n * m)`
- **Space Complexity:** `O(1)`

---

## Approach 2: Vertical Scanning


### Intuition

We compare the characters of the first string with the characters of the other strings in the array vertically. If we find a mismatch, we can early stop the process.

### Complexity Analysis
- **Time Complexity:** `O(n * m)`
- **Space Complexity:** `O(1)`

---


## Implementation

See `solution.py` for the full implementation.
