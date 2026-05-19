
class DifferenceEngine:
    def __init__(self, initial_values):
        """
        初始化差分機的齒輪狀態。
        :param initial_values: 一個包含初始數值的列表 [f(0), Δ1, Δ2, Δ3, ... , Δn]
                               其中最後一個元素 Δn 必須是常數。
        """
        # 複製初始數值，這代表機器的初始齒輪狀態
        self.state = list(initial_values)
        self.current_step = 0

    def turn_crank(self):
        """
        模擬轉動差分機的搖柄一次（計算下一個 x 的結果）。
        運算順序是從最高階差分往回加到函數值。
        """
        # 從倒數第二個元素開始，從右向左（從高階往低階）進行加法運算
        for i in range(len(self.state) - 2, -1, -1):
            self.state[i] += self.state[i + 1]
            
        self.current_step += 1
        
        # 狀態列表的第一個元素就是新的 f(x)
        return self.state[0]

    def display_state(self):
        """列印目前的齒輪狀態"""
        print(f"Step {self.current_step}: " + " | ".join(f"{val:4}" for val in self.state))

# ==========================================
# 測試模擬：計算 f(x) = x^2 + x + 1
# ==========================================
if __name__ == "__main__":
    # 初始狀態 (x=0 時)：
    # f(0) = 1
    # Δ1 = 2 (從 f(1)-f(0) 得來)
    # Δ2 = 2 (常數)
    initial_gears = [1, 2, 2]
    
    engine = DifferenceEngine(initial_gears)
    
    print("=== 巴貝奇差分機模擬 ===")
    print("欄位: f(x) |  Δ1  |  Δ2  ")
    print("-" * 25)
    engine.display_state()
    
    # 轉動搖柄 5 次
    for _ in range(5):
        engine.turn_crank()
        engine.display_state()