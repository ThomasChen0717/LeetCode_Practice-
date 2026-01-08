# 345. Reverse Vowels of a String

**Difficulty:** <span style="color:#2ecc71"><b>Easy</b></span>  
**Topics:** String, Two Pointers

---

## Problem Description

Given a string `s`, reverse only all the vowels in the string and return it.

The vowels are `'a'`, `'e'`, `'i'`, `'o'`, and `'u'`, and they can appear in both lower and upper cases, more than once.

---

## Examples
Example 1:
```
Input: s = "IceCreAm"

Output: "AceCreIm"

Explanation:

The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".
```
Example 2:
```
Input: s = "leetcode"

Output: "leotcede"
```

## Constraints

- `1 <= s.length <= 3 * 10^5`
- `s` consists of **printable ASCII** characters.

---

## Approach: Two Pointers

### Intuition
Keep two pointers, one at the beginning and one at the end of the string. 
Move the pointers towards each other until they meet.
At each step, if both pointers point to vowels, swap them.
If one of the pointers points to a non-vowel, move it towards the other pointer.

### Complexity Analysis
Let `n` be the length of the string.
- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(n)`

---

## Implementation

See `solution.py` for the full implementation.
