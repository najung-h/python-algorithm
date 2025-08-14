#import sys
#sys.stdin = open("input.txt", "r")

cnt = 0


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())  # 수열의 길이
    arr = list(map(int, input()))
    print(arr)

    result_lst = []

    for a in arr:

        if a == 1:
            cnt += 1
        else :
            result_lst.append(cnt)
            cnt = 0

    print(result_lst)

    print(f'#{test_case} {max(result_lst)}')
