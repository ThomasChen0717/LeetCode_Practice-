# 242. Valid Anagram

**Difficulty:** <span style="color:#2ecc71"><b>Easy</b></span>  
**Topics:** Array, Hash Table, Sorting

---

## Problem Description

Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise.

---

## Examples
Example 1:
```
Input: s = "anagram", t = "nagaram"

Output: true
```
Example 2:
```
Input: s = "rat", t = "car"

Output: false
```
## Constraints

- `1 <= s.length, t.length <= 5 * 10^4`
- `s` and `t` consist of lowercase English letters.

---

## Approach 1: Sorting

### Intuition

Sorting both strings and comparing them will tell us if they are anagrams of each other.

### Complexity Analysis

- **Time Complexity:** `O(n log n)` where `n` is the length of the strings.
- **Space Complexity:** `O(n)` for the sorted strings.

---

## Approach 2: Frequency Counter

### Intuition

Count the frequency of each character in both strings. If the frequency of each character is the same in both strings, then they are anagrams of each other.

### Complexity Analysis

- **Time Complexity:** `O(n)` where `n` is the length of the strings.
- **Space Complexity:** `O(1)` since the size of the frequency array is constant (26 lowercase English letters).

---

## Implementation

See `solution.py` for the full implementation.
