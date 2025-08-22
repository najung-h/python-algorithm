#import sys
#sys.stdin = open('input_b_14891.txt', 'r')






from collections import deque

def rotate(rotate_lst):
    for name, num in enumerate(rotate_lst):
        big_arr[name].rotate(num)




def turn_final(K_lst):
    

    '''

    초기에 회전해야하는 톱니 번호를 확인한다.

    내가 회전했을 때
    내 왼쪽 톱니가 존재하면서, 반대 자석이라면, 회전리스트에 회전 정보를 업데이트한다.
    
    내가 회전했을 대
    내 오른쪽 톱니가 존재하면서, 반대 자석이라면, 회전리스트에 회전 정보를 업데이트한다.

    '''
    
    # 각 회전 지시에 대해서
    
    
    
    for num, dir in K_lst:
        rotate_lst = [0,0,0,0]
        # 1. 첫 번째 톱니를 회전시킨다.
        #print('num, dir : ', num, dir)
        
        idx = num-1# 1번, 2번, 3번을 인덱스로 변환

        rotate_lst[idx] += dir
        
        
        original_num = idx
        original_dir = dir
        
        # 2-1. 그 왼쪽 톱니를 회전시킨다.
        

        if original_num != 0:
            R = True  # rotate 변수 초기화
            
            while True:
                if R is False: 
                    break
                
                if idx - 1 < 0:
                    break
                
                R = False
                
                if big_arr[idx][6] != big_arr[idx-1][2]:
                    idx = idx -1
                    if dir == -1: # 시계 방향
                        rotate_lst[idx] += 1
                        R = True
                        dir = -1*dir

                    elif dir == 1: # 반시계 방향
                        rotate_lst[idx] -= 1
                        dir = -1*dir
                        R = True



        # 2-2. 그 오른쪽 톱니를 회전시킨다.
        idx = original_num
        dir = original_dir

        if original_num != 3:
            R = True
            while idx+1 < 4:
                if R is False: 
                    break

                R = False

                if big_arr[idx][2] != big_arr[idx+1][6]:
                    idx = idx +1

                    if dir == -1: # 시계 방향
                        rotate_lst[idx] += 1
                        R = True
                        dir = -dir

                    elif dir == 1: # 반시계 방향
                        rotate_lst[idx] -= 1
                        dir = -dir
                        R = True
                        
        # 일괄 회전
        for i in range(4):
            if rotate_lst[i] != 0:
                # deque.rotate(k): k>0 시계, k<0 반시계
                big_arr[i].rotate(rotate_lst[i])
    
    return big_arr




def scoring(A,B,C,D):
    '''
    최종 아웃풋으로
    점수를 print하기 위한
    함수입니다.
    
    
    '''
    score = 0
    
    ABCD_SCORE_LST = [1, 2, 4, 8]

    for idx, item in enumerate([A,B,C,D]):
        if item[0] == 1: # 12시 방향이 s극 이라면
            score += ABCD_SCORE_LST[idx]

    '''if A[0] == 1 :
        score += 1
    
    if B[0] == 1:
        score += 2

    if C[0] == 1:
        score += 4
    
    if D[0] == 1:
        score += 8'''

    return score








# ------------- 메인 -----------------




A = deque(list(map(int, input().strip())))
B = deque(list(map(int, input().strip())))
C = deque(list(map(int, input().strip())))
D = deque(list(map(int, input().strip())))
big_arr = [A,B,C,D]
#print(big_arr)


K = int(input().strip()) # 회전 횟수
K_lst = [tuple(map(int, input().split())) for _ in range(K)]





big_arr = turn_final(K_lst)
#print(big_arr)
print(scoring(A,B,C,D))

#print(A, B, C, D)


'''gpt의 코드리뷰
1) 회전의 지시에 대해 나타내는 K_lst는 변경될 일이 없으니, tuple로 받는 것이 효율적

2) 매직 넘버 상수화: LEFT_TOOTH, RIGHT_TOOTH = 6, 2 등으로 의미 드러내기

'''



