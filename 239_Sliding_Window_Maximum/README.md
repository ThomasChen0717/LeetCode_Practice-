# 239. Sliding Window Maximum

**Difficulty:** <span style="color:#c0392b"><b>Hard</b></span>  
**Topics:** Array, Queue, Sliding Window, Heap (Priority Queue), Monotonic Queue

---

## Problem Description

You are given an array of integers `nums`, there is a sliding window of size `k` which is moving from the very left of the array to the very right. You can only see the `k` numbers in the window. Each time the sliding window moves right by one position.

Return _the max sliding window_.

---

## Examples

**Example 1:**
```
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7        5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
```

**Example 2:**
```
Input: nums = [1], k = 1
Output: [1]
```

## Constraints

- `1 <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`
- `1 <= k <= nums.length`

---

## Approach 1: Priority Queue (Max Heap)

### Intuition

A straightforward way to find the maximum in a dynamic window is to use a data structure that keeps elements ordered, like a max heap (priority queue). The largest element is always at the root, accessible in O(1) time.

The main challenge is handling the "sliding" part of the window. As the window moves, an old element leaves, and a new element enters. A standard heap doesn't support efficient removal of arbitrary elements. To solve this, we can use a **lazy removal** technique. Instead of removing an element from the heap as soon as it leaves the window, we leave it in and use a separate mechanism (like a hash map) to mark it as "deleted." When we query for the maximum, we check the top of the heap. If the top element is one that should have been deleted, we pop it and repeat until we find a valid, non-deleted element.

### Algorithm

1.  Initialize a max heap and a hash map `deleted` to track elements for lazy removal.
2.  Initialize a `res` list to store the results and a `start` pointer for the window's left boundary.
3.  Iterate through `nums` with an `end` pointer:
    a.  Add the new element `nums[end]` to the max heap.
    b.  When the window size reaches `k` (`end - start + 1 == k`):
        i.   **Clean the heap:** While the top element of the heap is in the `deleted` map with a count greater than 0, it means this element is stale. Pop it and decrement its count in the map.
        ii.  The current valid maximum for the window is now at the top of the heap. Add it to `res`.
        iii. **Slide the window:** Mark the outgoing element `nums[start]` for deletion by incrementing its count in the `deleted` map. Increment `start`.
4.  Return the `res` list.

### Complexity Analysis

-   **Time Complexity:** `O(N log N)`. In the worst case, we push and pop each of the `N` elements from the heap once. Heap operations take `O(log K)` time, where `K` is the size of the window (and thus roughly the size of the heap).
-   **Space Complexity:** `O(N)` for storing up to `n` elements in the priority queue and the hash map.

---

## Approach 2: Monotonic Queue (Deque)

### Intuition

This is the most optimal and classic approach for this problem. The key insight is that if we have two numbers in the window, `nums[i]` and `nums[j]` with `i < j`, and `nums[i] <= nums[j]`, then `nums[i]` can never be the maximum in any future window that still contains `j`. This is because `j` will always be in the window as long as `i` is, and `nums[j]` is larger.

This observation allows us to use a deque (double-ended queue) to store only the *indices* of promising candidates for the maximum. We maintain a **monotonically decreasing** queue: the values corresponding to the indices in the deque are always in descending order. The index at the front of the deque will thus always correspond to the maximum element in the current window.

### Algorithm

1.  Initialize an empty deque `q` to store indices and an empty list `ans` for the results.
2.  Iterate through `nums` with index `i`:
    a.  **Maintain Monotonicity:** Before adding the new index, remove all indices from the *back* of the deque whose corresponding values are less than or equal to `nums[i]`. This ensures the decreasing property.
    b.  **Add New Index:** Append the current index `i` to the back of the deque.
    c.  **Remove Out-of-Bounds Index:** If the index at the *front* of the deque is no longer in the current window (i.e., `q[0] <= i - k`), remove it from the front.
    d.  **Record Maximum:** Once the first full window is formed (`i >= k - 1`), the maximum element for that window is `nums[q[0]]`. Append this to the `ans` list.
3.  Return `ans`.

### Complexity Analysis

-   **Time Complexity:** `O(N)`. Each index is pushed onto and popped from the deque at most once, making the overall process linear.
-   **Space Complexity:** `O(K)`. The deque will store at most `k` indices.

---

## Approach 3: Block Separation + Prefix/Suffix Arrays

### Intuition

This is a clever dynamic programming approach that avoids using an explicit deque or heap. The idea is to split the array into blocks of size `k`. Any sliding window will either fall completely within one block or span across two adjacent blocks.

-   If a window `[i, j]` spans two blocks, it can be seen as the union of a *suffix* of the first block and a *prefix* of the second block.
-   The maximum of the window is then `max(maximum of the suffix, maximum of the prefix)`. 

We can precompute these prefix and suffix maximums for all blocks.

### Algorithm

1.  Initialize two arrays, `prefixMax` and `suffixMax`, of the same size as `nums`.
2.  **Compute `prefixMax`:** Iterate from left to right. For each block, `prefixMax[i]` will store the maximum value from the start of that block up to index `i`.
    -   If `i` is the start of a block (`i % k == 0`), `prefixMax[i] = nums[i]`.
    -   Otherwise, `prefixMax[i] = max(prefixMax[i - 1], nums[i])`.
3.  **Compute `suffixMax`:** Iterate from right to left. For each block, `suffixMax[i]` will store the maximum value from index `i` to the end of that block.
    -   If `i` is the end of a block (`(i + 1) % k == 0` or `i == n - 1`), `suffixMax[i] = nums[i]`.
    -   Otherwise, `suffixMax[i] = max(suffixMax[i + 1], nums[i])`.
4.  **Find Window Maximums:** Now, iterate through all possible window start positions `i` from `0` to `n - k`.
    -   The window is from `i` to `i + k - 1`.
    -   The end of the first block covered by the window is `i`, and the start of the second block covered is `i + k - 1`.
    -   The maximum for this window is `max(suffixMax[i], prefixMax[i + k - 1])`.
5.  Return the list of these maximums.

### Complexity Analysis

-   **Time Complexity:** `O(N)`. We make three linear passes through the array: one for `prefixMax`, one for `suffixMax`, and one to compute the final answer.
-   **Space Complexity:** `O(N)` to store the `prefixMax` and `suffixMax` arrays.

---

## Implementation

See `solution.py` for the full implementation of all three approaches.