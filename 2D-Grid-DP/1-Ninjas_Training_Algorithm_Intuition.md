## Ninja's Training — Algorithm & Intuition

**Problem:** A ninja trains over `n` days. Each day has 3 activities with point values. The ninja **can't do the same activity on consecutive days**. Maximise total points.

```
points = [
    [10, 40, 70],   ← day 0: activities A, B, C
    [20, 50, 80],   ← day 1
    [30, 60, 90],   ← day 2
]
→ maximum points = 210
```

---

### Intuition

**The Dream:** Do the highest-point activity every day.

**Key Insight:** You can't repeat. So track **which activity was done last** (`last`) and try all other activities for the current day. The state is `(day, last_activity)`.

```
dp[day][last] = max points from day 0..day
                when 'last' was the activity done on 'day'
```

---

### The State Space

```
day ∈ [0, n-1]
last ∈ [0, 1, 2, 3]   ← 0,1,2 = activities; 3 = "no previous activity" (start)

dp is a (n × 4) table
```

---

### Recurrence

```
For each day, try all 3 activities:
  Skip the one that equals 'last' (no repeat rule)

dp[day][last] = max over task ≠ last:
    points[day][task] + dp[day-1][task]
```

---

### Dry Run — 3 Days

```
points = [[10,40,70],[20,50,80],[30,60,90]]

Base case (day=0):
  dp[0][0] = max(40,70) = 70   ← last=0 (A used), best of B,C
  dp[0][1] = max(10,70) = 70   ← last=1 (B used), best of A,C
  dp[0][2] = max(10,40) = 40   ← last=2 (C used), best of A,B
  dp[0][3] = max(10,40,70) = 70 ← last=3 (no restriction), best of all

Day 1 (using dp[0]):
  dp[1][0]: task=1 → 50+dp[0][1]=120, task=2 → 80+dp[0][2]=120  → 120
  dp[1][1]: task=0 → 20+dp[0][0]=90,  task=2 → 80+dp[0][2]=120  → 120
  dp[1][2]: task=0 → 20+dp[0][0]=90,  task=1 → 50+dp[0][1]=120  → 120
  dp[1][3]: task=0 → 20+dp[0][0]=90,  task=1 → 50+dp[0][1]=120,
            task=2 → 80+dp[0][2]=120 → 120

Day 2 (using dp[1]):
  dp[2][3]: task=0 → 30+dp[1][0]=150,
            task=1 → 60+dp[1][1]=180,
            task=2 → 90+dp[1][2]=210  ← best!

Answer = dp[2][3] = 210 ✅
```

```
Optimal path: day0=C(70), day1=B(50)... wait:
day0=C(70), day1=B(50→120 total)? But day2 answer is 210:
day0=C(70), day1=B(50), day2=A(30)? 70+50+30=150. No.
day0=B(40)→dp[0][2]=40, then day1=C(80)→120, day2=B(60)→180. Still not 210.
day0=C(70), day1=C... can't repeat.

Actually: day0=C(70), day1 can't do C → best is B(50)=120. day2 can't do B → best is C(90)=210. ✅
70 + 50 + 90 = 210 ✅
```

---

### Space Optimization — Drop the 2D Table

```
Only need the previous day's row → use a 1D `prev` array of size 4.

For each day: compute `temp[4]` from `prev[4]`, then prev=temp.
```

---

### Why `last=3` as the Initial State?

```
On the very first call, no activity has been done yet.
last=3 means "no restriction" — all 3 activities are valid.

After day 0, last ∈ {0,1,2} (whichever activity was chosen).
Using index 3 as a sentinel avoids a special case.
```

---

### Recurrence Summary

```
Base (day=0):
  dp[0][last] = max(points[0][task] for task ≠ last)

Transition:
  dp[day][last] = max over task ≠ last:
      points[day][task] + dp[day-1][task]

Answer = dp[n-1][3]
```

---

### Complexity

| Approach | Time | Space |
|---|---|---|
| Memoization | O(N × 4 × 3) = O(N) | O(N × 4) |
| Tabulation | O(N × 4 × 3) = O(N) | O(N × 4) |
| Space Optimized | O(N × 4 × 3) = O(N) | O(4) = O(1) |
