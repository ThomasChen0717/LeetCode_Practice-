# 3614. Process String With Special Operations II

**Difficulty:** <span style="color:#e74c3c"><b>Hard</b></span>  
**Topics: String, Simulation, Stack, Two Pointers**

---

## Problem Description

You are given a string `s` consisting of lowercase English letters and the special characters: `'*'`, `'#'`, and `'%'`. You are also given an integer `k`. Build a new string `result` by processing `s` according to the following rules from left to right:
*   If the letter is a **lowercase** English letter append it to `result`.
*   A `'*'` **removes** the last character from `result`, if it exists.
*   A `'#'` **duplicates** the current `result` and **appends** it to itself.
*   A `'%'` **reverses** the current `result`.
Return the `kth` character of the final string `result`. If `k` is out of the bounds of `result`, return `'.'`.


---

## Examples
Example 1:
Input: s = "a#b%*", k = 1
Output: "a"
Explanation:
| i | s\[i\] | Operation                 | Current result |
| - | ------ | ------------------------- | -------------- |
| 0 | 'a'    | Append 'a'                | "a"            |
| 1 | '#'    | Duplicate result          | "aa"           |
| 2 | 'b'    | Append 'b'                | "aab"          |
| 3 | '%'    | Reverse result            | "baa"          |
| 4 | '*'   | Remove the last character | "ba"           |
The final `result` is `"ba"`. The character at index `k = 1` is `'a'`.

Example 2:
Input: s = "cd%#*#", k = 3
Output: "d"
Explanation:
| i | s\[i\] | Operation                 | Current result |
| - | ------ | ------------------------- | -------------- |
| 0 | 'c'    | Append 'c'                | "c"            |
| 1 | 'd'    | Append 'd'                | "cd"           |
| 2 | '%'    | Reverse result            | "dc"           |
| 3 | '#'    | Duplicate result          | "dcdc"         |
| 4 | '*'   | Remove the last character | "dcd"          |
| 5 | '#'    | Duplicate result          | "dcddcd"       |
The final `result` is `"dcddcd"`. The character at index `k = 3` is `'d'`.

Example 3:
Input: s = "z*#", k = 0
Output: "."
Explanation:
| i | s\[i\] | Operation                 | Current result |
| - | ------ | ------------------------- | -------------- |
| 0 | 'z'    | Append 'z'                | "z"            |
| 1 | '*'   | Remove the last character | ""             |
| 2 | '#'    | Duplicate the string      | ""             |
The final `result` is `""`. Since index `k = 0` is out of bounds, the output is `'.'`.

## Constraints

- `1 <= s.length <= 10^5`
- `s` consists of only lowercase English letters and special characters `'*'`, `'#'`, and `'%'`.
- `0 <= k <= 10^15`
- The length of `result` after processing `s` will not exceed `10^15`.

---

## Approach

### Intuition

The problem involves processing a string with special operations. A naive simulation by actually building the string `result` would be too slow and memory-intensive because the length of `result` can be up to `10^15`. This suggests that we cannot explicitly construct the string. Instead, we need a way to track the length and properties of the `result` string without building it. The key insight is to work backward from the final `k`th character. We can simulate the operations in reverse to determine what character would be at the `k`th position. For example, if we encounter a `'#'` (duplicate), we can determine if `k` falls into the first half or second half and adjust `k` accordingly. If we encounter a `'%'` (reverse), we can simply adjust `k` to its new mirrored position. For `'*'` (remove last character), we need to maintain the current length. For appending characters, we can determine the character directly when `k` matches.

### Complexity Analysis

- **Time Complexity:** `O(N)` where `N` is the length of the input string `s`. This is because we iterate through the input string `s` once to calculate sizes and then iterate once in reverse to find the `k`th character.
- **Space Complexity:** `O(N)` for storing the sizes array.

---

## Implementation

See `solution.c++` for the full implementation.
