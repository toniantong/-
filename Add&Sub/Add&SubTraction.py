def decimal_add(s1, s2):
    # 補零對齊
    max_len = max(len(s1), len(s2))
    s1, s2 = s1.zfill(max_len), s2.zfill(max_len)
    
    result = ""
    carry = 0
    for i in range(max_len - 1, -1, -1):
        # 計算：(s1編碼 + s2編碼 - '0'的編碼) + 上一輪進位
        # 這裡減去 ord('0') 是為了抵銷其中一個字元攜帶的 48 偏移量
        total = ord(s1[i]) + ord(s2[i]) - ord('0') + carry
        
        if total > ord('9'): # 溢位判斷 (57)
            carry = 1
            total -= 10      # 十進位逢 10 進 1
        else:
            carry = 0
        result = chr(total) + result
        
    return ("1" + result) if carry else result

def decimal_sub(s1, s2):
    # 簡化版：假設 s1 >= s2，且皆為非負字串
    max_len = max(len(s1), len(s2))
    s1, s2 = s1.zfill(max_len), s2.zfill(max_len)
    
    result = ""
    borrow = 0
    for i in range(max_len - 1, -1, -1):
        # 計算：(s1編碼 - s2編碼 + '0'的編碼) - 上一輪借位
        # 加回一個 ord('0') 是為了保持基準在 48
        diff = ord(s1[i]) - ord(s2[i]) + ord('0') - borrow
        
        if diff < ord('0'): # 借位判斷 (48)
            borrow = 1
            diff += 10      # 借 1 當 10 用
        else:
            borrow = 0
        result = chr(diff) + result
        
    return result.lstrip('0') or "0"

# --- 測試 ---
print(f"加法: 17 + 25 = {decimal_add('17', '25')}")   # 輸出: 42
print(f"減法: 50 - 17 = {decimal_sub('50', '17')}")   # 輸出: 33
