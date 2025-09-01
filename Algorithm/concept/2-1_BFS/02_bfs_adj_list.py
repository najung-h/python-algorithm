import sys
from collections import deque

sys.stdin = open('input.txt')


def bfs_list(start_node, V, adj_list):  # start_node만 받아도 상관 없음
    """
    큐(deque)와 인접 리스트를 사용한 BFS
    """
    visited = [False] * (V + 1)
    path = []
    q = deque()

    # --- BFS 시작 처리 ---
    # 1. 시작 노드 방문 처리 후 큐에 삽입
    visited[start_node] = True
    q.append(start_node)

    # 큐가 빌 때까지 탐색
    # 2. 큐에서 맨 앞에 있는 노드를 하나 꺼냄
    while q:
        current_node = q.popleft()
        path.append(current_node)
        
        # 3. 현재 노드와 '실제로 인접한' 노드들만 확인
        #   "sorted?" : 이 문제에서 '번호가 작은 인접 노드부터 방문'하라는 조건이 있기 때문에
        #   오름차순으로 정렬하여 q에 순서대로 배치하기 위함.
        #   (BFS 알고리즘 관점에서 필수 작성 요건은 아님)
        for next_node in sorted(adj_list[current_node]): 
            # 아직 방문하지 않은 인접 노드라면,
            if not visited[next_node]:
                # 4. 방문 처리 후, 다음 탐색을 위해 큐에 추가
                visited[next_node] = True
                q.append(next_node)

    return path



# --- 그래프 구성 ---
V, E = map(int, input().split())
data = list(map(int, input().split()))

adj_list = [[] for _ in range(V + 1)]
for i in range(E):
    n1, n2 = data[i * 2], data[i * 2 + 1]
    adj_list[n1].append(n2)
    adj_list[n2].append(n1)

# --- BFS 실행 ---
result_path = bfs_list(1, V, adj_list)
print(''.join(map(str, result_path)))
