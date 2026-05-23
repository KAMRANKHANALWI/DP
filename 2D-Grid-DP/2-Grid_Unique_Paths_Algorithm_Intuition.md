## Grid Unique Paths — Algorithm & Intuition

**Problem:** Given an `m × n` grid, count the number of unique paths from the **top-left** `(0,0)` to the **bottom-right** `(m-1, n-1)`. You can only move **right** or **down**.

```
m=3, n=2 (3 rows, 2 cols)
→ 3 unique paths
```

---

### Intuition

**The Dream:** Count every possible route.

**Key Insight:** To reach cell `(i, j)`, you must have come from either:
- `(i-1, j)` — moved down
- `(i, j-1)` — moved right

So `paths(i,j) = paths(i-1, j) + paths(i, j-1)`.

```
Grid (3×2):

(0,0) → (0,1)
  ↓       ↓
(1,0) → (1,1)
  ↓       ↓
(2,0) → (2,1) ← destination
```

---

### Building the DP Table

```
Base cases:
  Row 0 (top row):  can only come from the left → all 1s
  Col 0 (left col): can only come from above   → all 1s

   j=0  j=1
i=0 [ 1 ,  1 ]
i=1 [ 1 ,  2 ]
i=2 [ 1 ,  3 ]

dp[1][1] = dp[0][1] + dp[1][0] = 1+1 = 2
dp[2][1] = dp[1][1] + dp[2][0] = 2+1 = 3

Answer = dp[2][1] = 3 ✅
```

---

### Dry Run — `m=3, n=3`

```
   j=0  j=1  j=2
i=0 [ 1,   1,   1  ]
i=1 [ 1,   2,   3  ]
i=2 [ 1,   3,   6  ]

dp[1][1] = dp[0][1]+dp[1][0] = 1+1 = 2
dp[1][2] = dp[0][2]+dp[1][1] = 1+2 = 3
dp[2][1] = dp[1][1]+dp[2][0] = 2+1 = 3
dp[2][2] = dp[1][2]+dp[2][1] = 3+3 = 6

Answer = 6  (C(4,2) = 6 confirms this) ✅
```

---

### Space Optimization — Row-by-Row

```
Only need the previous row to compute the current row.

prev = [1, 1, 1]   ← row 0 (all 1s)

Row 1:
  curr[0] = 1  (left column, always 1)
  curr[1] = prev[1] + curr[0] = 1+1 = 2
  curr[2] = prev[2] + curr[1] = 1+2 = 3
  prev = [1, 2, 3]

Row 2:
  curr[0] = 1
  curr[1] = prev[1] + curr[0] = 2+1 = 3
  curr[2] = prev[2] + curr[1] = 3+3 = 6
  prev = [1, 3, 6]

return prev[n-1] = 6 ✅
```

---

### Mathematical Formula (Bonus)

```
Total steps = (m-1) downs + (n-1) rights = (m+n-2) steps
Choose which (m-1) steps are "down":

Answer = C(m+n-2, m-1) = (m+n-2)! / ((m-1)! × (n-1)!)

For m=3, n=3: C(4,2) = 6 ✅
```

The DP and combinatorics give the same answer — DP is used when obstacles exist (next problem).

---

### Recurrence Summary

```
dp[0][j] = 1  for all j       ← top row
dp[i][0] = 1  for all i       ← left column

dp[i][j] = dp[i-1][j] + dp[i][j-1]   ← came from above or from left

Answer = dp[m-1][n-1]
```

---

### Complexity

| Approach | Time | Space |
|---|---|---|
| Memoization | O(M×N) | O(M×N) |
| Tabulation | O(M×N) | O(M×N) |
| Space Optimized | O(M×N) | O(N) |
