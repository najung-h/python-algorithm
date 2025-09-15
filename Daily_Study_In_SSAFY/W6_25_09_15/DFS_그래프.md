#### **DFS (Depth First Search, 깊이 우선 탐색) 알고리즘 - 재귀**

- 모든 정점을 중복없이 빠짐없이 방문하는 경우
  - G : 탐색할 그래프
  - v : 방문하는 정점

```python
def dfs_recursive(graph, v, visited):
    # 현재 노드 방문 처리
    visited[v] = True
    print(v, end=" ")   # 방문 순서 출력

    # 인접 노드 탐색
    for w in graph[v]:
        if not visited[w]:
            dfs_recursive(graph, w, visited)


# 사용 예시
graph = {
    0: [1, 2],
    1: [0, 3],
    2: [0, 3],
    3: [1, 2, 4],
    4: [3]
}

visited = [False] * len(graph)
dfs_recursive(graph, 0, visited)
# 출력 예시: 0 1 3 2 4

```





#### **DFS 알고리즘 - 반복**

```python
def dfs_iterative(graph, start):
    visited = [False] * len(graph)   # 방문 여부 체크 배열
    stack = [start]                  # 스택 초기화

    while stack:
        v = stack.pop()              # 스택에서 하나 꺼내기
        if not visited[v]:           # 아직 방문하지 않았다면
            print(v, end=" ")        # 방문 처리 (출력)
            visited[v] = True

            # 인접 정점을 스택에 추가 (역순으로 넣으면 재귀 DFS와 순서 동일)
            for w in reversed(graph[v]):
                if not visited[w]:
                    stack.append(w)


# 사용 예시 (인접 리스트 그래프)
graph = {
    0: [1, 2, 5, 6],
    1: [],
    2: [],
    3: [],
    4: [3],
    5: [3, 4],
    6: [4]
}

dfs_iterative(graph, 0)
# 출력 예: 0 1 2 5 3 4 6

```



#### 참고로 방문 표시는 두번째 함수처럼 기록하는 게 훨씬 좋습니다.

```python
def dfs_with_check(graph, start):
    # 방문 여부를 기록할 배열 (정점 개수만큼 False 초기화)
    visited = [False] * len(graph)

    # DFS용 스택 (시작 정점 push)
    stack = [start]

    # 탐색 과정을 기록할 리스트 (방문한 정점, 스택 상태 저장)
    steps = []

    # 스택이 빌 때까지 반복
    while stack:
        v = stack.pop()  # 스택에서 하나 꺼내기

        # 아직 방문하지 않았다면
        if not visited[v]:
            visited[v] = True  # 방문 표시
            steps.append((v, stack[:]))  # 현재 방문 정점과 스택 상태 기록

            # 인접 정점들을 순회 (재귀 DFS와 순서 맞추기 위해 역순으로 push)
            for w in reversed(graph[v]):
                if not visited[w]:
                    stack.append(w)  # 아직 방문 안 했으면 push

    return steps


def dfs_no_duplicate(graph, start):
    # 방문 여부 기록
    visited = [False] * len(graph)

    # 시작 정점을 push하면서 바로 방문 표시
    stack = [start]
    visited[start] = True

    # 탐색 과정을 기록
    steps = []

    # 스택이 빌 때까지 반복
    while stack:
        v = stack.pop()  # 스택에서 하나 꺼냄
        steps.append((v, stack[:]))  # 방문 정점과 스택 상태 기록

        # 인접 정점들을 순회
        for w in reversed(graph[v]):
            if not visited[w]:
                stack.append(w)      # push
                visited[w] = True    # push하는 순간 방문 처리 (중복 방지)

    return steps



graph = {
    0: [1, 2],
    1: [0, 3],
    2: [0, 3],
    3: [1, 2, 4],
    4: [3]
}

print("중복검사 DFS:", dfs_with_check(graph, 0))
print("중복제거 DFS:", dfs_no_duplicate(graph, 0))

```



실행 과정 비교 (시작 정점 = 0)

| 단계 | **중복검사 DFS (pop 후 검사)** | 스택 상태 | **중복제거 DFS (push 시 검사)**  | 스택 상태 |
| ---- | ------------------------------ | --------- | -------------------------------- | --------- |
| 1    | pop(0), 방문 → push(2,1)       | [2,1]     | pop(0), 방문 → push(2,1)         | [2,1]     |
| 2    | pop(1), 방문 → push(3,0)       | [2,3,0]   | pop(1), 방문 → push(3)           | [2,3]     |
| 3    | pop(0), 이미 방문됨 skip       | [2,3]     | pop(3), 방문 → push(4,2)         | [2,4,2]   |
| 4    | pop(3), 방문 → push(4,2,1)     | [2,4,2,1] | pop(2), 방문 skip (이미 visited) | [2,4]     |
| 5    | pop(1), 이미 방문됨 skip       | [2,4,2]   | pop(4), 방문                     | [2]       |
| 6    | pop(2), 방문                   | [2,4]     | pop(2), skip                     | []        |
| 7    | pop(4), 방문                   | [2]       | 끝                               |           |
| 8    | pop(2), skip                   | []        |                                  |           |



즉, 아래와 같은 이점을 뒤쪽의 함수가 가집니다.

<u>**때문에 visited처리하자마자 push하는 게 정석인 걸로 기억해둡시다.**</u>

| 구분                   | `dfs_with_check`                                             | `dfs_no_duplicate`                                           |
| ---------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 방문 표시 시점         | **pop 이후** (정점을 꺼내 실제 방문할 때)                    | **push 시점** (스택에 올리면서 곧바로)                       |
| 중복 push 가능성       | **있음**. 어떤 정점 `v`가 여러 부모로부터 *방문되기 전에* 스택에 여러 번 올라갈 수 있음 | **없음**. 한 번 push할 때 바로 `visited[v]=True`라, 이후 부모가 또 보더라도 push 안 됨 |
| 시간/공간 오버헤드     | 불필요한 pop(“꺼내서 보니 이미 방문”)이 생겨 **추가 연산/스택 사용량** ↑ | 각 정점이 최대 1번만 스택에 올라가 **오버헤드 최소**         |
| 순서 안정성            | 중복 원소가 스택 위에 끼어들어 **방문 순서가 미세하게 흔들릴 수 있음**(정점 처리 자체는 올바름) | 더 **예측 가능**. 재귀 DFS의 “발견(Discovery) 시점 방문표시”와 동일한 의미 |
| 재귀 DFS와의 의미 대응 | 재귀 DFS와 **다름**(재귀는 진입하자마자 visited 표시)        | 재귀 DFS의 의미와 **동일**(발견=push 시 바로 방문표시)       |
| 최악 시간복잡도        | O(V+E+K) (K = 중복 push/pop 수, 그래프에 따라 E 크기까지 커질 수 있음) | O(V+E)                                                       |
| 최악 스택 크기         | O(E)까지 부풀 수 있음                                        | O(V)                                                         |