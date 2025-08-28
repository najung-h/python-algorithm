# 📘 DFS & BFS 정리 (with visited 관리)

## 1. 기본 개념

### BFS (Breadth-First Search)

- **너비 우선 탐색**
- 가까운 노드부터 차례대로 탐색
- **Queue (FIFO)** 사용

### DFS (Depth-First Search)

- **깊이 우선 탐색**
- 한 갈래를 끝까지 탐색 후 돌아옴
- **Stack (LIFO)** 또는 **재귀** 사용

------

## 2. 공통 구조

두 알고리즘 모두 핵심 로직은 동일하다:

1. **시작 노드**를 준비한다.
2. **방문 여부(`visited`)**를 관리한다.
3. **탐색할 노드**를 자료구조(queue/stack/recursion)에 넣는다.
4. 빼서 처리하고, 인접한 노드를 넣는다.
5. 반복.

------

## 3. 자료구조 차이

| 탐색 방법  | 자료구조   | 메서드       | 순서            |
| ---------- | ---------- | ------------ | --------------- |
| BFS        | Queue      | `popleft()`  | FIFO (선입선출) |
| DFS        | Stack      | `pop()`      | LIFO (후입선출) |
| DFS (재귀) | Call Stack | `dfs()` 호출 | LIFO            |

------

## 4. visited 관리 전략

### A. 전역 visited (한 번 방문하면 끝)

- **목적**: 도달 여부, 연결성 확인, 최단 경로
- BFS/DFS 모두 일반 그래프 탐색 시 사용
- 방문 여부를 **전역**으로 기록 → 무한 루프 방지

```python
# BFS with Global Visited (최단 거리 / 연결성 확인용)
from collections import deque   # BFS 구현을 위한 deque 불러오기

def bfs(graph, start):
    visited = set([start])      # 방문 집합 초기화 (start 방문 처리)
    q = deque([start])          # 큐 초기화 (start 노드 넣기)

    while q:                    # 큐가 빌 때까지 반복
        node = q.popleft()      # 큐의 맨 앞에서 노드 꺼내기 (FIFO)
        print(node)             # 현재 노드 처리 (출력/기록 등)

        # 인접 노드 순회
        for nxt in graph[node]:
            if nxt not in visited:      # 아직 방문하지 않은 노드라면
                visited.add(nxt)        # 방문 처리
                q.append(nxt)           # 큐에 추가 → 차례대로 탐색
```

------

### B. 경로 단위 visited (백트래킹)

- **목적**: 모든 경로 경우의 수 탐색, 최장 경로, Hamiltonian path 등
- 현재 경로에서는 방문 표시 → 재귀가 끝나면 다시 해제

```python
# DFS with Backtracking (모든 경로 탐색용)
# DFS (재귀 + 백트래킹) 예시
def dfs(x, visited, path):
    visited.add(x)          # 현재 노드를 방문 집합에 추가
    path.append(x)          # 현재 경로에 노드 추가

    # 인접한 노드들 탐색
    for nxt in graph[x]:
        if nxt not in visited:      # 아직 방문하지 않은 노드라면
            dfs(nxt, visited, path) # 재귀적으로 DFS 수행

    # ✅ 백트래킹 단계
    visited.remove(x)       # 현재 노드를 방문 집합에서 제거 (다른 경로 탐색 가능)
    path.pop()              # 현재 경로에서도 제거 (경로 복원)

```

------

### C. visited 관리 구현체

- **2D 배열** (`visited[r][c]`)
  - 격자형 문제에서 빠름, 단순.
- **set of tuples** (`visited={(r,c)}`)
  - 코드 가독성 좋음, 특히 경로 추적 시.
- **bitmask** (`visited_mask = 0b10101`)
  - 노드 수가 작을 때(≤20) 고속 상태 관리에 활용.

------

## 5. 문제 유형별 탐색 방식

| 문제 유형           | 예시                               | 탐색 방법      | visited 방식                     |
| ------------------- | ---------------------------------- | -------------- | -------------------------------- |
| 단순 연결 확인      | 그래프 연결성, 미로 탈출 가능 여부 | BFS/DFS        | 전역 visited                     |
| 최단 거리           | 미로 최단 경로, 토마토 익기        | BFS            | 전역 visited                     |
| 최장 거리           | 등산로 조성, Hamiltonian path      | DFS            | 경로 단위 visited (백트래킹)     |
| 모든 경로 경우의 수 | start→end 모든 경로 개수           | DFS            | 경로 단위 visited                |
| 트리 탐색           | preorder/inorder/postorder         | DFS (재귀)     | visited 불필요(사이클 없음)      |
| 가중치 최단 경로    | Dijkstra, Bellman-Ford             | 우선순위 큐/DP | visited 대신 거리 배열           |
| 위상 정렬           | DAG 정렬                           | BFS(Kahn), DFS | visited + 진입차수 관리          |
| 상태 탐색           | 퍼즐, 게임 판                      | BFS            | visited = 상태 저장(튜플/문자열) |

------

## 6. 실전 예시

### BFS: 2D 격자 최단거리

```python
from collections import deque   # BFS 구현에 필요한 deque 불러오기

def bfs(start, goal, grid):
    n, m = len(grid), len(grid[0])     # 격자의 크기 (행, 열)
    visited = [[0]*m for _ in range(n)] # 방문 여부를 저장하는 2차원 배열 (0=미방문, 1=방문)
    
    # 큐 초기화: (x좌표, y좌표, 현재까지의 거리)
    q = deque([(start[0], start[1], 0)])  
    visited[start[0]][start[1]] = 1     # 시작점 방문 처리

    while q:                            # 큐가 빌 때까지 반복
        x, y, d = q.popleft()           # 큐의 맨 앞 원소 꺼내기
        if (x, y) == goal:              # 목표 지점 도달 시
            return d                    # 현재까지의 거리 반환

        # 상하좌우 4방향 탐색
        for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            nx, ny = x+dx, y+dy         # 다음 좌표 계산
            # 격자 범위 안에 있고, 방문하지 않았으며, 길(grid[nx][ny]==1)일 때
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and grid[nx][ny]==1:
                visited[nx][ny] = 1     # 방문 표시
                q.append((nx, ny, d+1)) # 거리 +1 해서 큐에 추가
    return -1                           # 목표에 도달할 수 없는 경우 -1 반환
```

------

### DFS + 백트래킹: 등산로 조성 (SWEA 1949)

```python
def solve(board, K):
    N = len(board)                              # 지도 크기
    max_h = max(max(row) for row in board)      # 최고 높이 찾기
    # 최고 높이 봉우리 좌표 리스트
    starts = [(i,j) for i in range(N) for j in range(N) if board[i][j]==max_h]

    visited = [[False]*N for _ in range(N)]     # 방문 여부 2차원 배열
    best = 0                                    # 최장 등산로 길이 저장용 변수

    def dfs(x, y, used_cut, length):
        nonlocal best                           # 외부 변수(best) 갱신 가능하도록 선언
        best = max(best, length)                # 현재 경로 길이를 최장 길이와 비교해 갱신

        # 상하좌우 4방향 탐색
        for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            nx, ny = x+dx, y+dy                 # 다음 좌표
            if 0<=nx<N and 0<=ny<N and not visited[nx][ny]: # 격자 내부 & 미방문
                if board[nx][ny] < board[x][y]:
                    # 1) 다음 칸이 현재보다 낮으면 그냥 이동 가능
                    visited[nx][ny] = True
                    dfs(nx, ny, used_cut, length+1)
                    visited[nx][ny] = False     # 백트래킹 (다른 경로 위해 방문 해제)

                elif not used_cut and board[nx][ny]-K < board[x][y]:
                    # 2) 아직 공사 기회를 쓰지 않았고, K만큼 깎으면 이동 가능할 때
                    tmp = board[nx][ny]         # 원래 높이 저장
                    board[nx][ny] = board[x][y]-1  # 현재 높이보다 1 낮게 깎기

                    visited[nx][ny] = True
                    dfs(nx, ny, True, length+1) # 공사 사용 표시(used_cut=True)
                    visited[nx][ny] = False

                    board[nx][ny] = tmp         # 원상복구 (백트래킹)

    # 모든 최고 봉우리에서 시작 DFS 수행
    for sx, sy in starts:
        visited[sx][sy] = True                  # 시작점 방문 처리
        dfs(sx, sy, False, 1)                   # 시작점 포함 길이 = 1
        visited[sx][sy] = False                 # 백트래킹 (다른 시작점 고려)

    return best                                 # 최장 등산로 길이 반환
```

------

## 7. 연관 학습 주제

- **BFS 변형**: 0-1 BFS, 다중 시작점 BFS, 상태공간 BFS(큐에 `(좌표, 상태)` 저장).
- **DFS 변형**: Flood fill, 백트래킹(순열, 조합, N-Queens).
- **Graph Algorithms**: Dijkstra, Floyd-Warshall, Kruskal/Prim(MST).
- **Advanced visited 관리**:
  - `visited[x][y][state]` (예: 열쇠/문 BFS)
  - `visited_mask` (예: Traveling Salesman Problem).

------

## 8. 문제 접근 전략

1. **문제 목표 파악**
   - 연결 여부? → DFS/BFS
   - 최단 거리? → BFS
   - 최장 거리/모든 경로? → DFS + 백트래킹
   - 가중치? → 다익스트라/벨만포드
2. **그래프 모델링**
   - 2D 격자는 (r,c)를 노드로 보고 상하좌우 간선 연결
   - 일반 그래프는 인접리스트 사용
3. **visited 관리 결정**
   - 단순 탐색/최단 경로 → 전역 visited
   - 경우의 수/최장 경로 → 경로 단위 visited
4. **자료구조 선택**
   - BFS → `deque`
   - DFS → `stack` or 재귀
5. **시간복잡도 점검**
   - N ≤ 10^3 → BFS/DFS 가능
   - N ≤ 20 → 비트마스크 DFS 고려

------

# ✅ 마무리

앞으로 DFS/BFS 문제를 만났을 때는:

1. **“무엇을 구하는 문제인가?”** → 최단/최장/경로 수/도달 여부
2. **“재방문 허용 여부는?”** → visited 전역 vs 경로 단위
3. **“가중치가 있나?”** → BFS/DFS vs 다익스트라
4. **“상태 변화가 있나?”** → visited에 상태를 추가 관리

👉 항상 **문제 목표 → visited 전략 → 탐색 방식** 순으로 사고하면 됩니다.