#import sys
#sys.stdin = open("input2.txt", "r")

T = int(input())

for test_case in range(1, T+1):
    N = int(input())

    num_of_boxes_on_each_floor = list(map(int, input().split()))
    # print(num_of_boxes_on_each_floor)
    # [7, 4, 2, 0, 0, 6, 0, 7, 0]

    # 무조건 가장 왼쪽에 있는 열(뒤집기 전)의 낙차가 제일 클 수 밖에 없지...는 않음
    # 반례 ) 363333

    falling = 0      # 낙차 # 초기값
    max_falling = 0  # 최대낙차 # 초기값

    idx = 0   # idx번째 열(0부터 시작)
    for col in num_of_boxes_on_each_floor:

        # 각각 최고층에 대해서만 테스트하면 됨. (윗행)
        # 아래층이 있어야 윗층이 있기 때문에
        # 무조건 윗층이 낙차가 가장 큼, 그 열에 한해서는

        test_lst = num_of_boxes_on_each_floor[idx+1:] # 그 다음에 있는 블럭빌딩들에 대해
        # col이 7층이라면, 7,8, 9층 다 찾아야함.
        # -> 최고층과의 차이만큼 count를 반복해줘야해
        count = 0  # count 초기화
        # difference_btw_toppest_floor_n_col = N  - col

        for _ in range(col, N+1):
            # print(count)
            count += test_lst.count(_)


        # 아래에 count개가 있었다면,
        falling = N - idx - 1 - count
        # print(falling)
        if falling > max_falling:
            max_falling = falling


    print(f'#{test_case} {max_falling}')