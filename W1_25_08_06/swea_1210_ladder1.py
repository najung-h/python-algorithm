# 사다리

################### 


# (상) 하 좌 우
# 중에서, 우 좌 상 순으로 탐색
#   (m,n+1)
#   (m,n-1)
#   (m-1,n)


#하, 좌, 우 중에서,
# 1. 범위 안에 있는 값이냐
# 2. 그 값이 1이냐. 를 확인
err = False
arr = False

def can_go_right_or_left(now_point):
    m = now_point[0]
    n = now_point[1]
    can_go_lst = []


    for _ in range(3):
        can_go_lst.append((m,n+1))  # 우
        can_go_lst.append((m,n-1))  # 좌
        can_go_lst.append((m-1,n))  # 상

    can_go = 0    
    for a,b in can_go_lst:
        
        if a in range(100) and b in range(100): # 범위 안
            if big_arr[a][b] == 2:   # 도착지? 
                arr = True
                print('arrived')
            
            elif big_arr[a][b] ==1 and (a,b) not in went_lst:
                now_point = (a,b)
                return now_point
    if can_go == 0:
        err = True
        print('error')

    print(went_lst)





##########################

import sys
sys.stdin = open("input_1210.txt", "r")

T = 10

for test_case in range(1, T + 1):
    tc = int(input())
    big_arr =  [list(map(int, input().split())) for _ in range(100)]




    #print(can_go_right_or_left(0,0))

    for idx, i in enumerate(big_arr[-1]):
        if i == 2:
            now_point = (99, idx)

    #print(now_point)
    trying = 0
    went_lst = []


    while err == False and arr == False:
        trying += 1
        if trying >1000:
            break
        elif now_point[0] == 0: # 도착
            print(f'#{test_case} {now_point[1]}')
            break
        else:
            now_point = can_go_right_or_left(now_point)
            went_lst.append(now_point)
            #print(now_point)
