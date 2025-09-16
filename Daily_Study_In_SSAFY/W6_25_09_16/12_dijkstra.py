# import sys
import heapq

# sys.stdin = open('dijkstra_input.txt')


def dijkstra(start_node, num_vertices, adj_list):
    """
    Dijkstra 알고리즘 (우선순위 큐 활용)
    """
    # 1. 초기화 작업
    # 1번 정점으로부터 모든 정점까지의 거리를 기록할 리스트
    INF = float('inf')
    distance = [INF] * (num_vertices + 1)

    # 우선순위 큐(최소 힙) 생성
    priority_queue = []

    # 2. 시작 노드 처리
    # 2.1 시작 노드까지의 거리는 0으로 설정
    # 2.2 우선순위 큐에 삽입
    # 힙에는 (거리, 노드 번호) 순으로 저장, 최소힙이기 때문에 나중에 거리가 짧은 순으로 꺼내기 위함
    distance[start_node] = 0
    heapq.heappush(priority_queue, (0, start_node))

    # 3. main
    # 큐가 빌 때까지 반복
    while priority_queue:
        # 4. 현재까지 가장 거리가 짧은 노드를 힙에서 꺼냄
        current_dist, current_node = heapq.heappop(priority_queue)

        # 무시할 수 있을까?
        # 이미 처리한 노드라면 ( 더 짧은 경로를 이미 발견했다면 ) 무시
        # 내가 과거에 이 현재 노드에 더 짧게 방문한 적이 있다면 탐색은 무의미
        # 등호 넣으면 안 됨 : 최초 노드가 처리되지 않음
        if distance[current_node] < current_dist:
            continue

        # 5. 현재 노드의 인접한 노드들을 확인
        for adj_node, weight in adj_list[current_node]:
            # 새로운 경로의 거리
            new_dist = current_dist + weight
            
            # 6. 새로운 경로가 기존 경로보다 더 짧으면 갱신 (아니면 버리기)
            if new_dist < distance[adj_node]:
                distance[adj_node] = new_dist
                # 갱신된 정보를 우선순위 큐에 추가
                heapq.heappush(priority_queue, [new_dist, adj_node])


    return distance

    

# --- 실행 예시 ---
# V, E = map(int, input().split())
# start = int(input())
# adj_list = [[] for _ in range(V + 1)]
# for _ in range(E):
#     u, v, w = map(int, input().split())
#     adj_list[u].append((v, w))

# print('봐봐', adj_list)
# [[(1, 2), (2, 4)], [(2, 1), (3, 7)], [(4, 3)], [(4, 2), (5, 1)], [(5, 5)], [], []]





# (input 받았다고 가정하고, 정보 직접 입력할게요)
# images/dijkstra-image.png 참고
V, E, start = 6, 9, 1
adj_list = [
    [],
    [(2, 2), (3, 5), (4, 1)],  # (정점, 가중치)
    [(1, 2), (3, 3), (4, 2)],
    [(1, 5), (2, 3), (5, 5)],
    [(1, 1), (2, 2), (5, 1)],
    [(3, 5), (4, 1), (6, 2)],
    [(5, 2)],
]

# 다익스트라 알고리즘 실행
shortest_distances = dijkstra(start, V, adj_list)

# 1번 노드에서 각 노드까지의 최단 거리
print(shortest_distances)  # [inf, 0, 2, 5, 1, 2, 4]

# 결과 출력
for i in range(1, V + 1):
    if shortest_distances[i] == float('inf'):
        print(f"1번 노드에서 {i}번 노드까지: 도달 불가")
    else:
        print(
            f"1번 노드에서 {i}번 노드까지의 최단 거리: {shortest_distances[i]}"
        )
