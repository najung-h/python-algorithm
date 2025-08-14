import sys
sys.stdin = open('input_9490.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    N, M = list(map(int, input().split()))
    big_arr = [list(map(int, input().split())) for _ in range(N)]

    # 델타 접근 법 사용
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    max_ballon = 0

    # 행 방향으로 순회하겠습니다.
    for rdx in range(N):
        for cdx in range(M):
            # 그 풍선에 종이 꽃가루 몇 개 들었니 => 상하좌우 몇 개씩 더 터뜨려볼까
            how_much_ballon_to_kill = big_arr[rdx][cdx]
            
            #print('나는 지금 ', rdx, cdx,'에 있고, 추가로', how_much_ballon_to_kill, '개 터뜨려')
            # 초기화
            ballon = how_much_ballon_to_kill

            for d in range(4):
                for k in range(1,how_much_ballon_to_kill+1):
                    r = rdx + dr[d] * k
                    c = cdx + dc[d] * k
                    

                    if 0<= r < N and 0<=c<M: # 범위 내 값이라면
                        #print('추가로 터뜨려', r,c)
                        ballon += big_arr[r][c]
                    else:
                        # 이 방향은 더 이상 진행 불가.
                        break

            if ballon > max_ballon:
                max_ballon = ballon

    print(f"#{test_case} {max_ballon}")


