import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    # 카드를 여기다가 받아올게요
    num_lst = list(map(int, input()))
    # print(num_lst)    # [4, 9, 6, 7, 9]

    # 중복된 카드를 제거하기 위해서 set로 형변환시키겠습니다.
    num_set = set(num_lst)

    # 이제 set의 각 원소에 대해서, 개수를 센다음에
    num_count_lst = []
    # num_count_lst에다가 (숫자, 개수) 형태로 append 하겠습니다.

    for num in num_set:
        count = num_lst.count(num)
        num_count_lst.append((num,count))
    # print(num_count_lst)    # [(4, 1), (9, 2), (6, 1), (7, 1)]

    # maximum_count 값은 매번 0으로 초기화시켜두고 시작합니다.
    maximum_count = 0

    # 아래 반복문은 ,
    # 각각의 count값에 대해서 maximum_count보다 크다면
    # 걔를 maximum_count로, 걔의 넘버를 maximum_num으로 지정하겠습니다.
    for a, b in num_count_lst:
        if b > maximum_count and a is not 0:  # is not 0 안 쓰면, 0을 maximum num으로 지정하게 됩니다.
            maximum_num = a
            maximum_count = b

    print(f'#{test_case} {maximum_num} {maximum_count}')

