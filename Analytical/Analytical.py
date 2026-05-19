class AnalyticalEngine:
    def __init__(self):
        self.store = {}  # 記憶體
        self.mill = None # 運算結果

    def load(self, address, value):
        self.store[address] = value

    def add(self, addr1, addr2, result_addr):
        self.mill = self.store[addr1] + self.store[addr2]
        self.store[result_addr] = self.mill

    def multiply(self, addr1, addr2, result_addr):
        self.mill = self.store[addr1] * self.store[addr2]
        self.store[result_addr] = self.mill

    def output(self, address):
        print(f"Output from store[{address}]: {self.store[address]}")

# 使用範例
engine = AnalyticalEngine()
engine.load("A", 5)
engine.load("B", 7)
engine.add("A", "B", "C")
engine.output("C")   # 輸出 12
engine.multiply("C", "B", "D")
engine.output("D")   # 輸出 84