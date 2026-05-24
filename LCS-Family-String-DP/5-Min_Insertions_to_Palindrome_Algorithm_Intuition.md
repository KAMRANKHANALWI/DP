## Minimum Insertions to Make a Palindrome — Algorithm & Intuition

**Problem:** Find the minimum number of characters to **insert** into a string to make it a palindrome.

```
s = "abcaa"
→ 1 insertion   (insert 'b' or 'c' to get "abcba" or "aabcbaa"... wait)

s = "abcaa":
  LPS = "aaa" (length 3) or "aca" (length 3)
  n=5, LPS=3 → insertions = 5-3 = 2

Actually: "abcaa" → insert 'b','c' → "abcba" needs 2 ops? 
  "abcaa" → insert 'b' at end → "abcaab" (not palindrome)
  Optimal: "aabcbaa"? That's 2 insertions (one 'a' at start, one at somewhere)

Let me check: LPS("abcaa"):
  rev = "aacba"
  LCS("abcaa", "aacba") = ?
  Common chars in order: "a_a" = 3? → "aaa" length 3
  n=5, LPS=3, insertions = 5-3 = 2
```

---

### Intuition

**The Dream:** Make the string read the same forwards and backwards with minimal additions.

**Key Insight:** Characters that already form a palindromic subsequence (the LPS) don't need to change — they're already "balanced". The remaining `n - LPS` characters each need a mirror partner inserted.

```
n = length of string
LPS = longest palindromic subsequence length

minimum insertions = n - LPS
```

---

### Why `n - LPS`?

```
Think of building a palindrome from s:
  Keep the LPS characters in place — they're already symmetric.
  For every character NOT in LPS:
    → It has no palindromic partner in the string.
    → Insert its mirror image on the other side.
    → Each such character needs exactly 1 insertion.

Characters not in LPS = n - LPS
Each needs 1 insertion → total = n - LPS
```

```
Example: s = "ab", LPS = "a" (length 1)
  'b' has no partner → insert 'b' → "bab" or "abb" → need 1 insertion ✅
  n - LPS = 2 - 1 = 1 ✅
```

---

### The Algorithm — One Line After LPS

```
def minimum_insertions_to_palindrome(s):
    lps = longest_palindromic_subsequence(s)   ← problem 4
    return len(s) - lps
```

Literally just compute LPS and subtract from n. All the work is in the LPS computation.

---

### Dry Run — `s = "abcaa"`

```
rev = "aacba"

LCS("abcaa", "aacba"):
     ""  a  a  c  b  a
""  [ 0,  0,  0,  0,  0,  0 ]
a   [ 0,  1,  1,  1,  1,  1 ]
b   [ 0,  1,  1,  1,  2,  2 ]
c   [ 0,  1,  1,  2,  2,  2 ]
a   [ 0,  1,  2,  2,  2,  3 ]
a   [ 0,  1,  2,  2,  2,  3 ]

LPS = 3

min insertions = 5 - 3 = 2 ✅
```

---

### Alternative View — Edit Distance to Palindrome

```
Minimum insertions to palindrome is equivalent to:
  Minimum edit distance between s and reverse(s)
  where only insertions/deletions are allowed
  → (n + n - 2 × LCS(s, rev)) / 2
  = (2n - 2 × LPS) / 2
  = n - LPS ✅

Same answer, different derivation.
```

---

### Connection to Min Insert/Delete (Problem 6)

```
Min Insertions to Palindrome:
  Convert s to a palindrome (target = reverse of s, same length)
  Only insertions allowed → n - LPS

Min Insert/Delete (general):
  Convert s1 to s2 (arbitrary target)
  Both insertions and deletions allowed → (n - LCS) + (m - LCS)
```

---

### Recurrence Summary

```
rev = s[::-1]

LPS = LCS(s, rev) = dp[n][n]   ← standard LCS

Answer = n - LPS
```

---

### Complexity

| Approach | Time | Space |
|---|---|---|
| Tabulation | O(N²) | O(N²) |
| Space Optimized | O(N²) | O(N) |
