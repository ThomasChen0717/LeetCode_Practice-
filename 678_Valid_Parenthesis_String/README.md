# 678. Valid Parenthesis String

**Difficulty:** <span style="color:#f39c12"><b>Medium</b></span>  
**Topics:** Stack, Dynamic Programming, Two Pointers

---

## Problem Description

Given a string `s` containing only three types of characters: `'('`, `')'` and `'*'`, return `true` if `s` is valid.

The following rules define a **valid** string:
- Any left parenthesis `'('` must have a corresponding right parenthesis `')'`.
- Any right parenthesis `')'` must have a corresponding left parenthesis `'('`.
- Left parenthesis `'('` must go before the corresponding right parenthesis `')'`.
- `'*'` could be treated as a single right parenthesis `')'` or a single left parenthesis `'('` or an empty string `""`.

---

## Examples
Example 1:
```
Input: s = "()"
Output: true
```
Example 2:
```
Input: s = "(*)"
Output: true
```
Example 3:
```
Input: s = "(*))"
Output: true
```

## Constraints

- `1 <= s.length <= 100`
- `s[i]` is `'('`, `')'` or `'*'`.

---

## Approach: Top Down Dynamic Programming

### Intuition

At every position in the string, you only need to know two things to decide whether the rest can be valid:

1. `index` — where you are in the string
2. `open_count` — how many unmatched `'('` you currently have

Everything else about the past doesn’t matter.

So the question becomes:

From position `index` with `open_count` open parentheses, can the rest of the string be completed to a valid parentheses string?

That question is exactly what `is_valid_string(index, open_count, ...)` answers.

### Complexity Analysis

- **Time Complexity:** `O(n * n)`
- **Space Complexity:** `O(n * n)`

---

## Approach 2: Bottom Up Dynamic Programming

### Intuition

`dp[i][j]` means: 
After processing the first `i` characters of `s`, is it possible to have exactly `j` unmatched `'('` parentheses?

- `i = how many characters you’ve consumed

- `j` = how many `'('` are still open

This state captures everything that matters.

### Complexity Analysis

- **Time Complexity:** `O(n * n)`
- **Space Complexity:** `O(n * n)`

---

## Approach 3: Two Stakcs

### Intuition

- `openBracks` = a stack of indices of `'('`
- `asterisks` = a stack of indices of `'*'`

### Algorithm

1. Initialize `openBracks` and `asterisks` as empty stacks.
2. Iterate through each character `c` in the string `s`:
   - If `c` is `'('`, push its index to `openBracks`.
   - If `c` is `'*'`, push its index to `asterisks`.
   - If `c` is `')'`:
     - If `openBracks` is not empty, pop from `openBracks`.
     - Otherwise, if `asterisks` is not empty, pop from `asterisks`.
     - Otherwise, return `false`.
3. After processing all characters, check if both `openBracks` and `asterisks` are empty. 
   - Compare the indices in `openBracks` with the indices in `asterisks`.
     - If any index in `openBracks` is greater than any index in `asterisks`, return `false`.
     - Otherwise, pop from `openBracks` and `asterisks` until they are empty.
4. Check if `openBracks` is empty.
   - If it is, return `true`.
   - Otherwise, return `false`.

### Complexity Analysis

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(n)`

---

## Approach 4: Two Pointers

### Intuition
Keep a left and right pointer and count the number of unmatched parentheses.

Count `*` as `'('` and `')'` when traversing from left and right, respectively.

If at any point the number of unmatched parentheses is negative, return `false`. 
### Correctness 
The two-pointer method is correct because it detects exactly the two ways validity can fail: a prefix with too many `')'` and a suffix with too many `'('`; if neither occurs, there exists an assignment of `*` that balances the string.
### Complexity Analysis

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(1)`


See `solution.py` for the full implementation.