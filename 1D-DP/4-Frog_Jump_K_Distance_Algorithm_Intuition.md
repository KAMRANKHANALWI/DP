## Frog Jump K Distance — Algorithm & Intuition

**Problem:** Same as Frog Jump, but from index `i` the frog can jump to any of `i+1, i+2, ..., i+k`. Find the **minimum total energy** to reach the last stone.

```
heights = [10, 30, 40, 50, 20],  k = 3
→ minimum cost = 30
```

---

### Intuition

**The Dream:** Same as Frog Jump — reach the end cheapest. But now the frog has k choices at every step instead of 2.

**Key Insight:** `dp[i]` = minimum energy to reach stone `i`. To compute it, try all `j` from 1 to k — i.e., all stones the frog could have jumped from.

```
dp[i] = min over j in [1..k]:
    dp[i-j] + |heights[i] - heights[i-j]|   (if i-j >= 0)
```

---

### From 2 Choices to K Choices

```
Frog Jump (k=2):
  dp[i] = min(
      dp[i-1] + cost(i, i-1),
      dp[i-2] + cost(i, i-2)
  )

Frog Jump K (general):
  dp[i] = min(
      dp[i-1] + cost(i, i-1),
      dp[i-2] + cost(i, i-2),
      ...
      dp[i-k] + cost(i, i-k)
  )

Inner loop replaces the hardcoded two options.
```

---

### Dry Run — `[10, 30, 40, 50, 20]`, k=3

```
dp = [0, 0, 0, 0, 0]
dp[0] = 0   ← start here

i=1:
  j=1: dp[0] + |30-10| = 20
  dp[1] = 20

i=2:
  j=1: dp[1] + |40-30| = 30
  j=2: dp[0] + |40-10| = 30
  dp[2] = 30

i=3:
  j=1: dp[2] + |50-40| = 40
  j=2: dp[1] + |50-30| = 40
  j=3: dp[0] + |50-10| = 40
  dp[3] = 40

i=4:
  j=1: dp[3] + |20-50| = 40+30 = 70
  j=2: dp[2] + |20-40| = 30+20 = 50
  j=3: dp[1] + |20-30| = 20+10 = 30  ← best!
  dp[4] = 30

Answer = dp[4] = 30 ✅
```

```
Optimal path: stone 0 → stone 1 → stone 4
  cost = |30-10| + |20-30| = 20 + 10 = 30
```

---

### Why No Space-Optimized Version Here?

```
Frog Jump (k=2):  dp[i] depends only on dp[i-1] and dp[i-2]
                  → two variables suffice

Frog Jump K:      dp[i] depends on dp[i-1] through dp[i-k]
                  → need the last k values
                  → full dp array needed (or a deque of size k)

Space: O(N) in general (can be O(k) with a sliding window).
```

---

### Recurrence Summary

```
dp[0] = 0

For i from 1 to n-1:
    dp[i] = min(
        dp[i-j] + |heights[i] - heights[i-j]|
        for j in 1..k if i-j >= 0
    )

Answer = dp[n-1]
```

---

### Generalisation Ladder

```
Climbing Stairs (k=2): count paths      → dp[i] = dp[i-1] + dp[i-2]
Frog Jump (k=2):       min cost, 2 hops → dp[i] = min(dp[i-1]+c, dp[i-2]+c)
Frog Jump K:           min cost, k hops → dp[i] = min over j in [1..k]
```

Each step is a natural extension: more choices in the inner loop, same DP structure.

---

### Complexity

| Approach | Time | Space |
|---|---|---|
| Recursive (no memo) | O(k^N) | O(N) stack |
| Memoization | O(N × k) | O(N) |
| Tabulation | O(N × k) | O(N) |
