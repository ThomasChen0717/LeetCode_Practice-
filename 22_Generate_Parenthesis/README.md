# 22. Generate Parenthesis

**Difficulty:** <span style="color:#f39c12"><b>Medium</b></span>  
**Topics:**  Backtracking, Divide and Conquer

---

## Problem Description

Given `n` pairs of parentheses, write a function to *generate all combinations of well-formed parentheses*.

---

## Examples
Example 1:
```
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
```
Example 2:
```
Input: n = 1
Output: ["()"]
```
## Constraints

- `1 <= n <= 8`

---

## Approach: Backtracking

### Intuition

We use backtracking to generate all possible combinations of well-formed parentheses. 
At each step, we have two choices: add an opening parenthesis or add a closing parenthesis. 
We only add an opening parenthesis if the number of opening parentheses is less than `n`. 
We only add a closing parenthesis if the number of closing parentheses is less than the number of opening parentheses.

### Complexity Analysis

- **Time Complexity:** `O(4^n / (n * sqrt(n)))` 
    - This is the number of valid combinations of parentheses. (Catalan number)
- **Space Complexity:** `O(n)`
    - The depth of the recursion tree is `2n`.

---

## Approach: Divide and Conquer

### Intuition

We use divide and conquer to generate all possible combinations of well-formed parentheses. 
At each step, we divide the problem into subproblems: generate all combinations of `n-1` pairs of parentheses and add a pair of parentheses to each combination.

### Complexity Analysis

- **Time Complexity:** `O(4^n / (sqrt(n)))` 
    - This is the number of valid combinations of parentheses. (Catalan number)
- **Space Complexity:** `O(n)`
    - The depth of the recursion tree is `n`.

---

## Implementation

See `solution.py` for the full implementation.
