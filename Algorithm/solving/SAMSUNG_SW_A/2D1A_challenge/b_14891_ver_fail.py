import sys
sys.stdin = open('input_b_14891.txt', 'r')






from collections import deque





def num_to_lst(num):
        # 우선 1번 2 번 이런 톱니 번호를
    # A, B, C 이런 식으로 바꿀게요
    if num == 1:
        lst = A
    elif num == 2:
        lst = B
    elif num ==3:
        lst = C
    else:
        lst = D
    return lst




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
        lst = num_to_lst(num)

        if dir == 1: # 시계 방향
            lst.rotate(1)
            pass
        elif dir == -1: # 반시계 방향
            lst.rotate(-1)

        rotate_lst = [0,0,0,0]
        
        # 2-1. 그 왼쪽 톱니를 회전시킨다.
        original_num = num
        original_dir = dir

        if original_num != 1:
            R = True
            while num-1 > 0:
                if R is False: 
                    break
                R = False
                num = num -1
                if lst[6] != num_to_lst(num)[2]:
                    lst = num_to_lst(num)

                    if -1 * dir == 1: # 시계 방향
                        lst.rotate(1)
                        R = True
                        pass

                    elif -1 * dir == -1: # 반시계 방향
                        lst.rotate(-1)
                        R = True

        # 2-2. 그 오른쪽 톱니를 회전시킨다.
        num = original_num
        dir = original_dir

        if original_num != 4:
            R = True
            while num+1 <= 4:
                if R is False: 
                    break

                R = False
                num = num +1
                if lst[2] != num_to_lst(num)[6]:
                    lst = num_to_lst(num)

                    if -1 * dir == 1: # 시계 방향
                        dir = -1 * dir
                        lst.rotate(1)
                        R = True
                        pass

                    elif -1 * dir == -1: # 반시계 방향
                        dir = -1 * dir
                        lst.rotate(-1)
                        R = True





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

    turn_final(K_lst)


    print(scoring(A,B,C,D))

    print(A, B, C, D)




