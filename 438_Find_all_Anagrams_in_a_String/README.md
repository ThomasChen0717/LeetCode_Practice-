# 438. Find All Anagrams in a String

**Difficulty:** <span style="color:#f1c40f"><b>Medium</b></span>  
**Topics:** Hash Table, String, Sliding Window

---

## Problem Description

Given two strings `s` and `p`, return an array of all the start indices of `p`'s anagrams in `s`. You may return the answer in any order.

An **Anagram** is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

---

## Examples

**Example 1:**
```
Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
```

**Example 2:**
```
Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
```

## Constraints

- `1 <= s.length, p.length <= 3 * 10^4`
- `s` and `p` consist of lowercase English letters.

---

## Approach: Sliding Window

### Intuition

This problem asks us to find all occurrences of anagrams of a pattern `p` within a larger string `s`. A brute-force approach would be to check every substring of `s` that has the same length as `p` and see if it's an anagram. Checking for an anagram can be done by sorting the strings or by using character frequency maps. However, this would be inefficient, leading to a time complexity of roughly `O(len(s) * len(p))`, which would be too slow given the constraints.

A more efficient method is the **sliding window** technique. We can maintain a window of size `len(p)` and slide it across `s`. The key is to efficiently check if the characters inside the window form an anagram of `p`. We can do this by comparing the character frequency map of the window with the frequency map of `p`.

Instead of rebuilding the frequency map for the window at every step, we can update it in O(1) time as we slide the window: when the window moves one position to the right, we add the new character to our map and remove the character that is no longer in the window.

### Algorithm

1.  **Initialize Frequency Maps:** Create two arrays of size 26 (for lowercase English letters), one for the pattern `p` (`target`) and one for the current window in `s` (`window`).

2.  **Populate Target Map:** Iterate through `p` and populate the `target` frequency map.

3.  **Sliding Window Initialization:** Initialize a left pointer `i = 0` and a right pointer `j = 0`.

4.  **Optimization with Match Count:** To avoid comparing the entire frequency arrays at each step (which would take O(26) time), we can maintain a `matches` count. This count tracks how many characters in the current window have the same frequency as in the `target` map.
    - We also need to know the total number of unique characters in `p`, let's call this `non_zero_count`.

5.  **Expand the Window:** Iterate through `s` with the right pointer `j`.
    - For each character `s[j]`, add it to the `window` by incrementing its count in the `window` map.
    - Update the `matches` count:
        - If the count of `s[j]` in `window` now equals its count in `target`, we have a new character match, so increment `matches`.
        - If the count of `s[j]` in `window` was previously equal to the target count but is now one greater, we've lost a match, so decrement `matches`.

6.  **Shrink the Window:** If the window size (`j - i + 1`) is greater than the length of `p`:
    - Remove the leftmost character `s[i]` from the window by decrementing its count.
    - Update the `matches` count similarly:
        - If the count of `s[i]` was equal to the target count and is now one less, we've lost a match, so decrement `matches`.
        - If the count of `s[i]` was one greater than the target count and is now equal, we have a new match, so increment `matches`.
    - Move the left pointer `i` one step to the right.

7.  **Check for Anagram:** After each move of the window (both expansion and shrinking), if `matches` is equal to `non_zero_count`, it means the current window is an anagram of `p`. Add the starting index `i` to the result list.

8.  **Return Result:** After the loop finishes, return the list of starting indices.

### Complexity Analysis

-   **Time Complexity:** `O(len(s))`. We iterate through the string `s` once with the sliding window. The operations inside the loop (updating frequency maps and the matches count) take constant time.
-   **Space Complexity:** `O(1)` or `O(26)`. We use two fixed-size arrays (of size 26) to store character frequencies, which is constant space.

---

## Implementation

See `solution.py` for the full implementation.