# 249. Group Shifted Strings

**Difficulty:** <span style="color:#f39c12"><b>Medium</b></span>  
**Topics:** Hash Map, String Manipulation

---

## Problem Description

Perform the following shift operations on a string:

- Right shift: Replace every letter with the successive letter of the English alphabet, where 'z' is replaced by 'a'. For example, `"abc"` can be right-shifted to `"bcd"` or `"xyz"` can be right-shifted to `"yza"`.
- Left shift: Replace every letter with the preceding letter of the English alphabet, where 'a' is replaced by 'z'. For example, `"bcd"` can be left-shifted to `"abc"` or `"yza"` can be left-shifted to `"xyz"`.

We can keep shifting the string in both directions to form an **endless shifting sequence**.

- For example, shift `"abc"` to form the sequence: `... <-> "abc" <-> "bcd" <-> ... <-> "xyz" <-> "yza" <-> .... <-> "zab" <-> "abc" <-> ...`

You are given an array of strings `strings`, group together all `strings[i]` that belong to the same shifting sequence. You may return the answer in **any order**.

---

## Examples
Example 1:
```
Input: strings = ["abc","bcd","acef","xyz","az","ba","a","z"]

Output: [["acef"],["a","z"],["abc","bcd","xyz"],["az","ba"]]
```
Example 2:
```
Input: strings = ["a"]

Output: [["a"]]
```
## Constraints

- `1 <= strings.length <= 200`
- `1 <= strings[i].length <= 50`
- `strings[i]` consists of lowercase English letters.

---

## Approach: Hash Map

### Intuition

We can compute for each string the hash key by finding the shift factor of the first character to `a` and then shifting each character and appending the result to the hash key. 

We use the hashmap to store lists of strings that have the same hash key. 

### Complexity Analysis
Let `n` be the length of `strings` and `k` be the average length of the strings.
- **Time Complexity:** `O(n * k)`
- **Space Complexity:** `O(n * k)`

---

## Implementation

See `solution.py` for the full implementation.
