# 833. Find and Replace in String

**Difficulty:** <span style="color:#f39c12"><b>Medium</b></span>  
**Topics:** String, Sorting

---

## Problem Description

You are given a **0-indexed** string `s` that you must perform `k` replacement operations on. The replacement operations are given as three **0-indexed** parallel arrays, `indices`, `sources`, and `targets`, all of length `k`.

To complete the `ith` replacement operation:

1. Check if the **substring** sources[i] occurs at index `indices[i]` in the **original string** `s`.
1. If it does not occur, **do nothing**.
1. Otherwise if it does occur, **replace** that substring with `targets[i]`.

For example, if `s = "abcd"`, `indices[i] = 0`, `sources[i] = "ab"`, and `targets[i] = "eee"`, then the result of this replacement will be `"eeecd"`.

All replacement operations must occur **simultaneously**, meaning the replacement operations should not affect the indexing of each other. The testcases will be generated such that the replacements will **not overlap**.

- For example, a testcase with `s = "abc"`, `indices = [0, 1]`, and `sources = ["ab","bc"]` will not be generated because the `"ab"` and `"bc"` replacements overlap.

Return *the **resulting string** after performing all replacement operations on `s`*.

A **substring** is a contiguous sequence of characters in a string.

---

## Examples
Example 1:
![Example 1](https://assets.leetcode.com/uploads/2021/06/12/833-ex1.png)
```
Input: s = "abcd", indices = [0, 2], sources = ["a", "cd"], targets = ["eee", "ffff"]
Output: "eeebffff"
Explanation:
"a" occurs at index 0 in s, so we replace it with "eee".
"cd" occurs at index 2 in s, so we replace it with "ffff".
```
Example 2:
![Example 2](https://assets.leetcode.com/uploads/2021/06/12/833-ex2.png)
```
Input: s = "abcd", indices = [0, 2], sources = ["ab","ec"], targets = ["eee","ffff"]
Output: "eeecd"
Explanation:
"ab" occurs at index 0 in s, so we replace it with "eee".
"ec" does not occur at index 2 in s, so we do nothing.
```

## Constraints

- `1 <= s.length <= 1000`
- `k == indices.length == sources.length == targets.length`
- `1 <= k <= 100`
- `0 <= indices[i] < s.length`
- `1 <= sources[i].length, targets[i].length <= 50`
- `s` consists of only lowercase English letters.
- `sources[i]` and `targets[i]` consist of only lowercase English letters.

---

## Approach: Iterate by sorted indices

### Intuition

We iterate over the indices in sorted order. For each index, we check if the source substring matches the substring in `s` starting at that index. If it does, we replace it with the target substring. We keep a `prev` variable to include the characters in `s` that we do not process. It is crucial to not let `prev` decrease in case of a repeated indice. 

### Complexity Analysis
Let `n` be the length of `s`, `k` be the number of replacements, `S` = `sum(len(sources[i]) for i in range(k))` and `T` = `sum(len(targets[i]) for i in range(k))`.
- **Time Complexity:** `O(n log n)`
    - Sorting: `O(k log k)`
    - Total matching: `O(S)`
    - Building the result: `O(n - S + T)` 
    - Total: `O(k log k + n + T)`
        - If `S` and `T` are bounded and `k <= n`, we have `O(n log n)`
- **Space Complexity:** `O(n + T + k)`
    - The sorted indices array: `O(k)`
    - The result string: `O(n - S + T)`
        - Worst Case: `O(n + T)`



---

## Implementation

See `solution.py` for the full implementation.
