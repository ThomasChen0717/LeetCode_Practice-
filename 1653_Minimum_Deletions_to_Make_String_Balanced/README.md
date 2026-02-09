# 1653. Minimum Deletions to Make String Balanced

**Difficulty:** <span style="color:#f39c12"><b>Medium</b></span>  
**Topics:**  Dynamic Programming, Stack, Greedy

---

## Problem Description

You are given a string `s` consisting only of characters `'a'` and `'b'​​​​`.

You can delete any number of characters in `s` to make `s` **balanced**. `s` is **balanced** if there is no pair of indices `(i,j)` such that `i < j` and `s[i] = 'b'` and `s[j]= 'a'`.

*Return the **minimum** number of deletions needed to make `s` **balanced***.

---

## Examples
Example 1:
```
Input: s = "aababbab"
Output: 2
Explanation: You can either:
Delete the characters at 0-indexed positions 2 and 6 ("aababbab" -> "aaabbb"), or
Delete the characters at 0-indexed positions 3 and 6 ("aababbab" -> "aabbbb").
```
Example 2:
```
Input: s = "bbaaaaabb"
Output: 2
Explanation: The only solution is to delete the first two characters.
```

## Constraints

- `1 <= s.length <= 10^5`
- `s[i]` is `'a'` or `'b'`​​.

---

## Approach 1: Three Pass

### Intuition

We can solve this problem using three passes. 
In the first pass, we count the number of `'b'` characters to the left of each index, including the current index.
In the second pass, we count the number of `'a'` characters to the right of each index, including the current index.
In the third pass, we iterate through the string and calculate the minimum number of deletions needed to make the string balanced. Note we have to do minus 1 because we do not need to count the current index.

### Complexity Analysis
Let `n` be the length of the string `s`.
- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(n)`

---

## Approach 2:Two Pass two variables

### Intuition

We can solve this problem using two passes and using only two variables instead of arrays. 
In the first pass, we count the number of `'a'` characters in the entire string.
In the second pass, when we encounter `'a'`, we decrement `count_a`.  

We calculate the minimum before modifying `count_b` since we don't want to include the current element. 

When we encounter `'b'`, we increment `count_b`.

### Complexity Analysis
- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(1)`

---

## Approach 3: Stack

### Intuition

We can solve this problem using a stack.
We iterate through the string and push characters onto the stack.
When we encounter `'a'`, we check if the stack is not empty and the top element is `'b'`.
If satisfies, we pop the `b` element from the stack, do not add the `a` element to the stack, and increment the number of deletions `num_del` by 1, indicating that we have found a balanced pair.

### Complexity Analysis
- **Time Complexity:** `O(n)` One-pass
- **Space Complexity:** `O(n)`

---

## Approach 4: DP 

## Implementation
We define `dp[i]` as the minimum number of deletions needed to make the substring `s[0:i-1]` balanced.
We initialize `dp[0] = 0` and `b_count = 0`.
We iterate through the string `s` and update `dp[i + 1]` based on the current character `s[i]`.
If `s[i]` is `'b'`, we set `dp[i + 1] = dp[i]` and increment `b_count` by 1.
If `s[i]` is `'a'`, we set `dp[i + 1] = min(dp[i] + 1, b_count)`.
 - `dp[i] + 1` represents the number of deletions needed to make `s[0:i]` balanced if we delete `s[i]`.
 - `b_count` represents the number of `'b'` characters to the left of `s[i]`, including `s[i]`.

## Complexity Analysis
- **Time Complexity:** `O(n)` One-pass
- **Space Complexity:** `O(n)`

--- 

## Approach 5: Space Optimized DP

### Intuition

We can optimize the space complexity of the previous approach by using only two variables instead of an array.
We define `min_deletions` as the minimum number of deletions needed to make the substring `s[0:i-1]` balanced.
We initialize `min_deletions = 0` and `b_count = 0`.
We iterate through the string `s` and update `min_deletions` based on the current character `s[i]`.
If `s[i]` is `'b'`, we increment `b_count` by 1.
If `s[i]` is `'a'`, we set `min_deletions = min(min_deletions + 1, b_count)`.
 - `min_deletions + 1` represents the number of deletions needed to make `s[0:i]` balanced if we delete `s[i]`.
 - `b_count` represents the number of `'b'` characters to the left of `s[i]`.

### Complexity Analysis
- **Time Complexity:** `O(n)` One-pass


# Solution

See `solution.py` for the full implementation.
