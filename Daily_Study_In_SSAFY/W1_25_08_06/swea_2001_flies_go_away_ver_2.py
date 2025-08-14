import sys
sys.stdin = open('input_2001.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    # N * N 짜리 전체 행렬에서 M * M 짜리 파리채를 휘둘러
    N, M = list(map(int, input().split()))
    big_arr = [list(map(int, input().split())) for _ in range(N)]

    # 최대로 죽는 파리의 개수를 구하자!
    max_flies = 0

    k = N - M +1   # 자르는 경우의 수 # 각 행마다

    # 행 방향으로 돌게요
    for row in range(k):
        for col in range(k):

            # 각각의 좌표에서 초기 파리값을 설정합니다.
            flies = 0
            #print(f'{row}, {col} 에는 {flies}마리가 있어요')


            row_lst = list(range(row, row + M))
            col_lst = list(range(col, col + M))

            for r in row_lst:
                for c in col_lst:
                    if 0<= r < N and 0<= c < N:
                        flies += big_arr[r][c]
                        #print(f'근처 {r}, {c} 에는 {big_arr[r][c]}마리가 있어요')

            #print(f'이번에는 총 {flies}마리가 죽었어요')
            if flies > max_flies:
                max_flies = flies

    print(f"#{test_case} {max_flies}")