def count_paths(n, k):
    mod = 10**9 + 7

    if n == 1:
        return 1

    # предрасчет обратных по модулю за O(n)
    inv = [0] * n
    inv[1] = 1
    for i in range(2, n):
        inv[i] = (mod - (mod // i) * inv[mod % i] % mod) % mod

    ans = n % mod
    c = 1

    for d in range(1, n):
        c = c * (k + d) % mod * inv[d] % mod
        cnt = 2 * (n - d) % mod
        ans = (ans + cnt * c) % mod

    return ans
# print (count_paths(2, 2))   # 8
# print (count_paths(4, 5))   # 236
