import sys
sys.stdin = open('input_1211.txt', 'r')


'''
기존에 보셨던 사다리 문제는 바닥에 도착하는지를 확인했는데요
이번에는 어느 사다리를 골라야 최단거리인지를 구합니다.
때문에 순방향으로 모든 시작점에서 사다리를 타기 시작하고
움직일 때마다 거리를 1씩 추가해보려고 합니다.
'''

# 델타접근법을 사용하겠습니다. 다만, 순서는 오른쪽 왼쪽 아래쪽 순서에요
dr = [0, 0, +1]
dc = [+1, -1, 0]


# 각 출발점에 대해서 사다리를 타고, 이동한 거리를 기록하는 함수입니다.
def distance_for_each_start_point(cdx):
    now_r = 0
    now_c = cdx
    moving = 0 # 이동 거리 초기화

    before_r = -1
    before_c = -1

    while now_r < 99:
        for d in range(3):
            new_r = now_r + dr[d]
            new_c = now_c + dc[d]
            #print(f'{new_r}, {new_c}쪽으로 갈 수 있는지 확인해볼게요!')

            if 0<= new_r<100 and 0<=new_c<100 and big_arr[new_r][new_c] == 1 and (new_r, new_c) != (before_r, before_c) : # 범위 내 ^ 갈 수 있으면
                # 갔던 곳 다시 안 가게끔
                before_c = now_c
                before_r = now_r
                now_r = new_r
                now_c = new_c
                moving += 1
                break  
        
        else: # 아무곳도 갈 수 없었어.
            if now_r == 99:
                return moving
            else: print('error')
    
    return moving





T = 10

for test_case in range(1, T+1):
    tc = int(input())
    big_arr = [list(map(int, input().split())) for _ in range(100)]

    # 1. 첫 번째 줄에서 시작할 수 있는 위치를 확인하여 list에 담습니다.
    start_lst = []
    for cdx in range(100):
        if big_arr[0][cdx] == 1:
            start_lst.append(cdx)

    #print(start_lst)


    # 2. start list의 각 시작점에서 출발합니다.
    min_moving = 999999999999999
    result = 0
    
    for start in start_lst:
        moving = distance_for_each_start_point(start)
        #print(f'{moving}번 움직였어요!')
        if moving < min_moving:
            min_moving = moving
            result = start


    # 끄읕
    print(f'#{test_case} {result}')
