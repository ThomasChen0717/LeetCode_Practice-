# 502. IPO

**Difficulty:** <span style="color:#e74c3c"><b>Hard</b></span>  
**Topics:** Greedy, Array, Sorting, Heap (Priority Queue)

---

## Problem Description

Suppose LeetCode will start its IPO soon. In order to sell a good price of its shares to Venture Capital, LeetCode would like to work on some projects to increase its capital before the IPO. Since it has limited resources, it can only finish at most `k` distinct projects before the IPO. Help LeetCode design the best way to maximize its total capital after finishing at most `k` distinct projects.

You are given `n` projects where the `i`th project has a pure profit `profits[i]` and a minimum capital of `capital[i]` is needed to start it.

Initially, you have `w` capital. When you finish a project, you will obtain its pure profit and the profit will be added to your total capital.

Pick a list of at most `k` distinct projects from given projects to maximize your final capital, and return the final maximized capital.

---

## Examples

**Example 1:**
```
Input: k = 2, w = 0, profits = [1,2,3], capital = [0,1,1]
Output: 4
Explanation: Since your initial capital is 0, you can only start the project indexed 0.
After finishing it you will obtain profit 1 and your capital becomes 1.
With capital 1, you can either start the project indexed 1 or the project indexed 2.
Since you can choose at most 2 projects, you need to finish the project indexed 2 to get the maximum capital.
Therefore, output the final maximized capital, which is 0 + 1 + 3 = 4.
```

**Example 2:**
```
Input: k = 3, w = 0, profits = [1,2,3], capital = [0,1,2]
Output: 6
```

## Constraints

- `1 <= k <= 10^5`
- `0 <= w <= 10^9`
- `n == profits.length`
- `n == capital.length`
- `1 <= n <= 10^5`
- `0 <= profits[i] <= 10^4`
- `0 <= capital[i] <= 10^9`

---

## Approach: Sort by Capital and Max Heap

### Intuition

This problem asks us to make a series of investment choices to maximize our final capital. At each step, we can choose from a set of available projects. This suggests a greedy approach. To make the best greedy choice, we should always select the project that gives the maximum profit from the pool of projects we can currently afford.

The main challenge is efficiently managing the projects. As our capital `w` increases, more projects become affordable. We need a way to:
1.  Quickly identify projects that we can afford.
2.  From that affordable pool, quickly select the one with the highest profit.

This leads to a two-part strategy:
1.  **Sorting:** First, we can sort all projects based on their required capital. This allows us to iterate through them in an order where we can easily find all projects that our current capital `w` allows us to start.
2.  **Max Heap:** Once we have a set of affordable projects, we need to pick the most profitable one. A max heap is the perfect data structure for this, as it allows `O(1)` access to the maximum element (profit) and `O(log N)` for insertions.

The algorithm works as follows:
1.  Combine the `capital` and `profits` arrays into a list of `(capital, profit)` pairs and sort it by capital.
2.  Initialize a max heap to store the profits of affordable projects.
3.  Iterate up to `k` times (for each project we can undertake):
    a.  Add all projects that have a capital requirement less than or equal to our current capital `w` to the max heap. Since the projects are sorted, we can do this with a pointer that advances through the sorted list.
    b.  If the max heap is empty, it means we cannot afford any more projects, so we break.
    c.  Otherwise, pop the maximum profit from the heap, add it to our capital `w`.
4.  Return the final capital `w`.

### Complexity Analysis

-   **Time Complexity:** `O(N log N )`. Sorting the projects takes `O(N log N)`. The main loop runs up to `K` times. In the worst case, each of the `N` projects is pushed onto and popped from the heap once across all `K` iterations. Each heap operation takes `O(log N)` time. This gives a total complexity dominated by the sorting and the heap operations. K is bounded by N so amortized `O(N log N )`.
-   **Space Complexity:** `O(N)`. We need `O(N)` space to store the projects list. The max heap can also store up to `N` projects in the worst-case scenario.

---

## Implementation

See `solution.py` for the full implementation.
