# BFS

---

너비 우선 탐색



그래프를 탐색하는 방법에는 두 가지가 있습니다.

첫째는, BFS(너비 우선 탐색)

둘째는, DFS(깊이 우선 탐색)



오늘은 BFS, 너비 우선 탐색을 보시겠습니다.



BFS, 자세히는 Breadth First Search인데요

탐색 시작점의 인접한 정점들을 모두 차례로 방문한 후에,

방문했던 정점을 시작점으로 하여 다시 인접한 정점들을 차례로 방문하는 방식입니다.



​          ㅇ

​    /    ㅣ    \

  ㅇ    ㅇ      ㅇ

  /\             /ㅣ\

ㅇㅇ        ㅇㅇㅇ



의 그래프가 그려져있을 때는 

순서가

1

234

56789 이렇게 되는거죠.



자, 그래서, BFS는

인접한 정점들에 대해 탐색을 하고 나서야

이후에 너비 우선 탐색을 차례로 진행해야 하니깐요

선입선출 형태의 자료구조인 큐를 활용하게 됩니다.



< 요약 >

**시작 노드에서 가장 가까운 노드부터 우선적으로 방문한다.**

**-> 선입선출 구조의 큐와 완벽하게 일치**



---

# 구현 1  _  인접 행렬

input

```txt
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
```



```python
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
```

output

```txt
$ python 01_bfs_adj_matrix.py
1376542
```



---

# 구현 2  _  인접 리스트

input

```txt
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
```

```python
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

```

output

```txt
$ python 02_bfs_adj_list.py 
1234576\
```



