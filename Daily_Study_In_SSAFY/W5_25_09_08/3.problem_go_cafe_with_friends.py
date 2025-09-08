# [문제] 카페에 같이 갈 친구가 2명 이상 경우의 수
# - 바이너리 카운팅 버전 코드입니다!
# - 재귀 호출로도 구현해보세요
arr = ['A', 'B', 'C', 'D', 'E']
n = len(arr)

# 1 인 bit 수를 반환하는 함수
def get_count(tar):
    cnt = 0
    for _ in range(n):
        if tar & 0x1:
            cnt += 1
        tar >>= 1

    # 같은 코드
    # for i in range(n):
    #     if (tar >> i) & 0x1:
    #         cnt += 1
    # return cnt

# 모든 부분 집합 중 원소의 수가 2개 이상인 집합의 수
answer = 0
# 모든 부분 집합을 확인
for target in range(1 << n):
    # 만약, 원소의 개수가 2개 이상이면 answer += 1
    if get_count(target) >= 2:
        answer += 1
print(answer)
