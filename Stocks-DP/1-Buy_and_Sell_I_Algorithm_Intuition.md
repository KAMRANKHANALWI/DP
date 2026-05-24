## Buy and Sell Stock I — Algorithm & Intuition

**Problem:** Given an array of prices, find the **maximum profit** from a **single buy and sell** transaction. You must buy before you sell.

```
prices = [7, 1, 5, 3, 6, 4]
→ buy at 1, sell at 6 → profit = 5
```

---

### Intuition

**The Dream:** Buy at the lowest point, sell at the highest — but you must buy first.

**Key Insight:** On any day `i`, the best profit if you sell today = `prices[i] - min_price_so_far`. Track the running minimum and the running max profit in one pass.

```
For each day:
    profit_today = prices[i] - min_price
    max_profit   = max(max_profit, profit_today)
    min_price    = min(min_price, prices[i])
```

---

### Why This is Greedy, Not DP

```
This is actually a greedy problem — not classical DP.
No overlapping subproblems, no memoization needed.

At each step you greedily:
  1. Ask "if I sold today, what's my profit?"
  2. Update the cheapest buy point seen so far.

One pass, O(1) space.
```

That said, Buy and Sell II (unlimited transactions) does use DP.

---

### Dry Run — `[7, 1, 5, 3, 6, 4]`

```
min_price = 7, max_profit = 0

day | price | profit=price-min | max_profit | min_price
----|-------|-----------------|------------|----------
 0  |   7   |     7-7=0       |     0      |    7
 1  |   1   |     1-7=-6      |     0      |    1    ← new min
 2  |   5   |     5-1=4       |     4      |    1
 3  |   3   |     3-1=2       |     4      |    1
 4  |   6   |     6-1=5       |     5      |    1    ← new max profit
 5  |   4   |     4-1=3       |     5      |    1

Answer = 5 ✅  (buy at 1, sell at 6)
```

---

### Edge Cases

```
Prices always falling: [7, 6, 4, 3, 1]
  Every profit = negative → max_profit stays 0
  Return 0 (no transaction is better than a losing one)

Single day: [5] → can't buy and sell → profit = 0

All same: [3,3,3,3] → profit = 0
```

---

### What If You Could Sell Before Buying?

```
You can't — the running min tracks only elements seen SO FAR.
min_price is always from a past day → buy always precedes sell.
```

---

### Algorithm

```
min_price  = prices[0]
max_profit = 0

For i from 1 to n-1:
    profit     = prices[i] - min_price
    max_profit = max(max_profit, profit)
    min_price  = min(min_price, prices[i])

Return max_profit
```

---

### Comparison with Buy and Sell II

```
Buy and Sell I:
  1 transaction max
  Greedy: track min_price, O(N) time, O(1) space
  No DP needed

Buy and Sell II:
  Unlimited transactions
  DP with state (idx, buy): dp[idx][buy]
  O(N) time, O(N) or O(1) space

Buy and Sell I is the simplest stock problem.
All others build on this intuition with more constraints.
```

---

### Complexity

| | |
|---|---|
| Time | O(N) — single pass |
| Space | O(1) — two variables |
