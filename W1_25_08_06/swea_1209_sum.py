# swea_1209_sum
# 각 행의 합, 각 열의 합, 각 대각선의 합 중 최댓값을 구하라

import sys
sys.stdin = open('input_1209.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    big_arr =  [list(map(int, input().split())) for _ in range(100)]
    #print(big_arr)
    #print(len(big_arr))

    row_sum_lst = [0] * 100   # 각 행의 합
    col_sum_lst = [0] * 100   # 각 열의 합
    left_diagonal_sum = 0  # 좌측 상단에서 시작하는 대각선 합
    right_diagonal_sum = 0


    for idx, row in enumerate(big_arr):
        row_sum_lst[idx] = sum(row)   # 각 행의 합
        for cdx, col in enumerate(row):
            col_sum_lst[cdx] += col   # 해당 열에 해당하는 원소를 그 인덱스값에 계속 더해나가기
            if idx == cdx :           # 대각선
                left_diagonal_sum += col
            elif idx + cdx == 99:
                right_diagonal_sum += col

    # 전치행렬로 구현하면 편할 것 같았는데
    # 그냥 이중 반복문으로 해결하게 되었습니다.

    max_row = max(row_sum_lst)
    max_col = max(col_sum_lst)

    result = max(max_row, max_col, left_diagonal_sum, right_diagonal_sum)

    print(f'{test_case} {result}')
    

