
import sys
sys.stdin = open("input_2001.txt", "r")


def how_many_flies(now_point):
    a = now_point[0]
    b = now_point[1]

    can_kill_lst = []
    can_kill_num = 0

    for m in range(0, N):
        for n in range(0, N):
            if 0<= a+m < M and 0 <= b+n < M:
                can_kill_lst.append((a+m, b+n))
    
    for tu in can_kill_lst:
        can_kill_num += big_arr[tu[0]][tu[1]]
    
    #print(can_kill_num)

    return(can_kill_num)
    #for n in range(1, N+1):


T = int(input())
T = 2
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    M, N = list(map(int, input().split()))
    # M 배열 크기,   5<= M <= 15
    # N 파리채 크기,   2<N<M

    # 파리 개수는 30개 이하

    big_arr = [list(map(int, input().split())) for _ in range(M)]

    #print(big_arr)

    flies_num_lst = []

    for i in range(M-N):
        for j in range(M-N):
            now_point = (i,j)
            flies_num_lst.append(how_many_flies(now_point))

    print(f'#{test_case} {max(flies_num_lst)}')
        


    

    