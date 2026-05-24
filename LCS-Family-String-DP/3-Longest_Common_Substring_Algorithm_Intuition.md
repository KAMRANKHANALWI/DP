## Longest Common Substring — Algorithm & Intuition

**Problem:** Find the length of the longest **contiguous** substring common to both strings. Unlike LCS, the characters must be adjacent.

```
s1 = "abcdgh",  s2 = "acdghr"
→ longest common substring = "cdgh",  length = 4
```

---

### Intuition

**The Dream:** Find the longest unbroken run of matching characters.

**Key Insight:** One critical change from LCS — when characters **don't** match, there's no "skip and continue". The substring is **broken**. Reset to zero.

```
LCS:        mismatch → max(dp[i-1][j], dp[i][j-1])   ← try skipping either
Substring:  mismatch → dp[i][j] = 0                  ← substring ENDS here
```

---

### The DP State

```
dp[i][j] = length of longest common substring
           ENDING at s1[i-1] and s2[j-1]

Key word: ENDING. dp[i][j] only counts the current run.
The global answer is tracked separately with `maxi`.
```

---

### LCS vs Substring — Side by Side

```
Match:    dp[i][j] = 1 + dp[i-1][j-1]    ← same for both

Mismatch:
  LCS:       dp[i][j] = max(dp[i-1][j], dp[i][j-1])  ← carry forward
  Substring: dp[i][j] = 0                              ← reset!
```

```
LCS can skip characters to maintain a subsequence.
Substring cannot — the run must be continuous.
```

---

### Why Track `maxi` Separately?

```
In LCS: the answer is always at dp[n][m] (the last cell).
In Substring: dp[n][m] only holds the length of the
              common substring ENDING at (n,m).
              The actual longest might have ended earlier.

So we update maxi at every match:
    if s1[i-1] == s2[j-1]:
        dp[i][j] = 1 + dp[i-1][j-1]
        maxi = max(maxi, dp[i][j])   ← capture global max
```

---

### Dry Run — `s1="abcdgh"`, `s2="acdghr"`

```
     ""  a  c  d  g  h  r
""  [ 0,  0,  0,  0,  0,  0,  0 ]
a   [ 0,  1,  0,  0,  0,  0,  0 ]   ← 'a'='a' → 1
b   [ 0,  0,  0,  0,  0,  0,  0 ]   ← 'b'≠all → 0
c   [ 0,  0,  1,  0,  0,  0,  0 ]   ← 'c'='c' → 1
d   [ 0,  0,  0,  2,  0,  0,  0 ]   ← 'd'='d' → 1+dp[2][1]=0+1... wait

Let me redo carefully:
  dp[3][2]: s1[2]='c', s2[1]='c' → match → 1+dp[2][1]
  dp[2][1]: s1[1]='b', s2[0]='a' → no match → 0
  dp[3][2] = 1+0 = 1

  dp[4][3]: s1[3]='d', s2[2]='d' → match → 1+dp[3][2]=1+1=2
  dp[5][4]: s1[4]='g', s2[3]='g' → match → 1+dp[4][3]=1+2=3
  dp[6][5]: s1[5]='h', s2[4]='h' → match → 1+dp[5][4]=1+3=4

maxi = 4  → "cdgh" ✅
```

---

### Space Optimization

```
Only need previous row (for dp[i-1][j-1]):
  prev = row i-1
  curr = row i

  if match: curr[j] = 1 + prev[j-1]
  else:     curr[j] = 0
```

---

### Common Gotcha — LCS vs Substring Confusion

```
"abcde" and "ace":
  LCS = 3 ("ace")     ← subsequence, skips allowed
  Substring = 1 ("a") ← no skips, first common contiguous block

Never mix them up — the reset-to-zero on mismatch is the entire difference.
```

---

### Recurrence Summary

```
dp[0][j] = 0, dp[i][0] = 0   (empty string base)
maxi = 0

If s1[i-1] == s2[j-1]:
    dp[i][j] = 1 + dp[i-1][j-1]
    maxi = max(maxi, dp[i][j])
Else:
    dp[i][j] = 0               ← substring breaks

Answer = maxi
```

---

### Complexity

| Approach | Time | Space |
|---|---|---|
| Tabulation | O(N × M) | O(N × M) |
| Space Optimized | O(N × M) | O(M) |
