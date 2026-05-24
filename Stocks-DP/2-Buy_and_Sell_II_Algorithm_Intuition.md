## Buy and Sell Stock II — Algorithm & Intuition

**Problem:** Given daily prices, find the **maximum profit with unlimited transactions**. You can hold at most one stock at a time (must sell before buying again).

```
prices = [7, 1, 5, 3, 6, 4]
→ buy at 1, sell at 5 (profit 4) + buy at 3, sell at 6 (profit 3)
→ total profit = 7
```

---

### Intuition

**The Dream:** Capture every upswing in the market.

**Key Insight:** At each day, you're in one of two states:
- `buy=1` → allowed to buy (you don't hold a stock)
- `buy=0` → must sell (you hold a stock)

From each state, you can act or skip. This is a clean 2-state DP.

```
dp[idx][buy] = max profit from day idx onward, in state 'buy'
```

---

### The State Transitions

```
If buy=1 (can buy):
    take    = -prices[idx] + dp[idx+1][0]   ← buy today (spend money), now must sell
    not_take = dp[idx+1][1]                  ← skip buying
    dp[idx][1] = max(take, not_take)

If buy=0 (must sell):
    sell     = prices[idx] + dp[idx+1][1]   ← sell today (earn money), can buy again
    not_sell  = dp[idx+1][0]                ← hold stock one more day
    dp[idx][0] = max(sell, not_sell)
```

---

### Why Negative for Buying?

```
Buying costs money → subtract price.
Selling earns money → add price.

Tracking profit as a running sum:
  buy at price 1 → running total -= 1
  sell at price 5 → running total += 5
  net = +4 ✅
```

---

### Dry Run — `[7, 1, 5, 3, 6, 4]`

```
Base case: dp[6][0] = dp[6][1] = 0  (no days left)

Fill backwards:

idx=5 (price=4):
  buy=1: max(-4+dp[6][0], dp[6][1]) = max(-4,0) = 0
  buy=0: max(4+dp[6][1], dp[6][0])  = max(4,0)  = 4

idx=4 (price=6):
  buy=1: max(-6+dp[5][0], dp[5][1]) = max(-6+4,0) = max(-2,0) = 0
  buy=0: max(6+dp[5][1], dp[5][0])  = max(6+0,4)  = 6

idx=3 (price=3):
  buy=1: max(-3+dp[4][0], dp[4][1]) = max(-3+6,0) = 3
  buy=0: max(3+dp[4][1], dp[4][0])  = max(3+0,6)  = 6

idx=2 (price=5):
  buy=1: max(-5+dp[3][0], dp[3][1]) = max(-5+6,3) = max(1,3) = 3
  buy=0: max(5+dp[3][1], dp[3][0])  = max(5+3,6)  = 8

idx=1 (price=1):
  buy=1: max(-1+dp[2][0], dp[2][1]) = max(-1+8,3) = max(7,3) = 7
  buy=0: max(1+dp[2][1], dp[2][0])  = max(1+3,8)  = 8

idx=0 (price=7):
  buy=1: max(-7+dp[1][0], dp[1][1]) = max(-7+8,7) = max(1,7) = 7
  buy=0: ...

Answer = dp[0][1] = 7 ✅
```

---

### Space Optimization — "ahead" Array

```
dp only ever reads from idx+1 (next day).
→ Only need ONE array of size 2: `ahead[buy]`

ahead = [0, 0]   ← base case (idx=n)

for idx from n-1 down to 0:
    curr[1] = max(-prices[idx] + ahead[0], ahead[1])   ← can buy
    curr[0] = max(prices[idx]  + ahead[1], ahead[0])   ← must sell
    ahead = curr

return ahead[1]   ← start with ability to buy
```

---

### Greedy Alternative (Simpler for This Specific Problem)

```
Since transactions are unlimited, a simpler greedy works:
  Collect profit on every day where prices[i] > prices[i-1].
  profit += max(0, prices[i] - prices[i-1])

For [7,1,5,3,6,4]:
  day1→2: 5-1=4 ✅
  day3→4: 6-3=3 ✅
  total = 7 ✅

This is O(N), O(1). The DP approach generalises to problems
with transaction limits (k transactions, cooldown, fee) where
greedy no longer works.
```

---

### Recurrence Summary

```
dp[n][0] = dp[n][1] = 0

dp[idx][1] = max(-prices[idx] + dp[idx+1][0], dp[idx+1][1])
dp[idx][0] = max(prices[idx]  + dp[idx+1][1], dp[idx+1][0])

Answer = dp[0][1]
```

---

### Complexity

| Approach | Time | Space |
|---|---|---|
| Memoization | O(N × 2) = O(N) | O(N × 2) |
| Tabulation | O(N) | O(N × 2) |
| Space Optimized | O(N) | O(1) |
