#import sys
#sys.stdin = open('input_b_14891.txt', 'r')




from collections import deque


# 맞닿는 위치 인덱스 # GPT의 조언
RIGHT_TOOTH = 2
LEFT_TOOTH  = 6


def turn_left(idx, direction, rotate_lst):
    """기준 톱니(idx)가 direction으로 돌 때, 왼쪽으로 전파될 회전을 rotate_lst에 기록"""
    jdx = idx
    dirr = direction

    while jdx > 0:
        
        if big_arr[jdx][LEFT_TOOTH] == big_arr[jdx-1][RIGHT_TOOTH]: break
        else:          # 내 왼쪽과 왼쪽 톱니의 오른쪽이 같지 않다면 회전한다.
            jdx = jdx -1  # 자, 왼쪽 톱니에 대해서

            dirr = -dirr   # 반대 방향으로 회전할거야 
            rotate_lst[jdx] = dirr   # 반대 방향으로 회전한다는 것을 저장시켜


def turn_right(idx, direction, rotate_lst):

    jdx = idx
    dirr = direction

    while jdx < 3:  # 더 이상 오른쪽에 머가 없으면 break

        if big_arr[jdx][RIGHT_TOOTH] == big_arr[jdx+1][LEFT_TOOTH]:  break
        else: # 내 오른쪽과 오른쪽 톱니의 왼쪽이 같지 않다면 회전한다.
            jdx = jdx +1  # 오른쪽 톱니로 나아가자

            dirr = -dirr   # 반대 방향으로 회전할거야 
            rotate_lst[jdx] = dirr   # 반대 방향으로 회전한다는 것을 저장시켜
                


def turn_final(K_tu):
    
    '''
    초기에 회전해야하는 톱니 번호를 확인한다.

    각각의 톱니가 회전했을 때
    내 왼쪽 톱니가 존재하면서, 반대 자석이라면, 회전리스트에 회전 정보를 업데이트한다.
    
    각각의 톱니가 회전했을 때
    내 오른쪽 톱니가 존재하면서, 반대 자석이라면, 회전리스트에 회전 정보를 업데이트한다.

    한 번 다 회전 정보 리스트가 완성되었다면
    한번에 싹 돌린다.
    '''
    
    # 각 회전 지시에 대해서
    for num, direction in K_tu:

        # 이번 회전 지시에서 회전할 톱니의 정보를 저장할 리스트
        rotate_lst = [0,0,0,0]
      
         # 1번, 2번, 3번, ... 톱니 정보를 인덱스로 변환
        idx = num-1  

        # ---- 1. 첫 번째 톱니는 무조건 회전한다. ---- #
        rotate_lst[idx] = direction
        
        # 2-1. 그 왼쪽 톱니를 몇 개 회전시켜야할까  # 함수화
        turn_left(idx, direction, rotate_lst)

        # 2-2. 그 오른쪽 톱니를 몇 개 회전시켜야할까 rotate_lst에 받아와.
        turn_right(idx, direction, rotate_lst)

                        
        # 일괄 회전
        for i in range(4):
            if rotate_lst[i] != 0:
                # deque.rotate(k): k>0 시계, k<0 반시계
                big_arr[i].rotate(rotate_lst[i])

    
    return big_arr



def scoring(big_arr):
    '''     최종 점수를 출력하기 위한 함수입니다.        '''
    score = 0
    A,B,C,D = big_arr
    ABCD_SCORE_LST = [1, 2, 4, 8]

    for idx, item in enumerate([A,B,C,D]):
        if item[0] == 1: # 12시 방향이 s극 이라면
            score += ABCD_SCORE_LST[idx]

    return score





# ------------- 메인 -----------------


# 각 톱니의 정보를 받아와서, 리스트로 저장합니다.
A = deque(list(map(int, input().strip())))
B = deque(list(map(int, input().strip())))
C = deque(list(map(int, input().strip())))
D = deque(list(map(int, input().strip())))
big_arr = [A,B,C,D]


# 회전하는 횟수와 각 회전 지시 정보를 받아와서 int / tuple로 저장합니다.
# tuple로 저장하는 이유 : 회전 지시 정보는 바뀔 일이 없이, 참조만 하기 때문에!
K = int(input().strip()) # 회전 횟수
K_tu = [tuple(map(int, input().split())) for _ in range(K)]


# 회전을 다 시킨 정보를 받아옵니다.
big_arr = turn_final(K_tu)

# 점수를 매겨서 출력합니다.
print(scoring(big_arr))


'''gpt의 코드리뷰
1) 회전의 지시에 대해 나타내는 K_lst는 변경될 일이 없으니, tuple로 받는 것이 효율적

2) 매직 넘버 상수화: LEFT_TOOTH, RIGHT_TOOTH = 6, 2 등으로 의미 드러내기

3) dir 대신 direction 같은 이름을 권장(파이썬 내장 dir()과 충돌 피하기).

'''



