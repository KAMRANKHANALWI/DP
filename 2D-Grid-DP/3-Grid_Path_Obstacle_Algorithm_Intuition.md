## Grid Path with Obstacle — Algorithm & Intuition

**Problem:** Same as Unique Paths, but some cells contain `-1` (obstacles). You cannot pass through an obstacle. Count unique paths from top-left to bottom-right.

```
grid = [[0,  0,  0],
        [0, -1,  0],
        [0,  0,  0]]
→ 2 unique paths
```

---

### Intuition

**The Dream:** Count all paths that avoid blocked cells.

**Key Insight:** Identical to Unique Paths, with one extra rule: if `grid[i][j] == -1`, then `dp[i][j] = 0` — no path can go through here.

```
paths(i, j) = 0                          if grid[i][j] == -1
paths(i, j) = 1                          if i==0 and j==0
paths(i, j) = paths(i-1,j) + paths(i,j-1)  otherwise
```

---

### How Obstacles Propagate

```
An obstacle kills all paths through it — AND all paths that only
route through it. The zero propagates forward.

grid:         dp:
[0,  0,  0]   [1,  1,  1]
[0, -1,  0]   [1,  0,  1]   ← obstacle at (1,1) → dp=0
[0,  0,  0]   [1,  1,  2]   ← (2,2) gets 1 (from left) + 1 (from above)

Answer = dp[2][2] = 2 ✅
```

---

### Dry Run — 3×3 Grid with Center Obstacle

```
   j=0  j=1  j=2
i=0 [ 1,   1,   1  ]   ← top row: left→right, no obstacle, all 1
i=1 [ 1,   0,   1  ]   ← dp[1][1]=-1 → 0; dp[1][2] = dp[0][2]+dp[1][1] = 1+0 = 1
i=2 [ 1,   1,   2  ]   ← dp[2][1] = dp[1][1]+dp[2][0] = 0+1 = 1
                           dp[2][2] = dp[1][2]+dp[2][1] = 1+1 = 2

Answer = 2 ✅

The two paths:
  (0,0)→(1,0)→(2,0)→(2,1)→(2,2)
  (0,0)→(0,1)→(0,2)→(1,2)→(2,2)
```

---

### What if Start or End is an Obstacle?

```
If grid[0][0] == -1: return 0  ← can't even start
If grid[m-1][n-1] == -1: return 0  ← destination blocked

The recursion and tabulation both handle this naturally:
  grid[0][0]==-1 → dp[0][0]=0 → everything downstream = 0.
```

---

### The Obstacle Check Order Matters

```
In tabulation:
    if grid[i][j] == -1:
        dp[i][j] = 0
        continue           ← check BEFORE the base case

    if i == 0 and j == 0:
        dp[i][j] = 1
        continue

This way even if grid[0][0] is an obstacle,
it gets dp=0, not dp=1.
```

---

### Unique Paths vs Obstacle Paths

```
Unique Paths:   dp[i][j] = dp[i-1][j] + dp[i][j-1]  (always)
Obstacle Paths: dp[i][j] = 0  if grid[i][j] == -1
                          = dp[i-1][j] + dp[i][j-1]  otherwise

One extra guard. Same structure.
```

---

### Recurrence Summary

```
dp[0][0] = 1 (if not obstacle)

For each (i, j):
    If grid[i][j] == -1:  dp[i][j] = 0
    Else:                  dp[i][j] = (dp[i-1][j] if i>0 else 0)
                                    + (dp[i][j-1] if j>0 else 0)

Answer = dp[m-1][n-1]
```

---

### Complexity

| Approach | Time | Space |
|---|---|---|
| Memoization | O(M×N) | O(M×N) |
| Tabulation | O(M×N) | O(M×N) |
| Space Optimized | O(M×N) | O(N) |
