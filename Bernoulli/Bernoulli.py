from fractions import Fraction

def bernoulli_numbers(n):
    """計算前 n 個伯努利數 (B_0 到 B_n)"""
    B = [Fraction(0) for _ in range(n+1)]
    B[0] = Fraction(1)
    for m in range(1, n+1):
        s = Fraction(0)
        for k in range(m):
            s += Fraction(binomial(m+1, k)) * B[k]
        B[m] = -s / Fraction(m+1)
    return B

def binomial(n, k):
    """計算二項式係數"""
    if k < 0 or k > n:
        return 0
    res = 1
    for i in range(1, k+1):
        res = res * (n - i + 1) // i
    return res

# 測試：計算前 12 個伯努利數
B = bernoulli_numbers(12)
for i, b in enumerate(B):
    print(f"B_{i} = {b}")