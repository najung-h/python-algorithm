import sys

sys.stdin = open('input.txt')


def DFS_stack_pop_style(start):
    '''
    스택을 활용한 DFS (Pop 시점 방문 처리)
    '''

    visited = [False] * (V + 1)
    # 방문할 노드를 저장할 스택 (시작 노드 삽입)
    stack = [start]
    result_path = []
    
    # 탐색 시작(스택이 빌 때까지)
    while stack:
        # 1. 스택에서 정점을 pop
        current_node = stack.pop()

        # 2. [핵심] 스택에서 꺼낸 후, 방문 했었는지를 확인
        if not visited(current_node):
            # 3. 방문 처리 및 경로 추가
            visited[current_node] = True
            result_path.append(current_node)


# --- 그래프 구성 ---
V, E = map(int, input().split())
data = list(map(int, input().split()))

# 인접행렬(Adjacency Matrix) 생성
adj_matrix = [[0] * (V + 1) for _ in range(V + 1)]

# 간선 정보를 인접행렬에 기록 (양방향)
for i in range(E):
    n1, n2 = data[i * 2], data[i * 2 + 1]
    adj_matrix[n1][n2] = 1
    adj_matrix[n2][n1] = 1

# --- DFS 실행 ---
result_path = DFS_stack_pop_style(1)
print(''.join(map(str, result_path)))
