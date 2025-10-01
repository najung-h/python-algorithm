# 입력 받기
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
#  출력값 초기화
ans = 0

# 비숍 놓을 수 있는 곳이 1 아닌 곳이 0
# 서로가 잡을 수 없는 위치에 놓을 수 있는 비숍의 최대 개수

# 왼쪽 위 / 오른쪽 위 / 왼쪽 아래 / 오른쪽 아래
dr = (-1, -1, 1, 1)
dc = (-1, 1, -1, 1)

# 비숍이 놓이는 순간 오른쪽 대각선과 왼쪽 대각선을 점유해버림
# 비숍이 놓일 수 있는 곳 중에서
# 부분집합을 선택한 다음에
# 오른쪽 대각선과 왼쪽 대각선 정보를 싹 담고,
# 그 set끼리 교집합 했을 때 원소가 있으면 실패
def diagonal_set(r,c):
    '''
    어떤 곳에 비솝이 놓인다고 치고, 
    관련된 대각선 좌표들 싹 set에 담아다가 반환해주는 함수
    '''
    res = set()
    for d in range(4): # 각 방향 별로 
        for k in range(1, N): # 최대 n 번까지
            nr = r + dr[d] * k 
            nc = c + dc[d] * k 
            if  nr >= N or nr < 0 or nc < 0 or nc >= N:
                # 그 방향은 더 이상 안 돼. 백트래킹
                break
            if (nr, nc) in impossible:
                continue
            res.add((nr, nc))
    return res

def is_not_meet(subset):
    total_set = set()
    for s in subset:
        # print('s is : ', candi[s][2])
        now_set = candi[s][2]
        # print(now_set)
        # print(total_set) # 왜 계속 빈집합으로 출력이될까요?흠,
        if len(total_set.intersection(now_set)) != 0: # 교집합 발생
            return False
        # print([candi[s] for s in subset])
        total_set = total_set.union(now_set)
    # print('total set은 ',total_set)
    return True # 안 만난다.


# 비숍이 놓일 수 있는 곳의 좌표를 뽑아.
candi = []
impossible = []
for r in range(N):
    for c in range(N):
        if arr[r][c] == 1:
            # 비숍을 놓을 수 있어
            candi.append((r,c, diagonal_set(r,c)))
        elif arr[r][c] ==0:
            impossible.append((r,c))
# print(candi)

# print(candi)

candi_cnt = len(candi)
# 부분집합 비트마스크 연산
for i in range(1<<candi_cnt):
    # 부분집합 마다 초기화
    subset = []
    for j in range(candi_cnt):
        if i & (1<<j):
            subset.append(j)

    if len(subset) < ans:
        # 어차피 짧다면
        continue
    
    # 모든 비숍이 만나지 않는다면
    

    if is_not_meet(subset):
        # print('이번 부분집합은 : ',subset)
        # 자기 자신까지 더하기
        ans = max(len(subset)+1, ans)

print(ans)