# 49. Group Anagrams

**Difficulty:** <span style="color:#f39c12;"><b>Medium</b></span>  
**Topics:** Array, Hash Table, String, Sorting

---

## Problem Description

Given an array of strings `strs`, group the anagrams together. You can return the answer in **any order**.

---

## Examples
Example 1:
```
Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:

There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
```
Example 2:
```
Input: strs = [""]

Output: [[""]]
```
Example 3:
```
Input: strs = ["a"]

Output: [["a"]]
```

## Constraints

- `1 <= strs.length <= 10^4`
- `0 <= strs[i].length <= 100`
- `strs[i]` consists of lowercase English letters.

---

## Approach 1: Categorize by Sorted String

### Intuition

Each anagram will appear the same when sorted. Therefore, we can sort each string and use the sorted string as the key in a hash map. 

### Complexity Analysis
Let 
- `n` be the length of `strs`
- `k` be the maximum length of a string in `strs`
- **Time Complexity:** `O(n * k * log(k))` 
    - We iterate through each string in `strs` and sort each string. Sorting each string takes `O(k * log(k))` time.
- **Space Complexity:** `O(n * k)` 
    - We store each string in `strs` in the hash map.

---

## Approach 2: Categorize by Count

### Intuition

Each anagram will have the same character count. Therefore, we can use the character count as the key in a hash map.

We use a 26 element array to count the occurrences of each character in a string. The array index represents the character (a-z) and the value represents the count.

### Complexity Analysis
Let 
- `n` be the length of `strs`
- `k` be the maximum length of a string in `strs`
- **Time Complexity:** `O(n * k)` 
    - We iterate through each string in `strs` and count the characters in each string. Counting the characters in each string takes `O(k)` time.
- **Space Complexity:** `O(n * k)` 
    - We store each string in `strs` in the hash map.
    - The count array has a fixed size of 26, so it does not contribute to the space complexity. 

---

## Implementation

See `solution.py` for the full implementation.
