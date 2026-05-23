## Max Sum of Non-Adjacent Elements — Algorithm & Intuition

**Problem:** Given an array, pick a subset of elements such that **no two picked elements are adjacent**. Maximise the sum.

```
arr = [2, 1, 4, 9]
→ pick 2 and 9  (indices 0 and 3, not adjacent)
→ sum = 11  ✅  (or pick 2 and 4 = 6, or just 9 = 9)
```

---

### Intuition

**The Dream:** Greedily grab the biggest elements — but you can't take two in a row.

**Key Insight:** At every index `i`, you face exactly two choices:

```
PICK arr[i]:
    Can't use arr[i-1]. Best from rest = dp[i-2].
    Value = arr[i] + dp[i-2]

DON'T PICK arr[i]:
    arr[i-1] is still available.
    Value = dp[i-1]

dp[i] = max(pick, not_pick)
```

---

### Why `dp[i-2]` When You Pick?

```
arr = [2, 1, 4, 9]
           ↑ pick 4 (index 2)

Can't pick 1 (index 1) — adjacent.
Best available from [0..0] = dp[1-1] = dp[0] = arr[0] = 2

pick = arr[2] + dp[0] = 4+2 = 6
```

Picking at index `i` means the previous valid pick was at most at index `i-2`.

---

### Dry Run — `[2, 1, 4, 9]`

```
dp[0] = 2   ← only element available

i=1:
  pick     = arr[1] + dp[-1] = 1 + 0 = 1   (dp[-1] = 0, out of bounds)
  not_pick = dp[0] = 2
  dp[1] = max(1, 2) = 2

i=2:
  pick     = arr[2] + dp[0] = 4 + 2 = 6
  not_pick = dp[1] = 2
  dp[2] = max(6, 2) = 6

i=3:
  pick     = arr[3] + dp[1] = 9 + 2 = 11
  not_pick = dp[2] = 6
  dp[3] = max(11, 6) = 11

Answer = dp[3] = 11 ✅   (picked index 0 and index 3: 2+9)
```

---

### Space Optimized — Two Variables

```
prev2 = 0   (dp[i-2], initially out-of-bounds = 0)
prev  = arr[0] = 2   (dp[i-1])

i=1:
  pick  = arr[1] + prev2 = 1+0 = 1
  not_p = prev = 2
  curi  = 2
  prev2 = 2, prev = 2

i=2:
  pick  = arr[2] + prev2 = 4+2 = 6
  not_p = prev = 2
  curi  = 6
  prev2 = 2, prev = 6

i=3:
  pick  = arr[3] + prev2 = 9+2 = 11
  not_p = prev = 6
  curi  = 11
  prev2 = 6, prev = 11

return prev = 11 ✅
```

---

### Handling `i < 0` (Out of Bounds)

```
In recursion: base case `if i < 0: return 0`
In tabulation: `if i > 1: pick += dp[i-2]` (else pick = just arr[i])
In space opt:  prev2=0 handles the "nothing before index 0" case
```

All three approaches handle the same edge — they just express it differently.

---

### Recurrence Summary

```
dp[0] = arr[0]

dp[i] = max(
    arr[i] + (dp[i-2] if i >= 2 else 0),   ← pick
    dp[i-1]                                  ← don't pick
)

Answer = dp[n-1]
```

---

### Complexity

| Approach | Time | Space |
|---|---|---|
| Memoization | O(N) | O(N) |
| Tabulation | O(N) | O(N) |
| Space Optimized | O(N) | O(1) |
