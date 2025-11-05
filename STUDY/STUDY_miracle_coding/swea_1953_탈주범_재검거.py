import sys
sys.stdin = open("input_1953.txt", "r")

from collections import deque

'''# 상 하 좌 우
dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)'''

# 이걸 나중에 방향을 뚫려있는지 확인을 해야하니까. 서로 반대되게 매핑을 해야겠다.
# 상 좌 하 우 순서로
dr = (-1, 0, 1, 0)
dc = (0, -1, 0, 1)


def in_range(r, c, N, M):
    return 0 <= r < N and 0 <= c < M

#방향과 dr, dc 순서를 매핑하자.
tunnel_type_dic = {
    0 : [],
    1 : [0, 2, 1, 3],
    2 : [0, 2],
    3 : [1, 3],
    4 : [0, 3],
    5 : [2, 3],
    6 : [2, 1],
    7 : [0, 1],
}

T = int(input())
for test_case in range(1, T+1):
    # 지도가 N 행 M 열
    # 맨홀 뚜껑 위치는 (R, C)
    # 탈출 후 소요된 시간 L
    N, M, R, C, L = list(map(int, input().split()))
    big_arr = [list(map(int, input().split())) for _ in range(N)]
    
    # 숫자 1-7은 해당 위치의 터널 구조물 타입,
    # 숫자 0은 터널이 없는 장소
    
    q = deque()
    visited = set()
    
    D = big_arr[R][C] # 출발 타입
    # 시작 칸이 0이면 바로 0
    if D == 0 or L == 0:
        print(f'#{test_case} 0')
        continue
    
    START_POINT = (R,C,0,D)  # 출발 좌표, 경과 시간, 출발 타입
    '''bfs라 경과 시간을 체크안 하고도 잘 할 수 있을 것 같은데. 음. 잘 기억이 안 나니까 패스하자. 그대신 경과 시간 지나면 그 뒤에있는 애들은 popleft조차 안 해서 나름으 ㅣ백 트래킹!'''
    q.append(START_POINT)
    visited.add((R,C))
    
    
    
    while q:
        nr, nc, nt, nd = q.popleft()  # 좌표, 시간, 직전 방향까지
        
        # 나갈 수 있는 방향
        cur_type = big_arr[nr][nc]
        
         # 해당 방향에 대해 순회
        for d in tunnel_type_dic[cur_type]:
            nnr = nr + dr[d]
            nnc = nc + dc[d]
            nnd = d  # 다음으로 간 방향을 기록

        # 규격 이내라면
            if not in_range(nnr, nnc, N, M):
                continue
            # 시간 경과 체크
            if nt +1 >= L:
                continue
            # 빈 칸 혹은 이미 방문이면 패스
            if big_arr[nnr][nnc] == 0 or (nnr, nnc) in visited:
                continue
            
            # 넘어갈 수 있다면 == 옆에 칸이 반대 방향으로 열려 있는지 확인
            # 현재 방향 d의 반대는 (d+2)%4
            opp = (d + 2) % 4
            nxt_type = big_arr[nnr][nnc]
            dir_lst = tunnel_type_dic.get(nxt_type)
            
            # 이웃 칸이 반대 방향 허용하면 이동 가능
            if opp in dir_lst:
                visited.add((nnr, nnc))
                q.append((nnr, nnc, nt + 1, nnd))

    ans = len(visited)
    #print(visited)

    print(f'#{test_case} {ans}')