import sys
sys.stdin = open('input_2383.txt', 'r')

'''
이동이 완료되는 최소의 시간을 출력하라
이동시간은 택시 거리로 계산한다.
만약에 계단 위에 사람이 3 명 이상이라면,
더 이상 계단에 진입할 수 없다.
== 그 중 한 명이 계단을 완전히 내려갈 때까지 계단 입구에서 대기해야 한다.
1분에 한 칸씩 내려갈 수 있다.

그런데, 계단이 여러 개가 있다는 점이 개어려운 포인트

완탐밖에 방법이 없나??

계단은 2개
사람은 1- 10개

사람이 3명 이하라면,
그냥 생각할 거 없이 이동거리 + 계단 길이 더해서 최대 시간 출력하면 된다.

사람의 총 이동시간은 
이동거리 + 계단 길이 + (대기 시간)

사람이 3명 초과 6명 이하라면, 
계단이 겹치기 시작하면
이동거리 + 계단길이의 최대값이 
가장 작게끔 계단 위치를 매핑해주고,
만약에, 거기에 4명이상이 배치가 된다고 한다면,
그 계단에 있는 사람들을 다른 계단으로 이동 시킨 코드를 생각해볼 수 있겠는데.

문제는 6명 이상인 경우임
둘 다 초과가 날 수 있어.
그렇다면 어떻게 사람들을 분배할 것인가에 대한 로직을 생각하기가 힘들어짐.

흠,,, 제한시간이 몇 분이지
15초 ? 

50개 테케

최대 10명

최대 대기시간 10분

10명을 2개의 계단으로 분배하는 경우의 수는
2 + 20 + 90 + 240 + 630 + 252 = 1214?

그러면, 각각의 계산 * 1214경우 * 50 테케 
흠, 안 되게따!!!


그렇담시,,

일단 계단에서 가까운 사람부터 매칭해줄까
계단의 입장에서
내가 계단이야.
내 길이에 사람들까지의 거리를 계산해서 더하면
가장 가까운 놈을 찾아

그리고, 불러?

흠,,,

완탐은 안 되니까
계단 입장에서 생각하는 것밖에 답이 없는데.
흠,,


일단 구현할 수 있는 건 구현해
계단 위치 저장하고 사람 위치 저장할까?


'''


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    big = [list(map(int, input().split())) for _ in range(N)]
    # print(big)
    
    # 사람은 좌표값만 저장하고, 계단은 좌표값 + 계단 길이를 함께 저장해야해.
    human_set = set()
    stair_lst = []
    
    # 사람 위치와 stair 위치를 저장해
    for row in range(len(big)):
        for col in range(len(big)):
            if big[row][col] == 1:
                # 사람이다.
                human_set.add((row, col))
            elif big[row][col] != 0:
                stair_lst.append((row, col, big[row][col]))
            
            # 백트래킹 야무지게
            if len(human_set) >= 10 and len(stair_lst)>2 :
                break
        if len(human_set) >= 10 and len(stair_lst)>2 :
            break
    
    # print(big)
    # print(f'#{tc} {len(human_set)} {human_set} {stair_lst}')
    
    # 계단 1번을 기준으로 걸리시는 시간까지 고려하기
    # 행, 열, 시간, 계단1
    human_lst = []
    # 시간 복잡도를 생각해볼 시도를 하는 중
    # 계단 2 * 사람 10명 *  
    for s, stair in enumerate(stair_lst):
        row, col, length = stair
        for h, human in enumerate(human_set):
            r, c = human
            distance = abs(row-r) + abs(col-c)
            human_lst.append((distance + length , h + 1, r, c, distance, s + 1, length)) # 대기 없을때 총 탈출시간. #사람번호 # r, c - 디버깅용 #거리 #계단번호 # 계단 길이 
            
    # print(human_lst)
    from collections import deque
    import heapq
    
    hq = human_lst
    heapq.heapify(hq)
    
    print(hq)
    '''
        t     h     r    c     d     s     l
        토탈  사람              거리  계단   길이
       [(5,   2,    1,    2,    2,    1,    3), 
        (5,   5,    2,    3,    2,    1,    3),
        (6,   6,    0,    2,    3,    1,    3),
        (7,   3,    4,    0,    2,    2,    5), 
        (7,   1,    0,    1,    4,    1,    3),
        (9,   6,    0,    2,    4,    2,    5), 
       (10,   1,    0,    1,    5,    2,    5), 
        (8,   2,    1,    2,    3,    2,    5), 
        (7,   4,    2,    1,    4,    1,    3), 
        (8,   4,    2,    1,    3,    2,    5),
        (8,   5,    2,    3,    3,    2,    5),
       (10,   3,    4,    0,    7,    1,    3)]
    '''
    
    # 탈출 성공한 사람은 없애야지
    human_exit = set()
    stair_1 = []
    stair_2 = []    
    
    while hq:
        t, h, r, c, d, s, l = heapq.heappop(hq)
        if h in human_exit:
            continue
        if s == 1:
            if len(stair_1) < 3:
                heapq.heappush(stair_1, )
                # 졸려서 머리가 안 돌아간다. 일단 자자.
                
            

    
    
            
            
            
        
    