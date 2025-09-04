'''
정사각형 벌통
각 숫자는 각 벌통에 있는 꿀의 양

벌꿀을 채취하여 최대한 많은 수익을 얻으려고 한다.

채취 가능 개수 M 이 주어질 때
두 명의 일꾼,
각각의 일꾼은 가로로 연속되도록 M개의 벌통을 선택하고,
선택한 벌통에서 꿀을 채취하는데
겹치면 안 된 다.

하나의 벌통에서 채취한 꿀은 하나의 용기에 담아야한다.

하나의 벌통에서 꿀을 채취할 때, 일부분만 채취할 수 없고
벌통에 있는 모든 꿀을 한번에 채취해야 한다.
두 일꾼이 채취할 수 있는 꿀의 최대 양은 C이다.

만약 고른 M개의 꿀통들을 더했을 때, 
C를 초과한다면 하나만 선택해서 꿀을 채취해야 한다.

꿀이 팔릴 때 꿀이 많을 수록 상품 가치가 높아서, 
수익 = 꿀의 양 ^ 2이다.

두 일꾼이 꿀을 채취하여 얻을 수 있는 수익 합 최대를 찾아라.
그리고 그때의 최대 수익을 출력하는 프로그램을 작성해라.

(3 ≤ N ≤ 10)
(1 ≤ M ≤ 5 and M <= N)
(10 ≤ C ≤ 30)
하나의 벌통에서 채취할 수 있는 꿀의 양은 1 이상 9 이하의 정수
''' 

# 완전탐색
'''
1. 완전탐색으로 구현할 경우

1번함수 : 첫 번재 일꾼과 두 번째 일꾼이 선택할 모든 조합 찾아주는 함수

2번 함수 : 각 조합에 대해서 수익 계산하는 함수
            -> for 조합 in 전체조합:
                반복문 돌려서 max_수익 찾기

'''
from itertools import combinations
from itertools import combinations_with_replacement
from itertools import product

def special_combinations():
    '''한 행에서 두 번 채취를 하는 경우의 수를 구해주는 함수입니다.
    예외처리는 미리 해두고 진입할거기 때문에 별도 예외처리 없습니다.'''
    for rdx in range(N-M): # 각 행에서 첫번재 col을 먼저 구해주기, 두번재 칼럼을 위해 M만큼 여유는 남겨놔야함.
        for cdx in range(N-M-cdx): # 남은 여유 중에서 간격을 정해보기
            for alpha in range(N-M-cdx):
                return ((rdx, cdx), (rdx,cdx+alpha))




# 1번 함수
'''같은 행에서 두 개를 고르는 경우와, 두 개의 행을 골라서, 그 안에서 들어가는 경우가 있다.'''
def honey_combination():
    '''각 행에 대해 시작점을 다르게 가져갈 수 있음
    뒤로 n개 이상의 벌통을 선택하는 시작점을 리턴하자.'''
    combi_result = []

    # 같은 행에서 두 개 이상을 고를 수 없다면.
    # 행 인덱스는 중복 조합으로
    # 열 인덱스는 중복 순열로 구해서
    # 합치면 됨.
    if M*2 > N:
        # 두 개의 행을 고르고, 그 안에서 조합을 선택하는 경우
        rows = list(combinations(range(3), 2))
        for combi in product(rows, range(N)):
            combi_result.append(combi)
        print('행 두 개 마다 열 하나씩 고르는 경우')
        print(combi_result)

        '''
        temp = []
        for row in rows:
            for col in range(N-1):
                temp.append((row,col))
        return [combinations(temp, 2)]'''

    # 같은 줄에 경우의 수가 두 개 밖에 없는 경우, 딱 들어맞으니까 그냥 단순하게 계산해주기.
    elif M*2 == N:
        for rdx in range(N):
            combi_result.append([(rdx,0), (rdx, M)])

    else:
    
        # 같은 행에서 두 개를 고르는 경우
        for rdx in range(N):
            for cdx in range(N-1):

                '''별도의 함수가 필요해1!!'''

        # 두 개의 행을 고르고, 그 안에서 조합을 선택하는 경우
        rows = list(combinations(range(3), 2))
        for row in rows:
            for col in range(N-1):
                combi_result.append((row,col))
    
    return 



# 2번 함수
'''# 수익이 제곱수
# doubled_profit = (0, 1, 4, 9, 18, 27, 36, 49, 64, 81)
# now_profit = doubled_profit(big_arr[rdx][cdx])
# total_profit += now_profit
'''
# profit = 



import sys
sys.stdin = open('input_2115.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N, M, C = map(int, input().split())
    big_arr = tuple(tuple(map(int, input().split())) for _ in range(N))

    combi_result = []
    if M*2 > N:
        # 두 개의 행을 고르고, 그 안에서 조합을 선택하는 경우
        cases = list(combinations(range(N), 2))
        
        for rows in cases:
            for row in rows:
                print(row)





    print(f'#{tc} ')