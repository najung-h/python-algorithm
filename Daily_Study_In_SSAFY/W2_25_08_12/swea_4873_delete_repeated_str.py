# 4873 반복문자 지우기

import sys
sys.stdin = open('input_4873.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    lst = list(input())

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


    print(f"#{test_case} {len(lst)}")
