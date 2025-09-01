import sys

sys.stdin = open('input.txt')


def dfs_recursive_list(current_node, adj_list, visited, path):
    """
    인접 리스트와 재귀를 이용한 DFS
    """
    # 1. 현재 정점을 방문 처리 & 경로 추가
    visited[current_node] = True
    path.append(current_node)

    # 2. 현재 정점에 인접한 노드들을 직접 순회
    # 인접 행렬처럼 모든 노드를 확인할 필요 없이,
    # 인접한 노드를 바로 탐색 가능

    for next_node in adj_list[current_node]:
        # 인접 정점이 아직 방문하지 않았다면 재귀 호출 진행
        if not visited[next_node]:
            dfs_recursive_list(next_node, adj_list, visited, path)




# --- 그래프 구성 ---
# --- 그래프 구성 (인접 행렬) ---
# 정점과 간선의 개수를 입력 받기
V, E = map(int, input().split())

# 간선 정보를 리스트 하나로 입력 받기
edge_data = list(map(int, input().split()))

# 0번 인덱스를 쓰지 않을 예정이라, 한 개 여유를 줘서, V+1개만큼만 만들기
adj_list = [[] for _ in range(V+1)]
# print(adj_list)
# [[], [], [], [], [], [], [], []]


# 간선의 개수만큼 반복하면서 2개씩 짝지어서 표기
for i in range(E):
    # 두 정점을 저장 (n1과 n2는 인접한 두 정점을 의미)
    n1, n2 = edge_data[i*2], edge_data[i*2 + 1] 

    # 정점 n1번 리스트에 n2 정점을 추가
    adj_list[n1].append(n2)
    # 무향 그래프이므로, 정점 n2번 리스트에도 n1 정점을 추가
    adj_list[n2].append(n1)





# --- DFS 실행 ---
visited = [False] * (V+1)
result_path = []

# 1번 정점부터 탐색 시작
dfs_recursive_list(1, adj_list, visited, result_path)

print(result_path)


