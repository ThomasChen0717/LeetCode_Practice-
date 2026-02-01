# 20_Valid_Parenthese

**Difficulty:** <span style="color:#2ecc71"><b>Easy</b></span>  
**Topics:** Stack, String

---

## Problem Description

Given a string s containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

---

## Examples
Example 1:
```
Input: s = "()"

Output: true
```
Example 2:
```
Input: s = "()[]{}"

Output: true
```
Example 3:
```
Input: s = "(]"

Output: false
```
Example 4:
```
Input: s = "([])"

Output: true
```
Example 5:
```
Input: s = "([)]"

Output: false
```

## Constraints

- `1 <= s.length <= 10^4`
- `s` consists of parentheses only `'()[]{}'`.

---

## Approach: Stack

### Intuition

- We use a stack to keep track of opening brackets.
- When we encounter a closing bracket, we check if it matches the top of the stack.
- If it does, we pop the stack; otherwise, the string is invalid.
- Finally, the stack should be empty if the string is valid.

### Complexity Analysis

- **Time Complexity:** `O(n)`, where `n` is the length of the string.
- **Space Complexity:** `O(n)` in the worst case, where all characters are opening brackets.

---

## Implementation

See `solution.py` for the full implementation.
