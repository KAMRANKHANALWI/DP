## Longest Palindromic Subsequence — Algorithm & Intuition

**Problem:** Find the length of the **longest subsequence** of a string that is a palindrome.

```
s = "bbabcbcab"
→ LPS = "babcbab" or "bacbcab",  length = 7
```

---

### Intuition

**The Dream:** Find the longest way to read the same string forwards and backwards.

**Key Insight:** A palindromic subsequence reads the same from both ends. So if you pick characters from `s` and their reverse, you're looking for common characters in the same relative order.

```
LPS(s) = LCS(s, reverse(s))
```

---

### Why Does This Work?

```
s   = "b b a b c b c a b"
rev = "b a c b c b a b b"

LCS(s, rev) = longest sequence that appears in both s and rev
            = longest sequence that reads the same forwards (in s)
              and backwards (in rev)
            = longest palindromic subsequence ✅
```

```
Concrete example:
s   = "bbabcbcab"
rev = "bacbcbabb"

LCS picks characters that appear in both in order:
  "babcbab" (length 7) → palindrome ✅
```

---

### The Reduction

```
1. rev = s[::-1]
2. return LCS(s, rev)
```

That's literally the entire algorithm. All the LCS code from problem 1 applies directly.

---

### Dry Run — `s = "abcaa"`

```
rev = "aacba"

LCS(s="abcaa", rev="aacba"):

     ""  a  a  c  b  a
""  [ 0,  0,  0,  0,  0,  0 ]
a   [ 0,  1,  1,  1,  1,  1 ]
b   [ 0,  1,  1,  1,  2,  2 ]
c   [ 0,  1,  1,  2,  2,  2 ]
a   [ 0,  1,  2,  2,  2,  3 ]
a   [ 0,  1,  2,  2,  2,  3 ]

LPS = dp[5][5] = 3  → "aaa" (or "aca") ✅
```

---

### Palindrome Properties Used

```
A palindrome s[0..n-1] satisfies: s[i] == s[n-1-i]
→ it matches its own reverse character by character

So a palindromic subsequence of s is a common subsequence of s and s_reversed.
The longest such is the LPS.
```

---

### Downstream Problems Using LPS

```
Minimum Insertions to Palindrome:
    We have a string of length n.
    LPS characters already form a palindrome — keep them.
    We need to insert (n - LPS) characters to make the rest palindromic.
    → answer = n - LPS(s)
```

---

### Recurrence Summary

```
rev = s[::-1]

dp[i][j] = LCS of s[0..i-1] and rev[0..j-1]

If s[i-1] == rev[j-1]:  dp[i][j] = 1 + dp[i-1][j-1]
Else:                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

Answer = dp[n][n]   (both strings have length n)
```

---

### Complexity

| Approach | Time | Space |
|---|---|---|
| Tabulation | O(N²) | O(N²) |
| Space Optimized | O(N²) | O(N) |
