import sys

sys.stdin = open('input.txt')


def DFS_stack_push_style(start):
    '''
    스택을 활용한 DFS (Push 시점 방문 처리)
    '''
    visited = [False] * (V + 1)  # 방문 기록 리스트
    stack = []  # 방문할 노드를 저장할 스택
    path = []  # 최종 탐색 경로를 저장할 리스트

    # 1. 시작 노드를 방문 처리하고 스택에 push
    visited[start] = True
    stack.append(start)

    while stack:
        # 2. 스택에서 노드를 pop. 이 노드는 방문이 '확정'된 노드
        current_node = stack.pop()
        path.append(current_node)

        # 3. 현재 노드의 인접 노드들을 확인
        # 작은 번호를 우선 방문하고 싶다면, 스택에는 큰 번호부터 push
        for next_node in range(V, 0, -1):
            # 현재 노드와 연결되어 있고, 아직 방문하지 않았다면
            if (
                adj_matrix[current_node][next_node] == 1
                and not visited[next_node]
            ):
                # 4. 즉시 방문 처리('예약')하고 스택에 push
                visited[next_node] = True
                stack.append(next_node)

    return path  # 최종 탐색 경로를 반환


# --- 그래프 구성 ---
V, E = map(int, input().split())
data = list(map(int, input().split()))

# 인접 행렬 생성
adj_matrix = [[0] * (V + 1) for _ in range(V + 1)]

# 간선 정보
for i in range(E):
    n1, n2 = data[2 * i], data[2 * i + 1]
    adj_matrix[n1][n2] = 1
    adj_matrix[n2][n1] = 1


# --- DFS 실행 ---
result_path = DFS_stack_push_style(1)
print(''.join(map(str, result_path)))
