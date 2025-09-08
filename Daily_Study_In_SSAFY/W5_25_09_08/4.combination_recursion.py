# 5명 중 3명을 순서없이 고르기
arr = ['A', 'B', 'C', 'D', 'E']
N = 3
path = []


def recur(cnt, start):
    # N명을 뽑으면 종료
    if cnt == N:
        print(*path)
        return

    for i in range(start, len(arr)):
        path.append(arr[i])
        # recur(cnt + 1, i)  # i 번째를 골랐으니, 다음 선택은 i 부터 고려 (중복을 허용하는 조합)
        recur(cnt + 1, i + 1)  # i 번째를 골랐으니, 다음 선택은 i + 1 부터 고려 (중복을 허용하지 않는 조합)
        path.pop()


recur(0, 0)

