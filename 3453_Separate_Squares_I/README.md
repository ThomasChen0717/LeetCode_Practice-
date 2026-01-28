# 3453. Separate Squares I

**Difficulty:** <span style="color:#f39c12"><b>Medium</b></span>  
**Topics:** Binary Search, Scan Line

---

## Problem Description
You are given a 2D integer array `squares`. Each `squares[i] = [xi, yi, li]` represents the coordinates of the bottom-left point and the side length of a square parallel to the x-axis.

Find the **minimum** y-coordinate value of a horizontal line such that the total area of the squares above the line equals the total area of the squares below the line.

Answers within `10^-5` of the actual answer will be accepted.

**Note:** Squares **may** overlap. Overlapping areas should be counted **multiple times**.

---

## Examples
Example 1:
```
Input: squares = [[0,0,1],[2,2,1]]

Output: 1.00000

Explanation:
```
![Example 1](https://assets.leetcode.com/uploads/2025/01/06/4062example1drawio.png)
```
Any horizontal line between y = 1 and y = 2 will have 1 square unit above it and 1 square unit below it. The lowest option is 1.
```

Example 2:
```
Input: squares = [[0,0,2],[1,1,1]]

Output: 1.16667

Explanation:
```
![Example 2](https://assets.leetcode.com/uploads/2025/01/06/4062example2drawio.png)
```
The areas are:

Below the line: 7/6 * 2 (Red) + 1/6 (Blue) = 15/6 = 2.5.
Above the line: 5/6 * 2 (Red) + 5/6 (Blue) = 15/6 = 2.5.
Since the areas above and below the line are equal, the output is 7/6 = 1.16667.
```

## Constraints

- `1 <= squares.length <= 5 * 10^4`
-  `squares[i] = [x_i, y_i, l_i]`
- `squares[i].length == 3`
- `0 <= x_i, y_i <= 10^9`
- `1 <= l_i <= 10^9`
- The total area of all the squares will not exceed `10^12`.

---

## Approach 1: Binary Search

### Intuition

The total area of all squares is fixed.  
As we raise the horizontal line from bottom to top, the area below the line increases monotonically (and the area above decreases correspondingly).  
Therefore we can binary-search the smallest y such that the area below the line is at least half of the total area.  
For a candidate y we sweep the plane: every square contributes  
- its full area if the whole square is below y,  
- zero if the whole square is above y,  
- otherwise the rectangular strip of height (y - y_i) and width l_i.  


### Complexity Analysis
Let `n` be the number of squares, `U = max(y_i + l_i)`, and `L = 10^5`. 

- **Time Complexity:** `O(n log(LU))`
    - Compute total area: `O(n)`.
    - Number of iterations: `U / 2^k' <= 10^-5`, so `k' <= log(U * L)`.
        - Each Iteration: `O(n)` 
- **Space Complexity:** `O(1)`

---

## Approach 2: Scan Line

### Intuition

We can also solve this problem using a scan line algorithm.  
We start by computing the total area of all squares. 
We also keep a events list storing the events of the scan line. 
Each event is a tuple `(y, side length, delta)` where:
- `y` is the y-coordinate of the event.
- `side length` is the side length of the square.
- `delta` is 1 if the event is the bottom side of a square, and -1 if the event is the top side of a square.

We sort the events by their y-coordinate and then begin our scanning: 
- We keep track of the `covered_width` which means how many units of width are covered by the squares below the current line. 
    - This is incremented when we encounter the bottom side of a square.
    - This is decremented when we encounter the top side of a square. 
- We also keep track of the `curr_area` which is the cumulative area of the squares under the current line. 
-  We also keep track of the `prev_height`, which is the height of the previous line. 

When we would find that adding the new area to `curr_area` would  exceed half of the total area, we would return: 
```
prev_height + (total_area - 2 * curr_area) / (2 * covered_width)
```
which is derived from: 
``` 
total_area / 2 = curr_area + covered_width * (h - prev_height) 
=> h = prev_height + (total_area - 2 * curr_area) / (2 * covered_width)
``` 

## Complexity Analysis

- **Time Complexity:** `O(n log(U))`
    - Time of sorting: `O(n log(n))`.
    - Time of scanning: `O(n)`.
- **Space Complexity:** `O(n)`
    - Space of sorting: `O(n)` or `O(log(n))` depending on the implementation of the sorting algorithm.
    - Storing the sorted events: `O(n)`.

## Implementation

See `solution.py` for the full implementation.
