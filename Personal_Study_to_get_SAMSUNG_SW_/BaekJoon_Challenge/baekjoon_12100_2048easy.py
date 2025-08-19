import sys
sys.stdin = open('input_b_12100.txt', 'r')

# 보드의 크기
N = int(input())

big_arr = [list(map(int, input().split())) for _ in range(N)]

print(big_arr)

'''


'''

for rdx in range(N):
    for cdx in range(N):
        