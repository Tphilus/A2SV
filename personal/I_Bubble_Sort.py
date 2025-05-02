def count_sorted(n, k, q):
    if k >= n:
        return n.factorial() % q
    return k % q