# 41. First Missing Positive

**Difficulty:** <span style="color:#c0392b"><b>Hard</b></span>  
**Topics:** Array, Hash Table

---

## Problem Description

Given an unsorted integer array `nums`, return the smallest missing positive integer.

You must implement an algorithm that runs in `O(n)` time and uses `O(1)` constant extra space.

---

## Examples

**Example 1:**
```
Input: nums = [1,2,0]
Output: 3
Explanation: The numbers in the range [1,2] are all in the array.
```

**Example 2:**
```
Input: nums = [3,4,-1,1]
Output: 2
Explanation: 1 is in the array but 2 is missing.
```

**Example 3:**
```
Input: nums = [7,8,9,11,12]
Output: 1
Explanation: The smallest positive integer 1 is missing.
```

## Constraints

- `1 <= nums.length <= 5 * 10^5`
- `-2^31 <= nums[i] <= 2^31 - 1`

---

## Approach 1: Simulating a HashSet

### Intuition

The problem requires an `O(n)` time and `O(1)` space solution, which means we can't use a standard HashSet. The key insight is to use the array itself as a hash set. The first missing positive must be within the range `[1, n+1]`, where `n` is the length of the array. This is because if the array contained all numbers from `1` to `n`, the first missing positive would be `n+1`.

We can use the array's indices to store information about the presence of numbers in this range. For a number `x` in the range `[1, n]`, we can mark the index `x-1` to indicate that `x` has been seen. A common way to mark an index without losing the original information is to change the sign of the number at that index.

### Algorithm

1.  **Clean the Data:** First, we don't care about non-positive numbers or numbers greater than `n`, as they don't help us find the first missing positive in the `[1, n]` range. We can iterate through the array and replace all such numbers with a value outside our range of interest, like `n + 1`.

2.  **Mark Seen Numbers:** Iterate through the array again. For each number `num`:
    a.  Take its absolute value, as it might have been negated in a previous step.
    b.  If `1 <= num <= n`, it means this number is in our range of interest. We mark its presence by negating the value at index `num - 1`. We use `abs()` when accessing `nums[num - 1]` to ensure we don't corrupt the index if it was already negated.

3.  **Find the First Missing Positive:** Iterate through the array one last time.
    -   The first index `i` where the value `nums[i]` is still positive indicates that the number `i + 1` was never seen in the original array. This is our answer.

4.  **Handle the Edge Case:** If all numbers from `1` to `n` are present, all values in the array will be negative. In this case, the first missing positive is `n + 1`.

### Complexity Analysis

-   **Time Complexity:** `O(n)`. We perform three separate linear passes through the array.
-   **Space Complexity:** `O(1)`. We modify the input array in-place and do not use any extra data structures.

---

## Approach 2: Swapping (Cyclic Sort)

### Intuition

This approach also uses the array itself to store information, but instead of using signs, it tries to place each number in its "correct" position. The idea is that if the array were sorted and contained only positive integers, the number `x` should be at index `x - 1`.

We can iterate through the array and for each number `nums[i]`, we try to move it to its correct index `nums[i] - 1`. We do this by swapping `nums[i]` with `nums[nums[i] - 1]`. We keep swapping until the number at `nums[i]` is in its correct place, or it's a number we don't care about (negative, zero, or greater than `n`).

### Algorithm

1.  **Place Numbers in Correct Positions:** Iterate through the array with an index `i`.
    -   For the number `nums[i]`, while it is a positive integer within the range `[1, n]` and it is not already at its correct index (i.e., `nums[i] != nums[nums[i] - 1]`):
        -   Swap `nums[i]` with the element at its correct index, `nums[nums[i] - 1]`.
    -   This `while` loop ensures that we continue to place the *new* number at `nums[i]` (after a swap) into its correct position until the condition is no longer met.

2.  **Find the First Mismatch:** After the swapping phase, iterate through the array one more time.
    -   The first index `i` where `nums[i] != i + 1` indicates that `i + 1` is the first missing positive integer.

3.  **Handle the Edge Case:** If the entire array is sorted correctly (i.e., `nums[i] == i + 1` for all `i`), it means the array contains all numbers from `1` to `n`. The first missing positive is `n + 1`.

### Complexity Analysis

-   **Time Complexity:** `O(n)`. Although there is a nested `while` loop, each number is placed in its correct position at most once. In total, the number of swaps is bounded by `n`, leading to an amortized linear time complexity.
-   **Space Complexity:** `O(1)`. The swaps are performed in-place.

---

## Implementation

See `solution.py` for the full implementation of both approaches.