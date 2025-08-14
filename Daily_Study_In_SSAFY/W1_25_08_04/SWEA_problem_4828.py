import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())

# 싹 다 num_lst 로 데리고와서
# min max찾고
# 바로 print란에다가 계산해서 print해줄거에요
for test_case in range(1, T + 1):
    N = int(input())
    num_lst = list(map(int, input().split()))

    min_num = min(num_lst)
    max_num = max(num_lst)

    print(f'#{test_case} {max_num - min_num}')