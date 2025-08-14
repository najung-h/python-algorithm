import sys
sys.stdin = open('input_5189.txt', 'r')


from itertools import permutations


T = int(input())

for test_case in range(1, T+1):

    # 완전탐색으로 구현하겠습니다.
    # 시작점과 마무리점을 1로 고정하고
    # 그 사이에 들리는 경로는 (N-1)! 개입니다.
    #

    N = int(input())
    
    big_arr = [list(map(int, input().split())) for _ in range(N)] 
    # [[0, 18, 34], [48, 0, 55], [18, 7, 0]]

    # 2부터 N까지 숫자가 담긴 리스트 생성하고
    N_minus_1_num_lst_for_iterable_object = [i+2 for i in range(N-1)]        # [2, 3]
    # 그 리스트에서 순열 돌리기.
    charge_cases_lst = list(permutations(N_minus_1_num_lst_for_iterable_object, N-1))  # [(2, 3), (3, 2)]

    for case in charge_cases_lst:
        (1,3)





    print(f"#{test_case} ")