N = int(input())
score_lst = [0]
for i in range(N):
    score_lst.append(int(input()))
# print(score_lst)
# 동적 프로그래밍 사용하겠습니다

# 시작점은 계단이 아님
dp = [0]* (N +1)
# 각 계단까지의 최소 거리를 구하되, 
# 

# dp i번째 원소의 의미는 i번째 계단까지 가기 위한 
dp[0] = 0
dp[1] = score_lst[1]
dp[2] = dp[1] + score_lst[2]
# 연속한 3칸을 한칸씩 올랐다면 재조정

#cnt = 0
for stairs in range(3, N+1): 
    dp[stairs] = max(dp[stairs-2] + score_lst[stairs],
            dp[stairs-3] + score_lst[stairs-1] + score_lst[stairs])
        
        
    
    
'''
dp[stairs] = dp[stairs-1] + score_lst[stairs]
# 3칸마다 직전 3칸 중에 건너뛴 칸(0)이 하나도 없다면,
# 어떤 칸을 건너뛰는 게 이득인가를 계산
# 각 칸에서는 누적합 (뛰어넘을 경우는 변화x)
    if stairs>= 3:
        window= dp[stairs-2:stairs+1]
        # 직전 세 칸 중에 건너뛴게 없었다면
        if len(set(window)) == 3:
            dp[stairs] -= min(window)
# 직전 세 칸 중에서 가장 작은 칸을 확인해서 거기 누적합을 초기화시키자
'''
print(dp[N])