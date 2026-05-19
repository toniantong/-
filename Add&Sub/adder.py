def full_adder_bit(a, b, carry_in):
    sum_bit = (a ^ b) ^ carry_in
    carry_out = (a & b) | (carry_in & (a ^ b))
    return sum_bit, carry_out

# 模擬 2 位二進制加法
a_bits = [1, 1]  # 3
b_bits = [0, 1]  # 2
carry = 0
result = []
for i in range(len(a_bits)):
    s, carry = full_adder_bit(a_bits[i], b_bits[i], carry)
    result.append(s)
result.append(carry)
print(result[::-1])  # [0, 1, 0] = 5