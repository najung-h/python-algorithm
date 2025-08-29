import sys
sys.stdin = open('input_dfs.txt', 'r')

def dfs(start):
    visited[start] = True

    for item in lst[a]:
        if not visited[item] : 
            dfs(item)
            

V, E = list(map(int, input().split()))
info = list(map(int, input().split()))

lst = [[] for _ in range(V+1 )] # 첫번째 인덱스 안 쓸거임.
visited = [False * (V+1)]

for i in range(E):
    a,b = info[i*2], info[i*2+1]

    lst[a].append(b)
    lst[b].append(a)


# [[], [2, 3], [1, 4, 5], [1, 7], [2, 6], [2, 6], [4, 5, 7], [6, 3]]


