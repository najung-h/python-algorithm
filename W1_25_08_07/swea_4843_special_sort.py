import sys
sys.stdin = open("input_4843.txt", "r")


import sys
sys.stdin = open("input_4843.txt", "r")


def put_min(lst):
    min_ele = lst[0]
    min_idx = 0

    result_lst = []        # 최솟값이 아닌 애들을 담을 리스트

    for idx, i in enumerate(lst):
        if i < min_ele:
            min_ele = i
            min_idx = idx
        
    for idx in range(len(lst)):
        if idx == min_idx:
            pass
        else:
            result_lst.append(lst[idx])

    return [min_ele] + result_lst

def put_max(lst):
    max_ele = lst[0]
    max_idx = 0

    result_lst = []         # 최댓값이 아닌 애들을 담을 리스트

    for idx, i in enumerate(lst):
        if i > max_ele:
            max_ele = i
            max_idx = idx
        
    for idx in range(len(lst)):
        if idx == max_idx:
            pass
        else:
            result_lst.append(lst[idx])

    return [max_ele] + result_lst









T = int(input())
for test_case in range(1, T + 1):
    N = int(input())

    integer_lst = list(map(int, input().split()))
    #print(integer_lst)

    final_lst = []
    lenn = len(integer_lst)

    for idx in range(lenn -1):
        if idx%2 == 0:
            a = put_max(integer_lst)
            final_lst.append(a[0])
            integer_lst = a[1:]

        else: 
            a = put_min(integer_lst)
            final_lst.append(a[0])
            integer_lst = a[1:]

    final_lst.append(integer_lst[0])    # 마지막 남은애까지 추가

    #print(final_lst)

    print(f'#{test_case} ', end='')
    for i in final_lst[:9]:
        print(i, end=' ')
    print(final_lst[9])


