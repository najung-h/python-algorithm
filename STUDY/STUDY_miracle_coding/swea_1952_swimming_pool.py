import sys
sys.stdin = open('input_1952.txt', 'r')


'''완전탐색으로 풀이하겠습니다. '''
# [1년 이용권 사용수(최대 1), 3개월 이용권 사용 수(최대 4), 1달이용권 사용수(최대 12), 1일 이용권 사용수]
# 각 이용권 금액은 [10, 40, 100, 300]과 같이 plan_for_each_month_lst에 담겨있음
# 




T = int(input())

for test_case in range(1, T+1):
    fee_lst = list(map(int, input().split()))
    
    plan_for_each_month_lst = list(map(int, input().split()))

    # 금액 가격 리스트
    print('차례대로 1일권, 1개월 권, 3개월 권, 1년권의 가격은 ', fee_lst, '입니다.')
    # 죄다 1일권으로 이용했을 때의 금액
    cost_day = fee_lst[0] * sum(plan_for_each_month_lst)
    print('1일권으로 죄다 이용했을 때 : ', cost_day)

    # 죄다 1개월 권으로 이용했을 때의 금액
    # 각 달마다 0이 아닌 경우만 구매
    cost_1month = fee_lst[1] * (12 - plan_for_each_month_lst.count(0))
    print('1개월 권으로 죄다 이용했을 때 : ', cost_1month)

    # 죄다 3개월 권으로 이용했을 때의 금액
    

    # 1년권으로 이용했을 때의 금액
    cost_1year = fee_lst[3]
    print('1년권으로 이용했을 때의 금액 : ', cost_1year)
    

    ###
    #


    print(f'#{test_case} ')
