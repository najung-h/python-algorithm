import sys
sys.stdin = open('input_1949.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    N, K = list(map(int, input().split()))
    map_lst = [list(map(int, input().split())) for _ in range(N)]

    ''' 
    < 문제 조건>

    최대로 긴 등산로 만들기
    각 숫자는 지형의 높이 (1<= 지형의 높이 <=20)

    등산로는
    1. 가장 높은 봉우리에서 시작
    높이가 같으면 안 되고, 가로나 세로로 연결되어야

    strictly decreasing fcn
    
    단, 가장 높은 봉우리가 여러 개 있을 수 있다. (최대 5개)

    최대 K층만큼 깎아서 길을 연결할 수 있다.
    '''

    ''' 
    접근 방안
    1. 가장 높은 곳들을 찾아서 리스트로 저장한다.
    for start_point in highest_lst:
        델타 접근법을 활용해서 상하좌우 값 확인
        그 중 가장 높은 곳으로 일단 간다. * 반복

        못 가게 되면 (k가 남아있는 한) k를 소모해서 한 번 깎는다
 
    2. 예외 케이스가 없길 기도한다.
    '''


    # 1. find the highest 
    highest = 0
    highest_place_lst = []

    for rdx in range(N):
        for cdx in range(N):
            if map_lst[rdx][cdx] > highest:
                highest = map_lst[rdx][cdx]
                highest_place_lst = [] 
                highest_place_lst.append((rdx, cdx))
            elif map_lst[rdx][cdx] ==highest:
                highest_place_lst.append((rdx,cdx))
    
    # print(f'제가 싹 보니 {highest}짜리가 가장 높은데요. 그게 어디냐면... {highest_place_lst}여기에요')
    # 제가 싹 보니 9짜리가 가장 높은데요. 그게 어디냐면... [(0, 0), (2, 3), (2, 4)]여기에요


    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    moving_lst = []

    for start_point in highest_place_lst:
        stack = []
        now_height = highest
        #print(now_height)
        now_point_r = start_point[0]
        now_point_c = start_point[1]
        moving = 0

        #print(f'{start_point}에서 시작해볼까요? 현재 높이는 {highest}이고요')

        while True:
            
            #print(f'자 여기는 {now_point_r}, {now_point_c}에요!')
            # 각 방향의 높이를 조사합니다.
            height_lst = []  # 높이 담겨있음
            can_go_lst = []  # 좌표 담겨있음

            really_can_go_lst = []
            for d in range(4):
                r = now_point_r + dr[d]
                c = now_point_c + dc[d]

                if 0<= r<N and 0<= c <N:
                    h = map_lst[r][c]
                    ##print(f'{r},{c}의 높이는 {h}인데요?')

                    ##print(h, now_height)
                    if h < now_height : # 이전 높이보다는 낮다면
                        height_lst.append(h)
                        can_go_lst.append((r,c))

            if len(height_lst) != 0:
                max_height = max(height_lst)
            else:
                #print('탐색 끝이에요')
                #print(f'총 {moving}번 움직였어요')
                break

            for hdx in range(len(height_lst)):
                if height_lst[hdx] == max_height:
                    really_can_go_lst.append(can_go_lst[hdx])



            can_go_lst = really_can_go_lst
            #print(f'갈 수 있는 곳 중에서 가장 높은 곳은 {can_go_lst} 여긴데요, {max_height}층이에요')

            if len(can_go_lst) == 1: # 갈 곳이 하나라면 # 아이고 좋아 가자
                now_height = max_height
                now_point_r = can_go_lst[0][0]
                now_point_c = can_go_lst[0][1]
                moving += 1
                #print(f'{now_point_r}, {now_point_c}로 가볼게요! 지금까지 총 {moving}번 움직였어요!')


            elif len(can_go_lst) < 1: 
                # 갈 곳이 없자낭
                ##moving_lst.append(moving)
                #print(f'지금 내 높이보다 더 낮은 곳이 없어요ㅠ,ㅠ' )
                #print('탐색 끝이에요')
                #print(f'총 {moving}번 움직였어요')
                
                break
            

            else: 
                #print('기도가 먹히지 않았어요. 두 갈래 길이잖아요')    

                #################### 두 갈래 길이라면
                for can_go_point in can_go_lst:

                    now_height = max_height
                    now_point_r = can_go_point[0]
                    now_point_c = can_go_point[1]



                    while True:
                
                        #print(f'자 여기는 {now_point_r}, {now_point_c}에요!')
                        # 각 방향의 높이를 조사합니다.
                        height_lst = []  # 높이 담겨있음
                        can_go_lst = []  # 좌표 담겨있음

                        really_can_go_lst = []
                        for d in range(4):
                            r = now_point_r + dr[d]
                            c = now_point_c + dc[d]

                            if 0<= r<N and 0<= c <N:
                                h = map_lst[r][c]
                                ##print(f'{r},{c}의 높이는 {h}인데요?')

                                ##print(h, now_height)
                                if h < now_height : # 이전 높이보다는 낮다면
                                    height_lst.append(h)
                                    can_go_lst.append((r,c))

                        if len(height_lst) != 0:
                            max_height = max(height_lst)
                        else:
                            #print('탐색 끝이에요')
                            #print(f'총 {moving}번 움직였어요')
                            break

                        for hdx in range(len(height_lst)):
                            if height_lst[hdx] == max_height:
                                really_can_go_lst.append(can_go_lst[hdx])



                        can_go_lst = really_can_go_lst
                        #print(f'갈 수 있는 곳 중에서 가장 높은 곳은 {can_go_lst} 여긴데요, {max_height}층이에요')

                        if len(can_go_lst) == 1: # 갈 곳이 하나라면 # 아이고 좋아 가자
                            now_height = max_height
                            now_point_r = can_go_lst[0][0]
                            now_point_c = can_go_lst[0][1]
                            moving += 1
                            #print(f'{now_point_r}, {now_point_c}로 가볼게요! 지금까지 총 {moving}번 움직였어요!')


                        elif len(can_go_lst) < 1: 
                            # 갈 곳이 없자낭
                            #moving_lst.append(moving)
                            #print(f'지금 내 높이보다 더 낮은 곳이 없어요ㅠ,ㅠ' )
                            break
                        
                        elif len(can_go_lst) == 0:
                            #print('탐색 끝이에요')
                            #moving_lst.append(moving)
                            #print(f'총 {moving}번 움직였어요')
                            break

            
        #print(f'자,,, 싹 돌아보니까 이 출발점에서는 총 {moving}번 움직이네요')
        moving_lst.append(moving)
        ##print(moving_lst)
    
    if moving_lst :
        #print(f'시작지점에서 한번씩 출발을 해보니까, 가장 많이 움직인 길이는 {max(moving_lst)}만큼이에요!')
        print(f"#{test_case} {max(moving_lst)}")


