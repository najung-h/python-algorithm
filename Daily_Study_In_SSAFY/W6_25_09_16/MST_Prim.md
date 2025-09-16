## Prim 알고리즘

#### (정의)

**<u>하나의 정점</u>**에서 연결된 간선들 중에 하나씩 선택하면서 MST를 만들어 가는 방식

-> BFS처럼 접근한다고 생각하면 이해하기 수월하다.

1. 임의 정점을 하나 선택해서 시작
2. 선택한 정점과 인접하는 정점들 중의 **최소 비용의 간선이 존재하는 정점**을 선택
3. 모든 정점이 선택될 때까지 1, 2 과정을 반복



그렇다면,

queue에 

(1, 30),  (2, 20),  (3, 5) 

이런 식으로 들어가 있다고 했을 때, **가중치가 작은 노드를 먼저 꺼내야된다.** == 즉, 우선순위가 생긴다

때문에, 일반적인 queue가 아니라, 우선순위를 사용할 수 있는 heapq를 사용할 것이다.

참고로, 시간 복잡도까지 생각하면, 삽입에 O(logN) 삭제가 O(logN)



```python
import sys
sys.stdin = open('mst_input.txt', 'r')

# 특정 정점 기준으로 시작
# 갈 수 있는 노드들 중 가중치가 가장 작은 노드부터 간다
# 작은 노드를 먼저 꺼내기 위해 우선순위큐를 활용한다.
# 우선순위 큐는 정렬 기준이 가장 앞에 있는 애를 기준으로 하게끔되어있기 때문에
# (가중치, 노드)형태로 담아두면 됩니다.

# 힙큐를 쓰는 bfs 구현이라고 보셔도 됩니다.
# 단 다른 점이 또 있다면, 방문 처리를 하는 시점이 조금 다름


# import heapq #비추천
from heapq import heappop, heappush  # 추천


def prim(start_node):
    pq = [(0, start_node)]  # (가중치, 노드) 형태
    MST = [0] * V # visited 와 동일하다 # 미방문이 0
    min_weight = 0 #최종적으로 구할 최소 비용

    while pq:
        weight, node = heappop(pq) # 가장 작은 가중치

        # 이미 방문한 노드라면 continue
        if MST[node]:
            continue

        # MST에서는, BFS와 달리 여기에서 방문 처리
        MST[node] = 1  # node로 가는 최소 비용이 선택되었다.
        min_weight += weight # 누적합 추가


        for next_node in range(V):
            # 갈 수 없으면 continue # 연결되어 있지 않음
            if graph[node][next_node] == 0:
                continue

            # 이미 방문했으면 continue
            if MST[next_node]:
                continue
            
            # 가중치, next_node
            # 원래 BFS에서는 여기서 방문 처리를 해주었는데, MST에서는 안됩니다.
            # 내가 확인하자마자 방문처리를 해버린다면
            # 최소를 구할 수가 없습니다.
            # MST는 꺼냈을 때 비교해줍니다.
            heappush(pq, (graph[node][next_node], next_node))


    return min_weight



V, E = map(int, input().split())
graph = [[0] * V for _ in range(V)] #인접 행렬 vs 인접 리스트
# 오늘은 인접 행렬로 우선 해보겠습니다.


for _ in range(E):
    start, end, weight = map(int, input().split())
    graph[start][end] = weight
    graph[end][start] = weight # 양방향으로 연결


result = prim(0) #출발 정점과 함께 시작 
# 단, 출발 정점을 바꾸어도, 최소 비용은 똑같다.
# 단 그래프가 다르게 나올 수는 있다.
print(f'최소 비용 = {result}')
```

```txt
최소 비용 = 175
```

