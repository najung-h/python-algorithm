import sys
sys.stdin = open('input_1952.txt', 'r')


'''완전탐색으로 풀이하겠습니다. '''
# [1년 이용권 사용수(최대 1), 3개월 이용권 사용 수(최대 4), 1달이용권 사용수(최대 12), 1일 이용권 사용수]
# 각 이용권 금액은 [10, 40, 100, 300]과 같이 plan_for_each_month_lst에 담겨있음
# 최대 [1, 4, 12, 31] # 가중치 [365, 91.36, 30.49, 1 ]

max_lst = [1, 4, 12, 31]
weight =  [365, 91.35, 30.48, 1 ]




def all_cases_of_fee_plan(fee_lst, plan_for_each_month_lst):
    cost_1year = fee_lst[3]
    best_cost = cost_1year # 쌀수록 이득 # 초기값은 1년권
    best_case = tuple()

    for year_1 in range(max_lst[0] + 1):
        for month_3 in range(max_lst[1] + 1): 
            for month_1 in range(max_lst[2] + 1): 
                for day1 in range(max_lst[3] + 1):  
                    day_sum =  year_1  * weight[0] + month_3 * weight[1] + month_1 * weight[2] + day1  * weight[3]
                    
                    if day_sum < 365:
                        continue

                    cost = year_1 * fee_lst[3] + month_3 * fee_lst[2] + month_1 * fee_lst[1] + day1 * fee_lst[0]

                    if cost < best_cost:
                        best_cost = cost # 갱신
                        best_case = (year_1, month_3,month_1, day1) 
    
    return best_cost





T = int(input())

for test_case in range(1, T+1):
    fee_lst = list(map(int, input().split()))
    
    plan_for_each_month_lst = list(map(int, input().split()))

    '''
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
    cost_3month = fee_lst[2] * 4
    print('3개월권으로 죄다 이용했을 때 : ', cost_3month)

    # 1년권으로 이용했을 때의 금액
    cost_1year = fee_lst[3]
    print('1년권으로 이용했을 때의 금액 : ', cost_1year)
    '''
    
    best_cost = all_cases_of_fee_plan(fee_lst, plan_for_each_month_lst)




    print(f'#{test_case} {best_cost}')
