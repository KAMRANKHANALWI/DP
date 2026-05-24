## Coin Change II — Algorithm & Intuition

**Problem:** Given coin denominations (unlimited supply) and a target, count the **number of ways** to make the target.

```
coins = [1, 2, 5],  target = 5
→ 4 ways: {5}, {2,2,1}, {2,1,1,1}, {1,1,1,1,1}
```

---

### Intuition

**The Dream:** Count every distinct combination of coins that sums to target.

**Key Insight:** Coins are reusable (unbounded). At each coin, pick it (stay at same index, reduce target) or skip it (move to previous coin). Add both counts.

```
coin_change_2(idx, target) = ways using coins[0..idx] to form target

not_pick = coin_change_2(idx-1, target)         ← skip coin
pick     = coin_change_2(idx, target-coins[idx]) ← reuse coin, stay at idx
return pick + not_pick
```

---

### The Family Comparison

```
Problem          | Operation    | Unbounded | Goal
-----------------|--------------|-----------|------
Subset Sum       | OR           | No        | existence
Count Subsets    | +            | No        | count
Min Coins        | min(1+...)   | Yes       | minimize count
Coin Change II   | +            | Yes       | count ways
```

Coin Change II = Count Subsets + unbounded reuse (stay at same index for pick).

---

### Base Case

```
idx == 0 → only coins[0] available

If target % coins[0] == 0: return 1   ← one way: use target//coins[0] of this coin
Else:                       return 0   ← impossible
```

---

### Dry Run — `coins=[1,2,5]`, target=5

```
dp[idx][t] = ways to form t using coins[0..idx]

Base row (coin=1, unlimited):
  dp[0][t] = 1 for all t (one way: use t coins of value 1)

       t=0  t=1  t=2  t=3  t=4  t=5
idx=0  [ 1,   1,   1,   1,   1,   1 ]

idx=1 (coin=2, unlimited):
  t=0: 1
  t=1: not_pick=dp[0][1]=1, pick=dp[1][-1]→0 → 1
  t=2: not_pick=dp[0][2]=1, pick=dp[1][0]=1  → 2
  t=3: not_pick=1,          pick=dp[1][1]=1  → 2
  t=4: not_pick=1,          pick=dp[1][2]=2  → 3
  t=5: not_pick=1,          pick=dp[1][3]=2  → 3

       t=0  t=1  t=2  t=3  t=4  t=5
idx=1  [ 1,   1,   2,   2,   3,   3 ]

idx=2 (coin=5, unlimited):
  t=5: not_pick=dp[1][5]=3, pick=dp[2][0]=1  → 4

Answer = 4 ✅
```

---

### Key Tabulation Detail — Same Row for Pick

```
for idx in range(1, n):
    for t in range(target+1):
        not_pick = dp[idx-1][t]           ← previous row
        pick     = dp[idx][t-coins[idx]]  ← SAME row → unbounded reuse
        dp[idx][t] = pick + not_pick
```

This is identical to Min Coins except `pick = dp[idx][...]` and we sum (not min).

---

### Combinations Not Permutations

```
This counts {2,2,1} and {2,1,1,1} as distinct from {1,1,2,2} or {1,2,2,1}?

No — it counts unique COMBINATIONS (sets of coin counts), not orderings.
{2,2,1} is counted once regardless of arrangement order.

The DP naturally handles this: by iterating coins as the outer loop
and target as the inner loop, each combination is counted exactly once.
```

---

### Recurrence Summary

```
dp[0][t] = 1 if t % coins[0] == 0 else 0

dp[idx][t] = dp[idx-1][t]            ← not-pick
           + dp[idx][t - coins[idx]] ← pick (if coins[idx] <= t)

Answer = dp[n-1][target]
```

---

### Complexity

| Approach | Time | Space |
|---|---|---|
| Memoization | O(N × target) | O(N × target) |
| Tabulation | O(N × target) | O(N × target) |
| Space Optimized | O(N × target) | O(target) |