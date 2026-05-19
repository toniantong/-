def char_to_val(c: str) -> int:
    """輔助函數：將單個 16 進制字元轉換為 0-15 的整數數值"""
    c = c.upper()
    if '0' <= c <= '9':
        return ord(c) - ord('0')
    if 'A' <= c <= 'F':
        return ord(c) - ord('A') + 10
    return 0

def val_to_char(v: int) -> str:
    """輔助函數：將 0-15 的整數數值轉換回 16 進制字元 (大寫)"""
    # 在 Python 中直接用字串索引做對應最簡潔
    return "0123456789ABCDEF"[v]

def hex_add(a: str, b: str) -> str:
    """
    16進制加法函數
    參數: a (加數), b (被加數)
    回傳: 16進制字串結果
    """
    i, j = len(a) - 1, len(b) - 1
    carry = 0
    result = []

    # 當任一字串尚未處理完，或還有進位時繼續執行
    while i >= 0 or j >= 0 or carry > 0:
        val_a = char_to_val(a[i]) if i >= 0 else 0
        val_b = char_to_val(b[j]) if j >= 0 else 0
        
        total = val_a + val_b + carry
        result.append(val_to_char(total % 16)) # 取餘數作為當前位
        carry = total // 16                    # 計算進位 (使用整數除法)
        
        i -= 1
        j -= 1
        
    # 將列表結合成字串並反轉 (因為我們是從最低位開始存入的)
    return "".join(result)[::-1]

def hex_sub(a: str, b: str) -> str:
    """
    16進制減法函數 (前提假設：a >= b，且為無號數)
    參數: a (減數), b (被減數)
    回傳: 16進制字串結果
    """
    i, j = len(a) - 1, len(b) - 1
    borrow = 0
    result = []

    while i >= 0 or j >= 0:
        val_a = char_to_val(a[i]) if i >= 0 else 0
        val_b = char_to_val(b[j]) if j >= 0 else 0
        
        diff = val_a - val_b - borrow
        
        if diff < 0:
            diff += 16  # 向上借位
            borrow = 1
        else:
            borrow = 0
            
        result.append(val_to_char(diff))
        
        i -= 1
        j -= 1
        
    # 將結果反轉，並利用 lstrip 去除多餘的前導零
    final_result = "".join(result)[::-1].lstrip('0')
    
    # 如果結果全為零被清空了，確保至少回傳 "0"
    return final_result if final_result else "0"

# ==========================================
# 測試範例
# ==========================================
if __name__ == "__main__":
    a = "1A9F"
    b = "B2C"

    print(f"數值 A: {a}")
    print(f"數值 B:  {b}")
    print("-" * 20)

    # 測試加法
    print(f"A + B = {hex_add(a, b)}")

    # 測試減法
    print(f"A - B = {hex_sub(a, b)}")
