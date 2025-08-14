import sys
sys.stdin = open('input_4865.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    str1 = list(input())
    set1 = set(str1)
    str2 = input()

    max_cnt = 0

    for s in set1:
        cnt = str2.count(s)
        if cnt > max_cnt:
            max_cnt = cnt
            max_s = s


    print(f"#{test_case} {max_cnt}")

