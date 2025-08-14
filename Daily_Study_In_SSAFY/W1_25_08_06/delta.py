import sys

sys.stdin = open('input_delta.txt')


T = int(input())


for tc in range(1, T + 1):

    arr_size = int(input())

    big_arr = [list(map(int,input().split())) for _ in range(arr_size)]

    #print(big_arr)



    #print(f'#{tc} {result}')

    neighborhood_elements_lst = []
    abs_sum = 0

    for r, row in enumerate(big_arr):
        for c, col in enumerate(row):
            neighborhood_elements_lst = [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]   # 상 하 좌 우\
            really_neighborhood_elements_lst = []

            for neighborhood in neighborhood_elements_lst:
                m = neighborhood[0]
                n = neighborhood[1]
                if 0<= m <arr_size and 0<= n <arr_size:
                    abs_sum += abs(col - big_arr[m][n])

    print(f'#{tc} {abs_sum}')


