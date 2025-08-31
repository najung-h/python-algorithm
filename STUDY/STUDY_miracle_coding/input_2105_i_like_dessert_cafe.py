
def go_the_direction(rdx, cdx, d, steps, dessert_set, start_r, start_c, N, big_arr):    
    #'''한 변 내 이동'''
    
    rr, cc = rdx, cdx
    
    for s in range(steps):
        # 그 방향으로 계속 가는데,
        rr += dr[d]
        cc += dc[d] 
        
        # 규격 밖이면 실패
        if not (0 <= rr < N and 0 <= cc < N):
            return False
    
        # 다 걷기 전에 끝나면 실패
        if rr == start_r and cc == start_c:
            return False
        
        # 디저트 먹은거니
        dessert = big_arr[rr][cc]
        
            #먹었다면
        if dessert in dessert_set:
            return False
            # 안 먹었다면
        dessert_set.add(dessert)
    



dr =(1,  1, -1,   -1 )
dc =(1, -1,  -1,   1)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    big_arr = [list(map(int, input().split()))  for _ in range(N)] 
    dessert_set = set()
    max=0
    for rdx in range(N):
        for cdx in range(N):
            desser_set = set()
            dessert = big_arr[rdx][cdx]
            for d in range(4):

                r = rdx + dr[d]
                c = cdx + dc[d]
                
                if r<0 or r >= N or c <0 or c>=N:
                     continue
                if big_arr[r][c] in dessert_set:
                     continue
                dessert = big_arr[r][c] 
                dessert_set.add(dessert)
                go_the_direction(r,c,d)
            if len(dessert_set) >= max:
                max = dessert_set 

 

    print(f'#{tc} {max}')