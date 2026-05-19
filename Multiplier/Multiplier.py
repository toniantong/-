# 生成一位數乘法表 (0~9)
multiplier_table = {(i, j): i * j for i in range(10) for j in range(10)}

def multiply_by_table(num1: str, num2: str) -> int:
    """用乘法表計算多位數乘法"""
    digits1 = list(map(int, num1[::-1]))
    digits2 = list(map(int, num2[::-1]))
    result = [0] * (len(digits1) + len(digits2))

    # 筆算乘法：逐位查表
    for i, d1 in enumerate(digits1):
        for j, d2 in enumerate(digits2):
            result[i + j] += multiplier_table[(d1, d2)]

    # 處理進位
    for k in range(len(result)):
        if result[k] >= 10:
            result[k + 1] += result[k] // 10
            result[k] %= 10

    # 去掉前導零並轉成整數
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return int("".join(map(str, result[::-1])))

# 測試
print(multiply_by_table("12", "34"))   # 408
print(multiply_by_table("123", "456")) # 56088
print(multiply_by_table("99", "99"))   # 9801