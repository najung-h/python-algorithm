import sys
sys.stdin = open('input_subset.txt', 'r')
import copy

T = int(input())

for test_case in range(1, T+1):
    integer_lst = list(map(int,input().split()))

    subset_lst = []
    subset_1 = [0] * 10
    subset_2 = copy.deepcopy(subset_1)
    #print(subset_1)


    for idx, i in enumerate(subset_1):
        subset_2[idx] = 1
        subset_lst.append(subset_2)

    print(subset_lst)
