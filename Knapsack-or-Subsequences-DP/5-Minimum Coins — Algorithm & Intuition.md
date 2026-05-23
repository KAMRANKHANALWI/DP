## Minimum Coins — Algorithm & Intuition

**Problem:** Given coin denominations (unlimited supply of each) and a target amount, find the **minimum number of coins** needed to make the target. Return -1 if impossible.

```
coins = [1, 2, 3],  target = 7
→ 3 coins  (3+3+1 or 3+2+2)
```

---

### Intuition

**The Dream:** Pay the target using as few coins as possible.

**Key Insight:** Coins can be reused — this is an **unbounded knapsack** variant. At each coin, you can pick it (stay at same index, reduce target) or skip it (move to next coin).

```
min_coins(idx, target) = min coins using coins[0..idx] to form target

not_pick = min_coins(idx-1, target)         ← skip this coin
pick     = 1 + min_coins(idx, target-coins[idx])   ← use this coin, stay at idx
return min(pick, not_pick)
```

The crucial detail: `pick` calls `min_coins(idx, ...)` not `idx-1` — staying at the same index means this coin can be picked again.

---

### Unbounded vs 0/1

```
0/1 Knapsack:   pick → dp[idx-1][...]   ← item used once, move to previous
Min Coins:      pick → dp[idx][...]     ← coin reusable, stay at same row

Same problem structure, one line different.
```

---

### Base Case

```
idx == 0 → only coins[0] available

If target % coins[0] == 0:
    return target // coins[0]   ← exact coins needed
Else:
    return inf                  ← impossible with just this coin
```

---

### Dry Run — `coins=[1,2,3]`, target=7

```
dp[idx][t] = min coins to form t using coins[0..idx]

Base row (coin=1, unlimited):
  dp[0][t] = t   for all t  (t coins of value 1)

       t=0  t=1  t=2  t=3  t=4  t=5  t=6  t=7
idx=0  [ 0,   1,   2,   3,   4,   5,   6,   7  ]

idx=1 (coin=2):
  t=0: 0
  t=1: min(dp[0][1]=1, inf) = 1   (can't use coin 2 for t=1)
  t=2: min(dp[0][2]=2, 1+dp[1][0]=1) = 1
  t=3: min(dp[0][3]=3, 1+dp[1][1]=2) = 2
  t=7: min(7, 1+dp[1][5]) = min(7, 1+3) = 4

idx=2 (coin=3):
  t=7: min(dp[1][7]=4, 1+dp[2][4])
       dp[2][4] = min(dp[1][4]=3, 1+dp[2][1])
       dp[2][1] = min(dp[1][1]=1, inf) = 1
       dp[2][4] = min(3, 2) = 2
       dp[2][7] = min(4, 1+2) = 3 ✅

Answer = 3  (e.g. 3+3+1 or 3+2+2)
```

---

### Why `inf` as the Impossible Sentinel

```
Using float('inf') as "impossible":
  min(valid_count, inf) = valid_count   ← inf never wins
  1 + inf = inf                         ← impossible propagates

Final answer: if dp[n-1][target] == inf → return -1
```

---

### Tabulation — Key Detail: Same Row for Pick

```
for idx in range(1, n):
    for t in range(target+1):
        not_pick = dp[idx-1][t]              ← previous row
        pick = 1 + dp[idx][t - coins[idx]]  ← SAME row (unbounded!)
        dp[idx][t] = min(pick, not_pick)
```

This is the one-line difference from 0/1 Knapsack.

---

### Min Coins vs Coin Change II

```
Min Coins:       minimize count     → min(pick, not_pick), pick = 1 + ...
Coin Change II:  count ways         → pick + not_pick, pick = ways
Both:            unbounded (pick stays at same idx)
```

---

### Recurrence Summary

```
dp[0][t] = t//coins[0] if t%coins[0]==0 else inf

dp[idx][t] = min(
    dp[idx-1][t],                        ← not-pick
    1 + dp[idx][t - coins[idx]]          ← pick (if coins[idx] <= t)
)

Answer = dp[n-1][target]  (or -1 if inf)
```

---

### Complexity

| Approach | Time | Space |
|---|---|---|
| Memoization | O(N × target) | O(N × target) |
| Tabulation | O(N × target) | O(N × target) |
| Space Optimized | O(N × target) | O(target) |