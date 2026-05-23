## Subset Sum — Algorithm & Intuition

**Problem:** Given an array and a target, determine if any subset of the array sums exactly to the target.

```
arr = [1, 2, 3, 4],  target = 4
→ True   ([1,3] or [4])
```

---

### Intuition

**The Dream:** Try every possible subset, stop the moment one sums to target.

**Key Insight:** At every index, you have two choices — pick the element (reduce target) or skip it (leave target unchanged). This is the canonical **pick / not-pick** DP pattern.

```
subset_sum(idx, target) = True  if any subset of arr[0..idx] sums to target

If target == 0:  True   ← empty subset always valid
If idx == 0:     arr[0] == target   ← only one element left
Else:
    not_pick = subset_sum(idx-1, target)
    pick     = subset_sum(idx-1, target - arr[idx])  if arr[idx] <= target
    return pick or not_pick
```

---

### The DP State

```
dp[idx][t] = can we form sum t using elements from arr[0..idx]?

Dimensions:
  idx ∈ [0, n-1]     → which elements are available
  t   ∈ [0, target]  → remaining target to achieve
```

---

### Dry Run — `[1,2,3,4]`, target=4

```
dp table (n=4, target=4):
       t=0   t=1   t=2   t=3   t=4
idx=0  [ T,    T,    F,    F,    F  ]   ← can only form 0 or 1
idx=1  [ T,    T,    T,    T,    F  ]   ← can add 2: forms 0,1,2,3
idx=2  [ T,    T,    T,    T,    T  ]   ← add 3: 1+3=4 ✅
idx=3  [ T,    T,    T,    T,    T  ]

Answer = dp[3][4] = True ✅

dp[0][0]=T (empty subset)
dp[0][1]=T (arr[0]=1 == target 1)
dp[1][3]=T (pick 1+2=3, or just 3... wait arr[1]=2):
  pick: dp[0][3-2]=dp[0][1]=T ✅
dp[2][4]: pick → dp[1][4-3]=dp[1][1]=T ✅
```

---

### Base Case Initialization (Tabulation)

```
All dp[idx][0] = True    ← target=0 always achievable (empty subset)
dp[0][arr[0]] = True     ← using only first element, can form arr[0]
```

---

### Key Difference: Boolean vs Count vs Max

```
Subset Sum:       dp[i][t] = bool    → pick OR not_pick
Count Subsets:    dp[i][t] = int     → pick + not_pick
0/1 Knapsack:     dp[i][cap] = int   → max(pick, not_pick)
```

Same pick/not-pick structure — only the combination operation changes.

---

### Space Optimization — Why Iterate t in Any Order

```
For 0/1 knapsack (each item used once):
  pick reads from prev row → safe to iterate any direction

For unbounded knapsack (infinite reuse):
  pick reads from current row → must iterate t left-to-right
  (covered in Coin Change / Min Coins)
```

Here it's 0/1 (each element used at most once) → prev row for pick → any order safe.

---

### Recurrence Summary

```
dp[idx][0] = True   for all idx
dp[0][arr[0]] = True

dp[idx][t] = dp[idx-1][t]                    ← not-pick
          OR dp[idx-1][t - arr[idx]]          ← pick (if arr[idx] <= t)

Answer = dp[n-1][target]
```

---

### Complexity

| Approach | Time | Space |
|---|---|---|
| Memoization | O(N × target) | O(N × target) |
| Tabulation | O(N × target) | O(N × target) |
| Space Optimized | O(N × target) | O(target) |