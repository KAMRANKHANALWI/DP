## Partition Equal Subset Sum — Algorithm & Intuition

**Problem:** Given an array, can it be split into **two subsets with equal sum**?

```
arr = [1, 5, 11, 5]
→ True   ([1,5,5] and [11], both sum to 11)

arr = [1, 2, 3, 5]
→ False  (total=11, odd → impossible)
```

---

### Intuition

**The Dream:** Find a split where both halves are perfectly balanced.

**Key Insight:** If total sum is `S` and we split into two equal parts, each part must sum to `S/2`. So the problem reduces to:

```
Can we find a subset that sums to S/2?
→ This is exactly Subset Sum.
```

---

### The Reduction

```
total = sum(arr)

If total is ODD → impossible (can't split into two equal integers)
  → return False immediately

target = total // 2

If any subset sums to target:
  → the remaining elements automatically sum to target too
  → partition exists → return True
```

```
arr = [1, 5, 11, 5]
total = 22, target = 11

Find subset summing to 11:
  [1, 5, 5] → 11 ✅
  Remaining [11] → 11 ✅

Partition found!
```

---

### Why We Only Need to Find One Half

```
If subset P sums to target = total/2,
the complement Q = arr \ P automatically sums to total - target = total/2.

We never need to explicitly find Q.
```

---

### Early Exit Cases

```
1. total % 2 != 0 → return False   (odd total can't split evenly)

2. max(arr) > total//2 → return False
   (one element alone exceeds half — can't balance)
   [This isn't in the code but is a useful early exit]

3. arr = [x] (single element) → return False
   (can't split a single element into two non-empty subsets)
```

---

### Dry Run — `[1, 5, 11, 5]`

```
total = 22, target = 11

Run Subset Sum on arr with target=11:

       t=0  ...  t=5  t=6  ...  t=11
idx=0  [ T,       F,   F,        F  ]   ← arr[0]=1
idx=1  [ T,       T,   T,        F  ]   ← arr[1]=5
idx=2  [ T,       T,   T,        T  ]   ← arr[2]=11: dp[1][11-11]=dp[1][0]=T ✅
idx=3  ...

Answer = True ✅
```

---

### Connection to Subset Sum

```
partition_equal_subset_sum(arr):
    total = sum(arr)
    if total % 2 != 0: return False
    target = total // 2
    return subset_sum(arr, target)   ← exactly problem 1
```

This is a **pure reduction** — no new DP logic, just a smarter problem formulation.

---

### Recurrence Summary

```
Same as Subset Sum, just with target = sum(arr) // 2

dp[idx][0] = True
dp[0][arr[0]] = True   (if arr[0] <= target)

dp[idx][t] = dp[idx-1][t] OR dp[idx-1][t - arr[idx]]

Answer = dp[n-1][target]
```

---

### Complexity

| Approach | Time | Space |
|---|---|---|
| Memoization | O(N × S/2) | O(N × S/2) |
| Tabulation | O(N × S/2) | O(N × S/2) |
| Space Optimized | O(N × S/2) | O(S/2) |

Where S = sum of array.