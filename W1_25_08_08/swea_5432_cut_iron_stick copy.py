# 5432. 쇠막대기 자르기

import sys
sys.stdin = open('input_5432.txt', 'r')

T = int(input())

for test_case in range(1, T+1):

    str = input()
    print(str)
    
    laser_start_lst = []
    laser_end_lst = []
    # [0, 5, 7, 11, 14, 19]
    # [1, 6, 8, 12, 15, 20]

    first_laser_start_lst = []
    first_laser_end_lst = []
    # [4, 10, 18]
    # [9, 13, 21]

    second_laser_start_lst = []
    second_laser_end_lst = []

    for idx, i in enumerate(str):
        if i == '(' and str[idx+1] == ')':
            laser_start_lst.append(idx) # 레이저와 연관된 애들
            laser_end_lst.append(idx+1)

    for i in laser_start_lst:
        if i != 0 and str[i-1] == '(':
            first_laser_start_lst.append(i-1)
            for jdx, j in enumerate(str):
                if jdx > i and j == ')' and jdx not in laser_end_lst:
                    first_laser_end_lst.append(jdx)
                    break

    for i in first_laser_start_lst:
        if i != 0 and str[i-1] == '(':
            second_laser_start_lst.append(i-1)
            for jdx, j in enumerate(str):
                if jdx > i and j == ')' and jdx not in laser_end_lst and jdx not in first_laser_end_lst:
                    second_laser_end_lst.append(jdx)
                    break

    print(second_laser_start_lst)
    print(second_laser_end_lst)





    print(f"#{test_case} ")