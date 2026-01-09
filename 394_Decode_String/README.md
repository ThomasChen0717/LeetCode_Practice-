# 394. Decode String

**Difficulty:** <span style="color:#f39c12"><b>Medium</b></span>  
**Topics:** Stack, Recursion

---

## Problem Description

Given an encoded string, return its decoded string.

The encoding rule is: `k[encoded_string]`, where the `encoded_string` inside the square brackets is being repeated exactly `k` times. Note that `k` is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers,`k`. For example, there will not be input like `3a` or `2[4]`.

The test cases are generated so that the length of the output will never exceed `10^5`.

---

## Examples
Example 1:
```
Input: s = "3[a]2[bc]"
Output: "aaabcbc"
```
Example 2:
```
Input: s = "3[a2[c]]"
Output: "accaccacc"
```
Example 3:
```
Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
```

## Constraints

- `1 <= s.length <= 30`
- `s` consists of lowercase English letters, digits, and square brackets `'[]'`.
- `s` is guaranteed to be a **valid** input.
- All the integers in `s` are in the range `[1, 300]`.

---

## Approach 1: Stack

### Intuition

Use a stack to keep track of the strings and numbers we encounter. 
When we encounter a closing bracket `']'`, we pop the stack until we encounter an opening bracket `'['`. 
We then repeat the string inside the brackets the number of times specified by the number before the opening bracket. 
We push the repeated string back onto the stack. 
We continue this process until the we finish iterating. 

### Complexity Analysis
Let 
- `n` be the length of the input string `s`.
- `maxK` be the maximum value of the number before the opening bracket `'['`.
- `countK` be the number of times the string inside the brackets is repeated.
- **Time Complexity:** `O(maxK^countK * n)`
- **Space Complexity:** `O(maxK^countK * n)`

---

## Approach 2: Two Stacks

### Intuition

We can use two stacks to keep track of the strings and numbers we encounter. 
When we encounter an opening bracket `'['`, we push the current string and number onto the respective stacks. 
We reset the current string and number to empty and 0 respectively. 
When we encounter a closing bracket `']'`, we pop the number stack, repeat the current string the number of times specified by the number, and append the repeated string to the string on top of the string stack. 
Then we set current string to the decoded string since we are on the outer level. 
We continue this process until the we finish iterating. 

### Complexity Analysis
Let 
- `n` be the length of the input string `s`.
- `maxK` be the maximum value of the number before the opening bracket `'['`.
- `countK` be the number of times the string inside the brackets is repeated.
- **Time Complexity:** `O(maxK^countK * n)`
- **Space Complexity:** `O(maxK^countK * n)`

---
## Approach 3: Recursion

### Intuition

We can use recursion to decode the string. 
We iterate through the string. 
When we encounter a digit, we read the number. 
When we encounter an opening bracket `'['`, we recursively decode the string inside the brackets. 
When we encounter a closing bracket `']'`, we repeat the decoded string the number of times specified by the number before the opening bracket. 
We continue this process until the we finish iterating. 

### Complexity Analysis
Let 
- `n` be the length of the input string `s`.
- `maxK` be the maximum value of the number before the opening bracket `'['`.
- `countK` be the number of times the string inside the brackets is repeated.
- **Time Complexity:** `O(maxK^countK * n)`
- **Space Complexity:** `O(maxK^countK * n)`

## Implementation

See `solution.py` for the full implementation.
