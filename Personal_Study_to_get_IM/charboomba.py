import sys
sys.stdin = open('input_charboomba.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    N,M = list(map(int, input().split()))
    power_of_bomb = [list(map(int, input().strip().split())) for _ in range(N)]

    # 델타 접근법을 사용하겠습니다.
    dr = [-1, 1, 0, 0]  # 상하좌우
    dc = [0, 0, -1, 1] 

    max_bomb = 0

    for rdx in range(N):
        for cdx in range(M):
            # 각 원소에 대해서 
            # 터지는 폭탄값은
            now_bomb = power_of_bomb[rdx][cdx]
            #print(f'{rdx},{cdx}를 터뜨려볼게요. 여기는 power가 {now_bomb}이네용')

            for d in range(4): # 각 방향에 대해서
                for k in range(1, power_of_bomb[rdx][cdx]+1): # 각 power에 대해서

                    r = rdx + dr[d] * k
                    c = cdx + dc[d] * k

                    if 0<=r<N and 0<=c<M:  # 범위 내라면
                        now_bomb += power_of_bomb[r][c]
                        #print(f'{r},{c}에서 {power_of_bomb[r][c]}개 터트렸다!!!')
                    
                    else: # 범위 밖이라면
                        break # 그 방향으로는 더 이상 뻗어나가지 말자
            
            #print(f'터뜨려보니 총 {now_bomb}개가 터졌어요!')
            if now_bomb > max_bomb:
                max_bomb = now_bomb


    print(f'#{test_case} {max_bomb}')
