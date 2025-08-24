'''완전탐색으로 구현했습니다. -> 런타임 에러 발생'''

import sys
sys.stdin = open("input_6485.txt", "r")


T = int(input())
for test_case in range(1, T + 1):

    N = int(input())
    ab_lst = [tuple(map(int, input().split())) for _ in range(N)]
    P = int(input())
    C_tu = tuple(int(input()) for _ in range(P))
    
    ''' 
    <input>
    
    N(버스 노선의 개수) : 2
    ab_lst(i번째 버스 정보, a이상 b이하의 모든 정류장만을 다님) :  [(1, 3), (2, 5)]
    C_tu(P개의 버스 정류장에 대해 몇 개의 버스 노선이 다니는지?) :  (1, 2, 3, 4, 5)
    
    <output>
    print(f'#{test_case} ''.join(map(str, *bus_lst'))
    '''
    cnt = 0
    bus_lst = [0] * P
    
    for ab in ab_lst:
        adx = ab[0] -1
        bdx = ab[1] -1
        
        for i in range(adx, bdx+1):
            bus_lst[i] += 1
    
    print(f'#{test_case} {" ".join(map(str, [bus_lst[C-1] for C in C_tu]))}')