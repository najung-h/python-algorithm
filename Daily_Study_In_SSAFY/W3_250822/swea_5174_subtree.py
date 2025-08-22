import sys
sys.stdin = open('input_5174.txt', 'r')


def node_cnt(N):
    cnt = 0

    if node != 0: # 유효한 노드라면

    if left_kid_lst[N] == 0 and right_kid_lst[N] == 0 : 
        return cnt

    elif left_kid_lst[N] == 0:
        N = node_cnt(N)
            
    else:
        N = node_cnt(N)

    node_cnt += 1   





T = int(input())

for tc in range(1, T+1):
        
    E, N = list(map(int, input().split()))

    edge = list(map(int, input().split()))


    left_kid_lst = [0] * (E+2) 
    right_kid_lst = [0] * (E+2)

    for k in range((E+1)//2+2):
        parent, kid = edge[2*k], edge[2*k+1]

        # 왼쪽 자식이 비었다면, 너는 왼쪽에 들어갈거야
        if left_kid_lst[parent] == 0:  # 부모 노드
            left_kid_lst[parent] = kid

        # 아니라면, 너는 오른쪽으로 가자.
        else:
            right_kid_lst[parent] = kid

    print(f'왼쪽 자식 리스트 {left_kid_lst}')
    print(f'오른쪽 자식 리스트 {right_kid_lst}')

    # 이제, 트리에 대해서, N 아래있는 애들을 탐색한다.
    node_cnt = 0

    '''while True:
        print(f'{N}번 노드')'''

    cnt = node_cnt(N)

    print(f'#{tc} {cnt}')