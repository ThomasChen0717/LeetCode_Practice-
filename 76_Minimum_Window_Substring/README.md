# 76. Minimum Window Substring

**Difficulty:** <span style="color:#c0392b"><b>Hard</b></span>  
**Topics:** Hash Table, String, Sliding Window

---

## Problem Description

Given two strings `s` and `t` of lengths `m` and `n` respectively, return the minimum window substring of `s` such that every character in `t` (including duplicates) is included in the window. If there is no such substring, return the empty string `""`.

The testcases will be generated such that the answer is unique.

---

## Examples

**Example 1:**
```
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
```

**Example 2:**
```
Input: s = "a", t = "a"
Output: "a"
```

**Example 3:**
```
Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since s has only one 'a', we cannot find a valid window.
```

## Constraints

- `m == s.length`
- `n == t.length`
- `1 <= m, n <= 10^5`
- `s` and `t` consist of uppercase and lowercase English letters.

---

## Approach: Sliding Window + Hash Map

### Intuition

This problem asks for the *smallest* substring of `s` that contains all characters of `t`. This is a classic optimization problem that can be efficiently solved using the **sliding window** technique.

The core idea is to maintain a "window" (a substring of `s`) and expand it by moving a right pointer. Once the window contains all the characters required by `t`, it becomes a "valid" window. We then try to find the smallest possible valid window by shrinking it from the left (moving a left pointer). We keep track of the smallest valid window found during this process.

To efficiently check if a window is valid, we use a hash map (or a frequency array) to store the character counts needed by `t`. As we slide our window, we update the counts of characters within it.

### Algorithm

1.  **Character Frequency Map:** Create a hash map, `char_map`, to store the frequency of each character in the target string `t`.

2.  **Initialization:**
    -   `start`, `end`: Two pointers to define the sliding window, both initialized to 0.
    -   `count`: A counter initialized to the number of unique characters in `t`. This will help us track when a window becomes valid.
    -   `length`: A variable to store the minimum window length found so far, initialized to infinity.
    -   `idx`: A variable to store the starting index of the minimum window.

3.  **Expand the Window:** Move the `end` pointer from left to right across `s`.
    -   For each character `s[end]`, if it's a character we need (i.e., it exists in `char_map`), decrement its count in the map.
    -   If the count for a character in `char_map` drops to `0`, it means we have found all required instances of that specific character. Decrement the `count` of unique characters needed.

4.  **Shrink the Window:** Once `count` becomes `0`, our window is valid (it contains all characters from `t`). Now, we try to make it smaller.
    -   Enter a `while` loop that continues as long as `count == 0`.
    -   Check if the current window size (`end - start + 1`) is smaller than `length`. If so, update `length` and `idx`.
    -   Consider the character at the `start` of the window, `s[start]`.
    -   If `s[start]` is a character we care about (in `char_map`), increment its count in the map. If its count becomes greater than `0`, it means our window is no longer valid because we just lost a required character. To signify this, increment `count`.
    -   Move the `start` pointer one step to the right to shrink the window.

5.  **Continue:** After the inner `while` loop (shrinking phase) finishes, continue the outer loop by incrementing `end` to find the next valid window.

6.  **Return Result:** After iterating through `s`, if `length` is still infinity, it means no valid window was ever found, so return an empty string. Otherwise, return the substring of `s` starting at `idx` with length `length`.

### Complexity Analysis

-   **Time Complexity:** `O(len(s) + len(t))`. We iterate through `t` once to build the frequency map. Then, the `start` and `end` pointers each traverse `s` at most once.
-   **Space Complexity:** `O(len(t))` or `O(K)` where `K` is the number of unique characters in `t`. This space is used for the character frequency map.

---

## Implementation

See `solution.py` for the full implementation.