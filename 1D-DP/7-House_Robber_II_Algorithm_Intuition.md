## House Robber II — Algorithm & Intuition

**Problem:** Same as House Robber I, but the houses are arranged in a **circle** — the first and last house are adjacent. You can't rob both.

```
nums = [2, 3, 2]
→ can't rob house 0 and house 2 together (circular adjacency)
→ best = 3  (rob only house 1) ✅
```

---

### Intuition

**The Dream:** Rob the most money from a circular street.

**Key Insight:** In a circle, house `0` and house `n-1` are neighbours. So you can never rob both. This gives exactly two valid scenarios:

```
Case 1: Exclude house n-1  → rob from nums[0 .. n-2]
Case 2: Exclude house 0   → rob from nums[1 .. n-1]

Answer = max(Case 1, Case 2)
```

Both sub-problems are now **linear** (no circularity) — just run House Robber I on each slice.

---

### Why Two Cases Cover Everything

```
Either house 0 is robbed OR it isn't:

If house 0 IS robbed:
  → house n-1 cannot be robbed (adjacent in circle)
  → effectively solve linear problem on [0..n-2]
  → but since we're maximizing, "excluding n-1" includes the possibility of not robbing 0 too
  → Case 1 = rob_linear(nums[:-1]) handles all scenarios where n-1 is excluded

If house 0 is NOT robbed:
  → house n-1 might be robbed (no circular constraint now)
  → Case 2 = rob_linear(nums[1:]) handles this

Taking max of both gives the global optimum.
```

---

### Dry Run — `[2, 3, 2]`

```
n=3, nums=[2,3,2]

Case 1: nums[:-1] = [2,3]
  rob_linear([2,3]):
    prev2=0, prev=2
    i=1: pick=3+0=3, not=2 → curi=3, prev=3
    return 3

Case 2: nums[1:] = [3,2]
  rob_linear([3,2]):
    prev2=0, prev=3
    i=1: pick=2+0=2, not=3 → curi=3, prev=3
    return 3

max(3, 3) = 3 ✅
```

---

### Dry Run — `[1, 2, 3, 1]`

```
Case 1: [1,2,3]
  prev2=0, prev=1
  i=1: pick=2, not=1 → prev2=1, prev=2
  i=2: pick=3+1=4, not=2 → prev=4
  return 4

Case 2: [2,3,1]
  prev2=0, prev=2
  i=1: pick=3, not=2 → prev2=2, prev=3
  i=2: pick=1+2=3, not=3 → prev=3
  return 3

max(4, 3) = 4 ✅   (rob houses 0 and 2: 1+3)
```

---

### Edge Case — Single House

```
nums = [5]
n=1 → return nums[0] = 5 immediately
(slicing would give empty arrays, handled separately)
```

---

### The Two-Slice Trick — General Principle

Whenever a linear DP problem gets a "circular" constraint added, the standard fix is:

```
Run the linear DP twice:
  Once excluding the first element
  Once excluding the last element
Take the max.
```

This same trick appears in problems like "Circular Maximum Subarray" and "Delete and Earn (circular)" variants.

---

### Recurrence Summary

```
def rob(nums):
    if n == 1: return nums[0]
    return max(rob_linear(nums[:-1]),
               rob_linear(nums[1:]))

def rob_linear(nums):   ← House Robber I on a slice
    prev2=0, prev=nums[0]
    for i in 1..len(nums)-1:
        curi = max(nums[i]+prev2, prev)
        prev2=prev, prev=curi
    return prev
```

---

### Complexity

| | |
|---|---|
| Time | O(N) — two linear passes |
| Space | O(1) — space-optimized linear solver |
