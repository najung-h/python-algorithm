# 1234 비밀번호
# 4873 코드 재사용

import sys
sys.stdin = open('input_1234.txt', 'r')

T = 10

for test_case in range(1, T+1):
    N, lst = input().split()

    N = int(N)
    lst = list(map(int, lst))
    # [1, 2, 3, 8, 0, 9, 9, 0, 8, 4]

    while True:
        if len(lst) <2:
            break

        found = False

        for idx in range(len(lst)-1):
            if lst[idx] == lst[idx+1]:
                lst.pop(idx+1)  # 뒤에부터 pop
                lst.pop(idx)
                found = True
                break

        if found is False:
            break


    print(f"#{test_case} {''.join(map(str, lst))}")
