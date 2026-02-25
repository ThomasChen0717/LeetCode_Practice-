# 1461. Check If a String Contains All Binary Codes of Size K

**Difficulty:** <span style="color:#f39c12"><b>Medium</b></span>  
**Topics:** String, Bit Manipulation, Sliding Window, Hash Set

---

## Problem Description

Given a binary string `s` and an integer `k`, return `true` if every binary code of length `k` is a substring of `s`. Otherwise, return `false`.

---

## Examples
**Example 1:** 
```
Input: s = "00110110", k = 2
Output: true
Explanation: The binary codes of length 2 are "00", "01", "10" and "11". They can be all found as substrings at indices 0, 1, 3 and 2 respectively.
```

**Example 2:**
```
Input: s = "0110", k = 1
Output: true
Explanation: The binary codes of length 1 are "0" and "1", it is clear that both exist as a substring.
```

**Example 3:**
```
Input: s = "0110", k = 2
Output: false
Explanation: The binary code "00" is of length 2 and does not exist in the array.
```

## Constraints

- `1 <= s.length <= 5 * 10^5`
- `s[i]` is either `'0'` or `'1'`.
- `1 <= k <= 20`

---

## Approach 1: HashSet

### Intuition

To solve this problem, we need to verify if all `2^k` possible binary codes of length `k` are present in the string `s`. A straightforward way to do this is to find all unique substrings of length `k` and count them.

The algorithm is as follows:
1.  Create a hash set to store all unique substrings of length `k` that we find in `s`.
2.  Iterate through the string `s` with a sliding window of size `k`.
3.  For each window, extract the substring and add it to our hash set.
4.  After iterating through the entire string, check if the size of the hash set is equal to `2^k`. If it is, we have found all possible binary codes.

This approach is simple to understand but can be inefficient due to the repeated creation of substrings.

### Complexity Analysis

-   **Time Complexity:** `O((N-k) * k)`. We iterate `N-k` times, and in each iteration, slicing the string to create a substring of length `k` takes `O(k)` time.
-   **Space Complexity:** `O(2^k * k)`. In the worst case, the hash set will store `2^k` unique strings, each of length `k`.

---

## Approach 2: Rolling Hash

### Intuition

This approach optimizes the previous one by avoiding the costly substring slicing in each step. Instead of storing the substrings themselves, we can store their integer values. A rolling hash allows us to calculate the hash (the integer value) of the next window in `O(1)` time from the previous one.

The algorithm is as follows:
1.  The total number of unique binary codes of length `k` is `2^k`. We can use a boolean array `got` of size `2^k` to mark which codes we have seen.
2.  Calculate the integer value of the first `k`-length substring.
3.  Iterate through the rest of the string, and for each new character, update the hash value in `O(1)`:
    *   Shift the current hash value one bit to the left to "remove" the most significant bit.
    *   Apply a bitmask to ensure the hash value stays within the `k`-bit range.
    *   Add the new character's integer value as the new least significant bit.
4.  For each calculated hash value, mark `got[hash_val]` as `true`.
5.  If we have found `2^k` unique codes, we can return `true` early.

This method is significantly faster as it processes each character of the string only once.

### Complexity Analysis

-   **Time Complexity:** `O(N)`, where `N` is the length of the string `s`. We iterate through the string once, and all operations inside the loop are `O(1)`.
-   **Space Complexity:** `O(2^k)` to maintain the boolean array `got`.

---

## Implementation

See `solution.py` for the full implementation.
