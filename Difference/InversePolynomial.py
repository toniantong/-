def reverse_engineer_polynomial(x, y, z):
    """
    根據差分機的初始狀態反推二次方程式 f(n) = an^2 + bn + c
    :param x: f(0) 的值
    :param y: 第一差分 Δ1 的初始值
    :param z: 第二差分 Δ2 的固定值
    """
    # 根據推導公式計算 a, b, c
    a = z / 2
    b = y - (z / 2)
    c = x
    
    # 為了讓結果更漂亮，如果小數點是 .0 就轉成整數
    a = int(a) if a % 1 == 0 else a
    b = int(b) if b % 1 == 0 else b
    c = int(c) if c % 1 == 0 else c
    
    # 組裝方程式字串
    equation = f"f(n) = "
    
    # 處理 a 項
    if a != 0:
        equation += f"{a}n^2 "
        
    # 處理 b 項
    if b > 0 and a != 0:
        equation += f"+ {b}n "
    elif b > 0 and a == 0:
        equation += f"{b}n "
    elif b < 0:
        equation += f"- {abs(b)}n "
        
    # 處理 c 項
    if c > 0:
        equation += f"+ {c}"
    elif c < 0:
        equation += f"- {abs(c)}"
        
    return a, b, c, equation.strip()

# ==========================================
# 測試程式碼
# ==========================================
if __name__ == "__main__":
    # 測試案例 1：我們剛才討論的例子
    # f(0) = 1, Δ1 = 2, Δ2 = 2
    x1, y1, z1 = 1, 2, 2
    a, b, c, eq = reverse_engineer_polynomial(x1, y1, z1)
    print(f"輸入狀態: f(0)={x1}, Δ1={y1}, Δ2={z1}")
    print(f"解出係數: a={a}, b={b}, c={c}")
    print(f"還原方程: {eq}")
    print("-" * 30)

    # 測試案例 2：隨便給一組數字
    # f(0) = 5, Δ1 = 7, Δ2 = 4
    x2, y2, z2 = 5, 7, 4
    a, b, c, eq = reverse_engineer_polynomial(x2, y2, z2)
    print(f"輸入狀態: f(0)={x2}, Δ1={y2}, Δ2={z2}")
    print(f"還原方程: {eq}")