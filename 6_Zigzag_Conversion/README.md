# 6_Zigzag Conversion

**Difficulty:** <span style="color:#f39c12"><b>Medium</b></span>  
**Topics:** String 

---

## Problem Description

The string `"PAYPALISHIRING"` is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
```
P   A   H   N
A P L S I I G
Y   I   R
```
And then read line by line: `"PAHNAPLSIIGYIR"`

Write the code that will take a string and make this conversion given a number of rows:

`string convert(string s, int numRows)`

---

## Examples
Example 1:
```
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
```
Example 2:
```
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
```
Example 3:
```
Input: s = "A", numRows = 1
Output: "A"
```

## Constraints

- `1 <= s.length <= 1000`
- `s` consists of English letters (lower-case and upper-case), `','` and `'.'`.
- `1 <= numRows <= 1000`

---

## Approach 1: Following the Zigzag Pattern

### Intuition

We separate the pattern into sections and calculate the number of characters in each section, as well as the total number of columns in each section. We then iterate through the string, populating a matrix by the zigzag pattern. Finally, we concatenate the rows of the matrix to get the final result. 

### Complexity Analysis
Let `n` be the length of the string `s`, and `numRows` be the number of rows.
- **Time Complexity:** `O(n * numRows)`
- **Space Complexity:** `O(n * numRows)`

---

## Approach 2: String Traversal

### Intuition

We find that for each row in the zigzag pattern, we can find a pattern to jump to the next index. For example, for the first row, we jump to the next index by `2 * numRows - 2` characters, which is exactly the length of each section. For the second row, we jump to the next index by `length of section - 2 * currRow` characters, and so on.

### Complexity Analysis
- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(1)`

---

## Implementation

See `solution.py` for the full implementation.
