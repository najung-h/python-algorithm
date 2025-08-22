import sys
sys.stdin = open('input_1952.txt', 'r')


'''완전탐색으로 풀이하겠습니다. '''
# [1년 이용권 사용수(최대 1), 3개월 이용권 사용 수(최대 4), 1달이용권 사용수(최대 12), 1일 이용권 사용수]
# 각 이용권 금액은 [10, 40, 100, 300]과 같이 plan_for_each_month_lst에 담겨있음
# 
# 







T = int(input())

for test_case in range(1, T+1):
    fee_lst = list(map(int, input().split()))
    
    plan_for_each_month_lst = list(map(int, input().split()))

    



    print(f'#{test_case} ')
