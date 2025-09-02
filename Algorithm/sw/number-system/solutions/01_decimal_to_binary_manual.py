# --- 10진수를 2진수로 변환하는 원리 구현 ---

# 변환하고 싶은 10진수 숫자를 변수에 저장합니다.
target_num = 13

# 2진수의 각 자릿수(나머지)를 순서대로 담을 리스트입니다.
binary_digits = []

# target_num이 0보다 큰 동안 계속 반복합니다.
while ...:
    # 2로 나눈 나머지를 구합니다. (이것이 2진수의 현재 자릿수가 됨)
    remainder = ...
    binary_digits.append(remainder)

    # 다음 계산을 위해, target_num을 2로 나눈 몫으로 갱신합니다.
    target_num = ...

# 나머지를 계산한 순서는 실제 2진수의 역순이므로, 리스트를 뒤집어줍니다.
...

# 최종 변환 결과를 출력합니다.
print(f"10진수 13을 2진수로 변환: {binary_digits}")
