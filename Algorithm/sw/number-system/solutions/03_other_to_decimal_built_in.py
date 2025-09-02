# --- int() 함수를 사용하여 다양한 진법의 '문자열'을 10진수 '정수'로 변환 ---

# '1101' 문자열을 2진수(base=2)로 간주하고 10진수로 변환합니다.
decimal_from_binary = int('1101', 2)
print(f"int('1101', 2) => {decimal_from_binary}")  # 13

# 'A7' 문자열을 16진수(base=16)로 간주하고 10진수로 변환합니다.
decimal_from_hex = int('A7', 16)
print(f"int('A7', 16) => {decimal_from_hex}")  # 167

# '15' 문자열을 8진수(base=8)로 간주하고 10진수로 변환합니다.
decimal_from_octal = int('15', 8)
print(f"int('15', 8) => {decimal_from_octal}")  # 13
