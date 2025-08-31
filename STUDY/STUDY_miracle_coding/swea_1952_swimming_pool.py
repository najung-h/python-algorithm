import sys
sys.stdin = open('input_1952.txt', 'r')


'''완전탐색으로 풀이하겠습니다. '''
'''완전탐색 포기합니다.
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
    
    return best_cost'''

from itertools import combinations



def total_cost(buy_plan_lst):
    '''최종 이용 플랜이 나왔을 때
    그 비용을 계산해주는 함수
    단 1년권은 제외한다.'''
    total_cost = 0
    for mdx in range(12):
        if buy_plan_lst[mdx] == '1일권':
            total_cost += plan_for_each_month_lst[mdx] * fee_lst[0]
        
        elif buy_plan_lst[mdx] == '1달권':
            total_cost += fee_lst[1]
        
        elif buy_plan_lst[mdx] == '3달권':
            total_cost += fee_lst[2]
    
    return total_cost
            
def money():
    # 각각의 달에 대해서, 1일권 vs 1달권을 결정한다.
    # 1달권을 쓰는 달이 3개월 내 2개 이상이라면 1달권 vs 3달권을 결정한다.
    # 이 시점의 가격과 1년권의 가격을  비교하여 최종 결정한다.
    
    for month in range(12):
        
        # 이용계획이 없다면
        if plan_for_each_month_lst[month] == 0 :
            buy_plan_lst[month] = '안사'
            
        elif plan_for_each_month_lst[month] * fee_lst[0] < fee_lst[1]:
            buy_plan_lst[month] = '1일권'
        
        else:
            buy_plan_lst[month] = '1달권'
            
    hubo_lst = []
    for month in range(10):
        # 3달 안에 1개월 권을 두 번 이상 쓰는 경우가 있다면 
        # 일단 후보에 두자.
        
        if buy_plan_lst[month:month+3].count('1달권') >= 2:
            hubo_lst.append(month)
            
    if len(hubo_lst) == 0 : # 3개월 권 안 써도 됨 
        # 그럼 이젠 구매 계획 다 나왔으니까, 마지막으로 1년권이랑 비교만 하면 됨
        result = total_cost(buy_plan_lst)
        if result > fee_lst[3]:
            result = fee_lst[3]
        return result
    
    elif len(hubo_lst) ==1:
        buy_plan_lst[hubo_lst[0]] = '3달권'
        buy_plan_lst[hubo_lst[0]+1] = None     
        buy_plan_lst[hubo_lst[0]+2] = None
        
        result = total_cost(buy_plan_lst)
        if result > fee_lst[3]:
            result = fee_lst[3]
        return result
    
    
    # 겹치는 애들이 있다면 3개월 구매 예상 리스트
    # 단, 1월 2월 3월이 모두 담겨있을 수 있으니까.
    # 이 경우 어느 경우가 최적인지 계산해줘야함.
    
    
    else:
        # 겹치는 애들이 있는지 확인
        for a,b in combinations(hubo_lst, 2):
            if abs(a-b) == 1:
                hubo_set = set(hubo_lst)
                hubo_set.difference_update({a, b})

                
                plan_a, plan_b = buy_plan_lst[:], buy_plan_lst[:]
                plan_a[a] = '3달권'
                plan_a[a+1] = None
                plan_a[a+2] = None
                
                plan_b[b] = '3달권'
                plan_b[b+1] = None
                plan_b[b+2] = None
                
                if total_cost(plan_a) > total_cost(plan_b):
                    plan = plan_b
                else:
                    plan = plan_a
                    
                for hubo in hubo_set:
                    plan[hubo] = '3달권'
                    plan[hubo+1] = None     
                    plan[hubo+2] = None
        
        result = total_cost(plan)
        if result > fee_lst[3]:
            result = fee_lst[3]
        return result
               
            
        
            
        




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
    
    '''best_cost = all_cases_of_fee_plan(fee_lst, plan_for_each_month_lst)'''

    buy_plan_lst = [None] * 12
    result = money()

    print(f'#{test_case} {result}')
