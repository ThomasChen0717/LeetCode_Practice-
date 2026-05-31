# 2126. Destroying Asteroids

**Difficulty:** <span style="color:#f39c12"><b>Medium</b></span>  
**Topics:** Array, Greedy, Sorting

---

## Problem Description

You are given an integer `mass`, which represents the original mass of a planet. You are further given an integer array `asteroids`, where `asteroids[i]` is the mass of the `i`th asteroid.

You can arrange for the planet to collide with the asteroids in **any arbitrary order**. If the mass of the planet is **greater than or equal to** the mass of the asteroid, the asteroid is **destroyed** and the planet **gains** the mass of the asteroid. Otherwise, the planet is destroyed.

Return `true` if **all** asteroids can be destroyed. Otherwise, return `false`.

---

## Examples

**Example 1:**
```
Input: mass = 10, asteroids = [3,9,19,5,21]
Output: true
```
**Explanation:** 
One way to order the asteroids is [3, 5, 9, 19, 21]:
- Planet collides with mass 3. New mass: 10 + 3 = 13.
- Planet collides with mass 5. New mass: 13 + 5 = 18.
- Planet collides with mass 9. New mass: 18 + 9 = 27.
- Planet collides with mass 19. New mass: 27 + 19 = 46.
- Planet collides with mass 21. New mass: 46 + 21 = 67.
All asteroids are destroyed.

**Example 2:**
```
Input: mass = 5, asteroids = [4,9,23,4]
Output: false
```
**Explanation:** 
The planet cannot ever gain enough mass to destroy the asteroid with a mass of 23.
After the planet destroys the other asteroids, it will have a mass of 5 + 4 + 4 + 9 = 22.
This is less than 23, so a collision would not destroy the last asteroid.

## Constraints

- `1 <= mass <= 10^5`
- `1 <= asteroids.length <= 10^5`
- `1 <= asteroids[i] <= 10^5`

---

## Approach: Greedy

### Intuition

The problem states that we can collide with the asteroids in any order. This suggests that we should try to find an optimal order of collisions. The goal is to destroy all asteroids. To maximize our chances of destroying larger asteroids later, we should try to increase our planet's mass as quickly as possible with the least risk.

The best way to do this is to collide with the smallest asteroids first. This is a greedy strategy. By destroying smaller asteroids, we increase our mass, which in turn makes it possible to destroy even larger asteroids. If we can't destroy the smallest available asteroid, we certainly won't be able to destroy any of the larger ones.

Therefore, the optimal strategy is to sort the `asteroids` array in ascending order and then iterate through them. For each asteroid, we check if our current mass is sufficient. If it is, we add the asteroid's mass to our planet's mass and proceed. If at any point our mass is less than the asteroid's mass, it's impossible to continue, and we can immediately return `false`.

If we successfully iterate through all the asteroids, it means they can all be destroyed, and we return `true`.

### Complexity Analysis

- **Time Complexity:** `O(N log N)`, where `N` is the number of asteroids. This is dominated by the sorting step.
- **Space Complexity:** `O(1)` or `O(log N)` depending on the implementation of the sorting algorithm. In Python, `sort()` is in-place and has a space complexity of `O(log N)` for the call stack.

---

## Implementation

See `solution.py` for the full implementation.
