## Print Longest Common Subsequence — Algorithm & Intuition

**Problem:** Don't just find the LCS length — **reconstruct and print the actual LCS string**.

```
s1 = "abcde",  s2 = "ace"
→ LCS = "ace"
```

---

### Intuition

**The Dream:** Follow the decisions you made during DP — backwards.

**Key Insight:** The LCS DP table encodes every decision (match, skip s1, skip s2). Start from `dp[n][m]` and trace back to `dp[0][0]` by reversing the choices. Collect matched characters along the way.

---

### Two Phases

```
Phase 1 — Build the DP table:
    Identical to LCS tabulation.
    dp[i][j] = LCS length of s1[0..i-1] and s2[0..j-1]

Phase 2 — Backtrack from dp[n][m]:
    At each cell (i, j):
        If s1[i-1] == s2[j-1]:  ← match
            ADD s1[i-1] to result
            Move diagonally → i--, j--

        Else:  ← no match, retrace the decision
            If dp[i-1][j] > dp[i][j-1]:
                Move up → i--      (we skipped from s1)
            Else:
                Move left → j--    (we skipped from s2)

    Continue until i==0 or j==0
    Reverse the collected characters
```

---

### Why Reverse at the End?

```
Backtracking goes from end → start.
Characters are appended in reverse order.
Reversing at the end gives the correct LCS.
```

---

### Dry Run — `s1="abcde"`, `s2="ace"`

```
DP table:
     ""  a  c  e
""  [ 0,  0,  0,  0 ]
a   [ 0,  1,  1,  1 ]
b   [ 0,  1,  1,  1 ]
c   [ 0,  1,  2,  2 ]
d   [ 0,  1,  2,  2 ]
e   [ 0,  1,  2,  3 ]

Backtrack from (5, 3):
  (5,3): s1[4]='e' == s2[2]='e' → ADD 'e', move to (4,2)
  (4,2): s1[3]='d' != s2[1]='c' → dp[3][2]=2, dp[4][1]=1 → 2>1 → move up → (3,2)
  (3,2): s1[2]='c' == s2[1]='c' → ADD 'c', move to (2,1)
  (2,1): s1[1]='b' != s2[0]='a' → dp[1][1]=1, dp[2][0]=0 → 1>0 → move up → (1,1)
  (1,1): s1[0]='a' == s2[0]='a' → ADD 'a', move to (0,0)
  i=0 → STOP

Collected (reversed): e,c,a → reverse → "ace" ✅
```

---

### The Backtrack Decision Logic

```
At cell (i, j) where s1[i-1] != s2[j-1]:

    dp[i-1][j] > dp[i][j-1] → move UP  (i--)
                               we came from the row above when building table
                               meaning we skipped s1[i-1] to achieve this value

    else                     → move LEFT (j--)
                               we skipped s2[j-1]

Equal values: either direction works (multiple valid LCS exist, pick either)
```

---

### Why Not Recursively Reconstruct?

```
Recursive reconstruction is possible but messy — multiple branches possible when dp[i-1][j] == dp[i][j-1].
Table backtracking is clean: one linear pass, O(N+M) after the DP.
```

---

### Complexity

| Phase | Time | Space |
|---|---|---|
| Build DP table | O(N × M) | O(N × M) |
| Backtrack | O(N + M) | O(LCS length) |
| Total | O(N × M) | O(N × M) |
