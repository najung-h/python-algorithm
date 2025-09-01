import sys

sys.stdin = open("input.txt")


# 입력 처리
N, M = map(int, input().split())
grid = [list(map(int, input())) for _ in range(N)]

# 방문 여부
visited = [[False] * M for _ in range(N)]

# 상, 하, 좌, 우, 대각선 4방향을 포함한 8방향 델타
dr = (-1, 1, 0, 0, -1, -1, 1, 1)
dc = (0, 0, -1, 1, -1, 1, -1, 1)


# DFS 함수 정의 (재귀 방식)
def dfs(r, c):
    '''섬에 들어가서, 섬 8 방향을 사이즈를 재는 것'''
    '''빈 지도에 방문 처리 섬을 그려나가는 것.'''
    # 현재 위치를 방문했다고 표기
    visited[r][c] = True

    # 현재 위치에서 8방향의 이웃을 확인
    for i in range(8):
        nr, nc = r + dr[i], c + dc[i]

        # 다음 이동 위치가 격자 범위 안에 있고,
        if 0<= nr < N and 0<= nc < M:
            # 그곳이 땅(1)이면서, 아직 방문하지 않았다면,
            if grid[nr][nc] == 1 and visited[nr][nc]:
                # 재귀적으로 탐색을 이어감
                # 한 칸 이동해서 8칸을 보고, 보고 , 보고, 보고,
                dfs(nr, nc)


# --- 메인 로직 ---
island_count = 0

# 모든 칸을 하나씩 확인합니다.
for i in range(N):
    for j in range(M):
        # 현재 위치가 땅(1)이면서, 아직 방문하지 않은 곳이라면,
        if grid[i][j] == 1:
            # 새로운 섬을 발견한 것이다.
            island_count += 1
            # 이 섬과 연결된 모든 땅을 방문 처리 하기 위해 dfs를 시작
            dfs(i, j)


# 최종 섬의 개수를 출력합니다.
print(island_count)
