import sys
sys.stdin = open('input_10804.txt', 'r')

T = int(input())


def mirror_test(lst):
    for idx in range(len(lst)):
        if lst[idx] == 'b' :  lst[idx] = 'd'
        elif lst[idx] == 'd' : lst[idx] = 'b'
        elif lst[idx] == 'p' : lst[idx] = 'q'
        else: lst[idx] = 'p'
    return lst


for test_case in range(1, T+1):
    lst = list(input())
    print(f'#{test_case} {"".join(mirror_test(lst)[::-1])}')


