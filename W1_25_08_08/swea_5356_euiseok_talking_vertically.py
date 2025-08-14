import sys
sys.stdin = open('input_5356.txt', 'r')

T = int(input())

for test_case in range(1, T+1):

    big_arr = [list(input()) for _ in range(5)]
    print(big_arr)

    # transpose
    transposed_big_arr = list(zip(*big_arr))
    # [('A', 'a', '0', 'a', 'P'), ('A', 'f', '9', '8', '5'), ('B', 'z', '1', 'E', 'h'), ('C', 'z', '2', 'W', '3')]
    # 이렇게 하면, 끊겨있는 부분에 대해서는 반영하지 못함.
    # # 때문에 아래 출력은 꽉 차있는 열까지만 출력함.

    print(f"#{test_case} ", end='')

    for tu in transposed_big_arr:
        for ele in tu:
            print(ele, end='')

    # 위와 같이 하니, 꽉 찬 행렬은 잘 print 하는데, 비어있는 컬럼부터는 끊겨버림
    # #2 Aa0aPAf985Bz1EhCz2W3


    # 이제, 출력 안 된 애들 찾아서 추가로 출력할 예정

    min_lenn = 16 # 문자열 길이가 15이하
    for row in big_arr:
        if len(row) < min_lenn:
            min_lenn = len(row)
    
    # 이제 프린트를 해야할 기준 좌표는 min_lenn열 0행
    # 거기부터 min_lenn열 1행 ,....,
    # 14열 4행까지 열 방향 순회하면 됨

    for c in range(min_lenn, 15):
        for r in range(0,5):
            try: print(big_arr[r][c] , end='')
            except: pass
    print('') # 끝났으니 엔터

    '''
    for col in big_arr:
        for row in col:
            if len(row) > min_lenn: #출력이 안 되었다면,
                print(col)
    print(min_lenn)

    '''