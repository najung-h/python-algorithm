# --- 16진수 문자열을 2진수 문자열로 변환 (10진수 정수를 거쳐가는 방법) ---

# 1. 16진수 문자열 'A7'을 10진수 정수로 변환
decimal_value = int('A7', 16)  # 167

# 2. 10진수 정수 167을 2진수 문자열로 변환
binary_string = bin(decimal_value)

print(binary_string)  # '0b10100111'
print(binary_string[2:])  # '10100111'
