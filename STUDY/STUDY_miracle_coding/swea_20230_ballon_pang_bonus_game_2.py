import sys
sys.stdin = open('input_20230.txt', 'r')


def get_ballon_num(now_point):
    '''
    이 함수는 지금의 위치(튜플)와 현재 얻은 포인트 값을 넣어주면
    현 위치에서 같은 행과 열의 풍선을 터뜨려서
    점수를 다 더해서 return 해주는 함수입니다.
    '''
    row = now_point[0]
    col = now_point[1]

    dr = (-1, 1, 0, 0)
    dc = (0, 0, -1, 1)

    result = big_arr[row][col]

    # 풍선이 터지는 것의 최대가 
    

    for d in range(4):
        for k in range(1, N):
            r = row + dr[d] * k
            c = col + dc[d] * k
            
            if 0<=r<N and 0<=c<N :
                result += big_arr[r][c]
                #print(f'{r},{c}도 터뜨려봐요!')
            else: 
                break # 그 방향은 더 이상 뻗어나가지 않아도 돼..

    return result





T = int(input())

for test_case in range(1, T+1):
    N = int(input())   # 격자의 크기
    big_arr = [list(map(int, input().split())) for _ in range(N)]

    max_ballon = 0

    for rdx in range(N):
        for cdx in range(N):
            now_point = (rdx,cdx)
            #print(f'지금은 {now_point}에 있어요!')
            now_ballon = get_ballon_num(now_point)
            #print(f'여기서 풍선을 터뜨리니 {now_ballon}개를 터뜨릴 수 있군요..')
            if  now_ballon > max_ballon:
                #print(f'!!!!!어머나 {now_ballon}개라니! 최대 풍선이에요!')
                max_ballon = now_ballon


    print(f"#{test_case} {max_ballon}")


 
