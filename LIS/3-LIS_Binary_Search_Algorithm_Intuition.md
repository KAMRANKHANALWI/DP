## LIS — Binary Search Optimization O(N log N) — Algorithm & Intuition

**Problem:** Same as LIS — find the length. But now in **O(N log N)** instead of O(N²).

```
arr = [10, 9, 2, 5, 3, 7, 101, 18]
→ LIS length = 4
```

---

### Intuition

**The Dream:** Process each element once and decide instantly where it fits in the LIS — no inner loop scanning all previous elements.

**Key Insight:** Maintain an array `temp` where `temp[i]` = **smallest possible tail element of any increasing subsequence of length i+1** seen so far. This array is always sorted, enabling binary search.

---

### The `temp` Array — What It Represents

```
temp is NOT the actual LIS.
temp[i] = the minimum ending value for an IS of length (i+1).

The length of temp = the length of the LIS.

"Smallest possible tail" → gives future elements the best chance to extend.
```

---

### The Algorithm — Two Cases Per Element

```
For each num in arr:

Case 1: num > temp[-1]  → num extends the longest IS
    temp.append(num)
    LIS length grows by 1

Case 2: num <= temp[-1]  → num can't extend, but might improve a tail
    Find the first element in temp >= num (using binary search)
    Replace it with num (smaller tail = better for future extensions)
    LIS length unchanged
```

---

### Dry Run — `[10, 9, 2, 5, 3, 7, 101, 18]`

```
temp = []

num=10: temp=[] → append → temp=[10]
num=9:  9<10 → bisect_left([10],9)=0 → replace → temp=[9]
num=2:  2<9  → bisect_left([9],2)=0  → replace → temp=[2]
num=5:  5>2  → append → temp=[2,5]
num=3:  3<5  → bisect_left([2,5],3)=1 → replace → temp=[2,3]
num=7:  7>3  → append → temp=[2,3,7]
num=101:101>7 → append → temp=[2,3,7,101]
num=18: 18<101 → bisect_left([2,3,7,101],18)=3 → replace → temp=[2,3,7,18]

len(temp) = 4 ✅
```

---

### Why Replacing Doesn't Break Anything

```
temp = [2, 3, 7, 101]
num = 18 → replace 101 with 18 → temp = [2, 3, 7, 18]

Does this mess up the LIS we already found [2,3,7,101]?
NO — because the LIS length (4) is already recorded in len(temp).
temp is just tracking tails for FUTURE elements.

If a future element is between 18 and 101, it can now extend
the length-4 subsequence (which wasn't possible with 101 as tail).
Replacing 101 with 18 makes future extensions more possible.
```

---

### `bisect_left` — Lower Bound

```
bisect_left(arr, target) = first index where arr[idx] >= target
                         = "lower bound"

Why "first index >= target" and not "first index > target"?
    We want strictly increasing: replace the first element
    that is >= current num (i.e., not strictly smaller).
    This ensures the IS remains strictly increasing.
```

---

### `temp` is NOT the Actual LIS

```
arr = [3, 5, 6, 2, 5, 4, 19, 5, 6, 7, 12]

After processing: temp = [2, 4, 5, 6, 7, 12]  (length 6)

But temp itself is NOT a valid LIS of arr!
The actual LIS is [3, 5, 6, 7, 12] or [2, 4, 5, 6, 12] etc.

temp only stores the optimal TAILS — not the sequence itself.
To reconstruct, you'd need the parent pointer approach (problem 2).
```

---

### The Lower Bound Implementation

```python
def lower_bound(arr, target):
    lo, hi = 0, len(arr)-1
    ans = len(arr)       # default: target > all elements
    while lo <= hi:
        mid = (lo+hi)//2
        if arr[mid] >= target:
            ans = mid
            hi = mid-1   # search left for smaller valid index
        else:
            lo = mid+1
    return ans
```

`bisect_left` from Python's standard library does this in one call.

---

### Comparison of All LIS Approaches

```
Approach              | Time       | Space | Reconstruct?
----------------------|------------|-------|------------
Brute Force Recursion | O(2^N × N) | O(N)  | No
Memoization           | O(N²)      | O(N²) | Hard
Tabulation dp[i]      | O(N²)      | O(N)  | Yes (problem 2)
Binary Search         | O(N log N) | O(N)  | No (temp isn't LIS)
```

---

### Complexity

| | |
|---|---|
| Time | O(N log N) — one binary search per element |
| Space | O(N) — the temp array |
