import sys

sys.stdin = open('input.txt')


def DFS_stack_push_style(start_node):
    """
    스택과 인접 리스트를 사용한 DFS (Push 시점 방문 처리)
    """
    visited = [False] * (V + 1)  # 방문 여부 리스트
    stack = []  # 방문할 노드를 저장할 스택
    path = []  # 최종 탐색 경로를 저장할 리스트

    # 1. 시작 노드를 먼저 방문 처리하고 스택에 push
    visited[start_node] = True
    stack.append(start_node)

    while stack:
        # 2. 스택에서 노드를 pop하여 경로에 추가
        current_node = stack.pop()
        path.append(current_node)

        # 3. 현재 노드의 인접 노드들을 확인
        # adj_list가 내림차순 정렬되어 있으므로, 큰 번호부터 확인
        for next_node in adj_list[current_node]:
            # 4. 아직 방문하지 않은 노드를 발견하면,
            if not visited[next_node]:
                # 5. 즉시 방문 처리('예약')하고 스택에 push
                visited[next_node] = True
                stack.append(next_node)

    return path


# --- 그래프 구성 ---
V, E = map(int, input().split())
data = list(map(int, input().split()))

# 인접 리스트(Adjacency List) 생성
adj_list = [[] for _ in range(V + 1)]

# 간선 정보 입력 (양방향)
for i in range(E):
    n1, n2 = data[2 * i], data[2 * i + 1]
    adj_list[n1].append(n2)
    adj_list[n2].append(n1)

# 방문 순서를 결정하기 위해, 인접 리스트를 각 노드별로 내림차순 정렬
for i in range(1, V + 1):
    adj_list[i].sort(reverse=True)


# --- DFS 실행 ---
result_path = DFS_stack_push_style(1)
print(''.join(map(str, result_path)))
