import sys
sys.stdin = open('input_1966.txt', 'r')

T = int(input())

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




for test_case in range(1, T+1):

    N = int(input())    # 5<= N <= 50

    num_lst = list(map(int,input().split()))
    final_lst = []

    for _ in range(N):
        num_lst = put_min(num_lst)
        final_lst.append(num_lst[0])
        num_lst = num_lst[1:]


    print(f"#{test_case} ", end = '')

    for i in final_lst[:N-1]:
        print(i, end = ' ')

    print(final_lst[N-1])