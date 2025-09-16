import sys
sys.stdin = open('input_1249.txt', 'r')

# dfs 사용하겠습니다.
from collections import deque

# 방향은 하단 아니면, 우측으로 이동하기로,,
# 안되네^^ 다 해봐야겠다 ^^
# 그대신 다 탐색하면 시간 초과날 것 같으니까
# 2차원 dp느낌으로 풀어볼게요
# 그 칸까지 가는데 최소 경로를 찾아놔야겠어

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)



def dfs(r,c,gongsa):
    global min_cnt
    
    stack = deque()
    stack.append((r, c, gongsa))
    
    
    while stack:
        rr, cc, ggongsa = stack.pop()
        
        # 도착했는지 확인
        if (rr, cc) == (N-1, N-1):
            min_cnt = min(ggongsa, min_cnt)
            continue
        
        # 도착하지 않았다면,
        # 아이디어1: 어차피 아래쪽이랑오른쪽만 탐색하니까
        # 왔던 곳을 돌아가는 경우는 없다.
        # 탐색에서 제외하자.
        
        r1 = rr + dr[0]
        c1 = cc + dc[0]
            
        r2 = rr + dr[1]
        c2 = cc + dc[1]
        
        # 아이ㅣ어 2: stack에서 dfs를 할  건데,
        # 그나마 작은 애를 미리 찾아서 min_cnt로 지정해야지
        # 탐색횟수를 줄일 수 있을 것이다.
        # 그래서, 오른쪽과 아래쪽을 비교해서,
        # 큰 애들부터 먼저 stack에 담아야겠다.
        #== 작은 애 우선 탐색
        
        # 규격 내인지도 확인
        if 0<= r1 < N and 0<= c1 < N:
            if 0<= r2 < N and 0<=  c2 < N:
                if big_arr[r1][c1] <= big_arr[r2][c2]:
                    #  백트래킹 확인하고 넣기.
                    if ggongsa +  big_arr[r2][c2] <= min_cnt:
                        stack.append((r2, c2,  ggongsa + big_arr[r2][c2]))
                    if ggongsa + big_arr[r1][c1] <= min_cnt:
                        stack.append((r1, c1, ggongsa +  big_arr[r1][c1]))
            
            else: # r1만 가능한 경우
                if ggongsa + big_arr[r1][c1] <= min_cnt:
                    stack.append((r1, c1, ggongsa +  big_arr[r1][c1]))
        
        else:
            if 0<= r2 < N and 0<=  c2 < N: # r2만 가능한 경우.
                if ggongsa +  big_arr[r2][c2] <= min_cnt:
                    stack.append((r2, c2,  ggongsa + big_arr[r2][c2]))
                
                
                
                
        
        
            
            
        
    
    
    


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    big_arr = [list(map(int,input())) for _ in range(N)]
    
    min_cnt = float('inf')    
    dfs(0, 0, 0)
    
    print(f'#{tc} {min_cnt}')