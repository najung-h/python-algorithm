import sys
sys.stdin = open('input_5643.txt', 'r')

'''노드 각각에서 출발했을 때, 
모든 노드를 탐색할 수 있으면 됨
굳이 무향 / 유향 노드를 구분할 필요도 없음

아니네, 구분해야하네 ㅎㅎ
'''

from collections import deque

def dfs(start_node, path):
    stack = deque()
    path_all = []  # 어디어디랑 키 비교가 가능한지 알 수 있어야 하니까. 전체 리스트 
    # 나 보다 큰 애 누구?

    # 첫 번째 노드 방문 처리 후 스택에 삽입
    path.append(start_node)
    stack.append((start_node, path))
    path_all.append(start_node)

    while stack:
        current_node, current_path = stack.pop()
        # print('스택에서 노드를 꺼내봅시다 : ', current_node, current_path)

        
        for new_node in node_info_lst[current_node]:
            if new_node not in current_path:
                if len(current_path) == N-1: # 모두 방문할 수 있다면
                    return current_path
                stack.append((new_node, current_path + [new_node]))
                # print('다시 넣을게요 : ', new_node, current_path + [new_node])
                path_all.append(new_node)

    return path_all

def dfs2(start_node, path):
    '''위 함수랑 똑같고, 참조하는 애만 변경
    node_info_lst => node_info_lst_reverse'''
    stack = deque()
    path_all = []  # 어디어디랑 키 비교가 가능한지 알 수 있어야 하니까. 전체 리스트 
    # 나 보다 큰 애 누구?

    # 첫 번째 노드 방문 처리 후 스택에 삽입
    path.append(start_node)
    stack.append((start_node, path))
    path_all.append(start_node)

    while stack:
        current_node, current_path = stack.pop()
        # print('스택에서 노드를 꺼내봅시다 : ', current_node, current_path)

        
        for new_node in node_info_lst_reverse[current_node]:
            if new_node not in current_path:
                if len(current_path) == N-1: # 모두 방문할 수 있다면
                    return current_path
                stack.append((new_node, current_path + [new_node]))
                # print('다시 넣을게요 : ', new_node, current_path + [new_node])
                path_all.append(new_node)

    return path_all





T = int(input())
for tc in range(1, T+1):
    N = int(input())   # 노드의 개수
    M = int(input())  # 간선의 개수

    # 입력 받으면서 바로 노드 정보 채우기
    node_info_lst = [[] for _ in range(N+1)]
    node_info_lst_reverse = [[] for _ in range(N+1)]

    for _ in range(M):
        a, b = list(map(int, input().split()))
        node_info_lst[a].append(b) # 작은 친구에서 큰 친구로 이어지게끔 설정.
        node_info_lst_reverse[b].append(a)  # 큰 친구에서 작은 친구로 이어지게끔 설정.

    # print(node_info_lst)  
    # print(node_info_lst_reverse)

    # [[], [5], [], [4], [2, 6], [4, 2], []]
    # [[], [], [4, 5], [], [3, 5], [1], [4]]

    result_cnt = 0

    for n in range(1, N+1):
        if len(set(dfs(n, [])).union(set(dfs2(n, [])))) == N:  #start_node가 중복으로 되어있으니까 등호 허용 x
            result_cnt += 1
    

    print(f'#{tc} {result_cnt}')