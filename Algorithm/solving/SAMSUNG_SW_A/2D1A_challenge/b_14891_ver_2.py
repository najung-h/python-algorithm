import sys
sys.stdin = open('input_b_14891.txt', 'r')






from collections import deque

def rotate(rotate_lst):
    for name, num in enumerate(rotate_lst):
        big_arr[name].rotate(num)


rotate_lst = [0,0,0,0]

def turn_final(K_lst):
    

    '''

    초기에 회전해야하는 톱니 번호를 확인한다.

    내가 회전했을 때
    내 왼쪽 톱니가 존재하면서, 회전하지 않았다면
    회전시킨다.
    
    내가 회전했을 대
    내 오른쪽 톱니가 존재하면서 회전하지 않았다면
    회전시킨다.

    '''
    
    # 각 회전 지시에 대해서
    
    
    for num, dir in K_lst:
        # 1. 첫 번째 톱니를 회전시킨다.
        num = num-1# 1번, 2번, 3번을 인덱스로 변환

        rotate_lst[num] += dir
        
        
        # 2-1. 그 왼쪽 톱니를 회전시킨다.
        original_num = num
        original_dir = dir

        if original_num != 1:
            R = True
            while num-1 >= 0:
                if R is False: 
                    break

                R = False
                
                if big_arr[num][6] != big_arr[num-1][2]:
                    num = num -1
                    if dir == -1: # 시계 방향
                        rotate_lst[num] += 1
                        R = True
                        dir = -1*dir

                    elif dir == 1: # 반시계 방향
                        rotate_lst[num] -= 1
                        dir = -1*dir
                        R = True

        # 2-2. 그 오른쪽 톱니를 회전시킨다.
        num = original_num
        dir = original_dir

        if original_num != 4:
            R = True
            while num+1 < 4:
                if R is False: 
                    break

                R = False

                if big_arr[num][2] != big_arr[num+1][6]:
                    num = num +1

                    if dir == -1: # 시계 방향
                        rotate_lst[num] += 1
                        R = True
                        dir = -1*dir

                    elif dir == 1: # 반시계 방향
                        rotate_lst[num] -= 1
                        dir = -1*dir
                        R = True
    return rotate_lst




def scoring(A,B,C,D):
    '''
    최종 아웃풋으로
    점수를 print하기 위한
    함수입니다.
    
        
    '''
    score = 0

    if A[0] == 1 :
        score += 1
    
    if B[0] == 1:
        score += 2

    if C[0] == 1:
        score += 4
    
    if D[0] == 1:
        score += 8

    return score











T = int(input())

for tc in range(1, T+1):


    A = deque(list(map(int, input())))
    B = deque(list(map(int, input())))
    C = deque(list(map(int, input())))
    D = deque(list(map(int, input())))

    K = int(input()) # 회전 횟수
    K_lst = []
    for _ in range(K):
        K_lst.append(list(map(int, input().split())))

    big_arr = [A,B,C,D]





    rotate_lst = turn_final(K_lst)

    rotate(rotate_lst)

    print(scoring(A,B,C,D))

    #print(A, B, C, D)




