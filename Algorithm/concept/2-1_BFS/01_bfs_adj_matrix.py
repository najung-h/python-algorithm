import sys
from collections import deque

sys.stdin = open('input.txt')


def bfs_matrix(start_node, V, adj_matrix):
    """
    큐(deque)와 인접 행렬을 사용한 BFS
    """
    visited = [False] * (V + 1)  # 각 노드의 방문 여부를 기록
    path = []  # 최종 탐색 경로를 저장
    # BFS는 큐를 사용. 파이썬 list의 pop(0)은 비효율적이므로 deque 사용
    q = deque()

    # --- BFS 시작 처리 ---
    # 1. 시작 노드를 방문 처리를 하고 큐에 삽입
    # "큐에 넣었다."는 것은 "이 노드를 이미 발견해서 다음에 처리할 예정"이라는 의미.
    # 큐에 넣기 직전에 방문 처리를 하는 것이 논리적으로 명확하고 중복을 방지할 수 있음

    visited[start_node] = True
    q.append(start_node)

    # 큐가 비어있지 않은 동안 반복 ( 큐가 빌 때까지 탐색 진행)
    while q:
        # 2. 큐에서 노드를 하나 꺼냄(dequeue)
        current_node = q.popleft()
        path.append(current_node)

        # 3. 현재 노드와 인접한 모든 인접 노드를 확인해야함.
        for next_node in range(1, V+1):
            # 조건 1 : next_node가 current_node와 인접해 있는가?
            # 조건 2 : next_node가 아직 방문한 적이 없는가?
            if adj_matrix[current_node][next_node] == 1 and not visited[next_node]:
                # 4. 방문 처리 후 큐에 삽입(enqueue)
                # 두 조건을 모두 만족하면, 다음 방문 대상으로 저장
                visited[next_node] = True
                q.append(next_node)

    return path


# --- 그래프 구성 ---
V, E = map(int, input().split())
data = list(map(int, input().split()))

adj_matrix = [[0] * (V + 1) for _ in range(V + 1)]
for i in range(E):
    n1, n2 = data[i * 2], data[i * 2 + 1]
    adj_matrix[n1][n2] = 1
    adj_matrix[n2][n1] = 1

# --- BFS 실행 ---
result_path = bfs_matrix(1, V, adj_matrix)
print(''.join(map(str, result_path)))
