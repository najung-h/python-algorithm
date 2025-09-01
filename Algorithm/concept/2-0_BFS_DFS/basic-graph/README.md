# graph 란

---





1. 인접 행렬로 구현하기
```python
import sys
sys.stdin = open('input.txt')


# --- 그래프 구성 (인접 행렬) ---
# 정점과 간선의 개수를 입력 받기
V, E = map(int, input().split())

# 1. V+1 * V+1 크기의 2차원 리스트를 0으로 초기화
adj_matrix = [[0] * (V+1) for _ in range(V+1)]
# print(adj_matrix)

# 간선 정보를 리스트 하나로 입력 받기
edge_data = list(map(int, input().split()))

# 2. 간선 정보를 바탕으로 2개씩 짝지어서 인접 행렬에 표기
# 총 표기 회수는 간선의 개수 만큼(E번)
for i in range(E):
    # 정점의 번호를 저장 ( 인접 행렬의 인덱스 값으로 쓰임 )
    n1, n2 = edge_data[i * 2], edge_data[i*2+1]

    # 두 정점이 인접해 있다는 것을 1로 표기
    adj_matrix[n1][n2] =1

    # 무향 그래프이므로, 반대 방향도 연결 되었음을 표기 행야한다
    adj_matrix[n2][n1] =1


# --- 결과 확인 ---
print(adj_matrix)
'''
[   [0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 1, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 1, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 1],
    [0, 0, 1, 0, 0, 0, 1, 0], 
    [0, 0, 1, 0, 0, 0, 1, 0], 
    [0, 0, 0, 0, 1, 1, 0, 1], 
    [0, 0, 0, 1, 0, 0, 1, 0]]'''


```



2. 인접 리스트로 구현하기

```python

import sys
sys.stdin = open('input.txt')


# --- 그래프 구성 (인접 행렬) ---
# 정점과 간선의 개수를 입력 받기
V, E = map(int, input().split())

# 간선 정보를 리스트 하나로 입력 받기
edge_data = list(map(int, input().split()))

# 0번 인덱스를 쓰지 않을 예정이라, 한 개 여유를 줘서, V+1개만큼만 만들기
adj_lst2 = [[] for _ in range(V+1)]
# print(adj_lst2)
# [[], [], [], [], [], [], [], []]


# 간선의 개수만큼 반복하면서 2개씩 짝지어서 표기
for i in range(E):
    # 두 정점을 저장 (n1과 n2는 인접한 두 정점을 의미)
    n1, n2 = edge_data[i*2], edge_data[i*2 + 1] 

    # 정점 n1번 리스트에 n2 정점을 추가
    adj_lst2[n1].append(n2)
    # 무향 그래프이므로, 정점 n2번 리스트에도 n1 정점을 추가
    adj_lst2[n2].append(n1)





'''
print(adj_lst2)
[[], 
 [2, 3],   # 1번과 연결된 친구들~
 [1, 4, 5], # 2번과 연결된 친구들~
 [1, 7], 
 [2, 6], 
 [2, 6], 
 [4, 5, 7], 
 [6, 3]
 ]
'''


```