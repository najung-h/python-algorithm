import sys
sys.stdin = open('input_security.txt', 'r')


T = int(input())

for test_case in range(1, T+1):
    N = int(input()) # 공간의 넓이
    big_arr = [list(map(int, input().split())) for _ in range(N)]

    #print(big_arr)

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    cnt_1 = 0
    cnt_0 = 0
    fail_to_hide_num = 0


    '''
    전체 리스트를 순회하면서
    2면 경비병의 위치로 저장합니다
    1이면 벽의 개수를 늘려주고
    0이면 길의 개수를 늘려줄겁니다.
    '''
    for rdx in range(N):
        for cdx in range(N):
            if big_arr[rdx][cdx] ==2:
                security_x = rdx
                security_y = cdx

            elif big_arr[rdx][cdx] ==1: # 벽
                cnt_1 += 1
            
            else:
                cnt_0 += 1


    '''
    이제, 확인한 경비병의 위치를 기준으로
    델타 접근법을 사용하겠습니다.
    상/하/좌/우 각 방향에 대해
    갈 수 있다면 계속 한 칸씩 가면서
    fail_to_hide_num을 하나씩 늘려주겠습니다(경비병 관찰 가능한 위치)
    그러다가, 1을 맞닥뜨리는 순간 break하면서 그 방향은 이제 그만 가겠습니다.
    '''            
    for d in range(4):
        for k in range(1, N+1): # N만큼 관찰 가능

            r = security_x + dr[d] * k
            c = security_y + dc[d] * k

            if 0<=r<N and 0<= c < N :
                if big_arr[r][c] == 0:
                    fail_to_hide_num += 1
                else: # 벽이라면 그 방향 그만ㄱ ㅏ
                    break

    '''
    이제는, 원래 갈 수 있는 곳cnt_0의 수에서
    fail_to_hide_num 즉, 경비병의 시선이 닫는 곳의 개수를 빼주겠씁니다.
    '''
    print(f'#{test_case} {cnt_0-fail_to_hide_num}')
                

