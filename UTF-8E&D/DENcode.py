# UTF-8 bytes 轉換成 wchar_t (Python str)
utf8_bytes = b'\xe4\xb8\xad\xe6\x96\x87'  # UTF-8 編碼的 "中文"
wchar_string = utf8_bytes.decode('utf-8')
print("UTF-8 -> wchar_t:", wchar_string)

# wchar_t (Python str) 轉換成 UTF-8 bytes
wchar_string = "中文"
utf8_bytes = wchar_string.encode('utf-8')
print("wchar_t -> UTF-8:", utf8_bytes)

# 若需要明確處理 wchar_t (例如 C 語言中的寬字元)，
# 可以透過 Python 的 ctypes 模組模擬 wchar_t 陣列：
import ctypes

# 建立 wchar_t 陣列
wchar_array = (ctypes.c_wchar * len(wchar_string))(*wchar_string)
print("ctypes wchar_t array:", wchar_array[:])