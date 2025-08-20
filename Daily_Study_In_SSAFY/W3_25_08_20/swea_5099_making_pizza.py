from collections import deque

import sys
sys.stdin = open('input_5097.txt', 'r')


T = int(input())

for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    arr = list(map(int, input().split()))

    new_arr = [[0,0] for _ in range(N)]

    for idx, i in enumerate(arr):
        new_arr[idx][0] = idx
        new_arr[idx][1] = i

    # print(new_arr) # [[0, 5527], [1, 731], [2, 31274]]

    que = deque(new_arr[:N])


    while True:
        if len(que) == 1:
            print(now_pizza[0])
            break

        new_pizza_cnt = 0

        

        now_pizza = que.popleft()
        now_pizza = [now_pizza[0], now_pizza[1] //2]

        if now_pizza[1] ==1:
            # 피자가 녹았어
            # 이제 (가능하다면) 다음 피자 넣고 
            if new_pizza_cnt < N-M:
                que.append(new_arr[N+new_pizza_cnt])
                new_pizza_cnt += 1

            # 한 번 돌려야해
            que.rotate(-1)
        
        else:
            # 아직 피자가 덜 녹았어. 
            # 다시 넣고
            que.append(now_pizza)
            # 한 바퀴 더 돌려야해
            que.rotate(-1)


        


    