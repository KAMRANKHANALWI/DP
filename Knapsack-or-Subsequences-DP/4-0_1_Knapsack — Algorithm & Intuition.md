## 0/1 Knapsack — Algorithm & Intuition

**Problem:** Given items with weights and values, and a knapsack of fixed capacity, choose items to **maximise total value**. Each item can be picked at most once (0 or 1 times).

```
weights  = [1, 2, 4, 5]
values   = [5, 4, 8, 6]
capacity = 5
→ max value = 13   (items with weight 1 and 4: value 5+8)
```

---

### Intuition

**The Dream:** Take every item — but the bag has limited capacity.

**Key Insight:** At each item, pick or skip. If you pick, you gain its value but lose its weight from remaining capacity.

```
knapsack(idx, cap) = max value using items 0..idx with capacity cap

If can't pick (weight > cap): not_pick only
Else:
    not_pick = knapsack(idx-1, cap)
    pick     = values[idx] + knapsack(idx-1, cap - weights[idx])
    return max(pick, not_pick)
```

---

### The DP State

```
dp[idx][cap] = max value achievable
               using items from 0..idx
               with knapsack capacity = cap

Dimensions:
  idx ∈ [0, n-1]
  cap ∈ [0, capacity]
```

---

### Dry Run — `weights=[1,2,4,5]`, `values=[5,4,8,6]`, capacity=5

```
Base row (idx=0, item weight=1, value=5):
  dp[0][cap] = 5   for cap >= 1
  dp[0][0]   = 0   (can't fit)

       cap=0  cap=1  cap=2  cap=3  cap=4  cap=5
idx=0  [  0,    5,    5,    5,    5,    5  ]
idx=1  [  0,    5,    5,    9,    9,    9  ]   ← item(w=2,v=4): cap≥2 → 5+4=9
idx=2  [  0,    5,    5,    9,    9,   13  ]   ← item(w=4,v=8): cap=5→5+8=13
idx=3  [  0,    5,    5,    9,    9,   13  ]   ← item(w=5,v=6): only at cap=5 → max(13,6)=13

Answer = dp[3][5] = 13 ✅
Optimal: pick item 0 (w=1,v=5) + item 2 (w=4,v=8) → total weight=5, value=13
```

---

### Pick vs Not-Pick Logic

```
At dp[idx][cap]:

not_pick = dp[idx-1][cap]
           ↑ same capacity, previous item row

pick = values[idx] + dp[idx-1][cap - weights[idx]]
       ↑ gain value, reduce capacity, look at previous row

→ key: BOTH pick and not_pick look at dp[idx-1][...]
       because each item used at most once (0/1)
```

---

### 0/1 vs Unbounded Knapsack

```
0/1 Knapsack (this problem):
  pick = values[idx] + dp[idx-1][cap - weights[idx]]   ← previous row
  Each item used at most once.

Unbounded Knapsack (Coin Change):
  pick = values[idx] + dp[idx][cap - weights[idx]]     ← same row
  Each item can be reused infinitely.

The only difference: which row pick reads from.
```

---

### Base Case Initialization

```
For first item (idx=0):
  If weights[0] <= cap → dp[0][cap] = values[0]
  Else                 → dp[0][cap] = 0

Loop: for cap in range(weights[0], capacity+1): dp[0][cap] = values[0]
```

---

### Recurrence Summary

```
dp[0][cap] = values[0]  if weights[0] <= cap, else 0

dp[idx][cap] = max(
    dp[idx-1][cap],                                   ← not-pick
    values[idx] + dp[idx-1][cap - weights[idx]]       ← pick (if fits)
)

Answer = dp[n-1][capacity]
```

---

### Complexity

| Approach | Time | Space |
|---|---|---|
| Memoization | O(N × capacity) | O(N × capacity) |
| Tabulation | O(N × capacity) | O(N × capacity) |
| Space Optimized | O(N × capacity) | O(capacity) |