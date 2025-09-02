# --- 10진수를 2진수로 변환하는 원리 구현 ---

# 변환하고 싶은 10진수 숫자를 변수에 저장합니다.
target_num = 13

# 2진수의 각 자릿수(나머지)를 순서대로 담을 리스트입니다.
binary_digits = []

# target_num이 0이 될 때까지 (더 이상 나눌 수 없을 때까지) 반복합니다.
while target_num > 0:
    # 2로 나눈 나머지를 구합니다. (0 또는 1)
    # 이 나머지가 2진수의 현재 자릿수가 됩니다.
    remainder = target_num % 2
    binary_digits.append(remainder)

    # 다음 계산을 위해, target_num을 2로 나눈 몫으로 갱신합니다.
    # (예: 13 -> 6, 6 -> 3, ...)
    target_num //= 2

# 나머지를 계산한 순서는 실제 2진수의 역순이므로, 리스트를 뒤집어줍니다.
# (예: [1, 0, 1, 1] -> [1, 1, 0, 1])
binary_digits.reverse()

# 최종 변환 결과를 출력합니다.
print(f"10진수 13을 2진수로 변환: {binary_digits}")  # [1, 1, 0, 1]
