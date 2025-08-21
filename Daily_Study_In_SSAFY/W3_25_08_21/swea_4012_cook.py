import sys
sys.stdin = open('input_4012.txt', 'r')


'''완전탐색으로 구현해보겠습니다.'''

from itertools import combinations


T = int(input())


for test_case in range(1, T+1):
    # 인풋 받아옵시다.
    N = int(input())
    #print(f'재료는 {N}개에요')
    big_arr = [list(map(int,input().split())) for _ in range(N)]

    index_ = [0] * N
    for i in range(N):
        index_[i] = i
    # #print(index_) #[0, 1, 2, 3]


    arr = list(combinations(index_, N//2))
    #print(arr) # 4c2개가 들어옴 # [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]

    min_synergy_diff = 999999999999999

    for food_cooking_case in (arr):
        # 각 경우의 수에 대해서 idx번째 경우를 데려옵니다. 예시 (0,1)
        # 각 요리
        synergy = 0
        synergy_b = 0
        for rdx in range(N):
            for cdx in range(N):
                if (rdx in food_cooking_case) and (cdx in food_cooking_case): # 그 요리 할거야
                    # 시너지 계산해
                    synergy += big_arr[rdx][cdx]

                elif (rdx not in food_cooking_case) and (cdx not in food_cooking_case): # 그 요리 할거야
                    # 시너지 계산해
                    synergy_b += big_arr[rdx][cdx]
        
        #print(f'{food_cooking_case}조합을 요리했더니 A요리는 맛이{synergy}가 났어요.')
        #print(f'{food_cooking_case}조합을 요리했더니 B요리는 맛이{synergy_b}가 났어요.')

        synergy_diff = abs(synergy - synergy_b)
        #print(f'두 음식간 맛의 차이는 {synergy_diff}에요')

        if synergy_diff < min_synergy_diff:
            min_synergy_diff = synergy_diff
            max_food = food_cooking_case
            #print(f'{max_food}조합을 요리했더니 {min_synergy_diff}가 났어요.')




    print(f'#{test_case} {min_synergy_diff}')

'''gpt의 코드리뷰

1) 멤버십 검사는 tuple이 아니라 set에서 수행해야 간단하다.
멤버십 검사가 필요하면 set을 써서 O(1)로.

2) rdx, cdx는 전체 N * N으로 돌릴 필요가 없다.
그룹 내 쌍만 돌리고, 맛은 S[i][j] + S[j+i]로 한번에 계산해라

3) 중복 케이스 (A,B)와 (B,A)를 둘 다 탐색할 필요가 없다.
이를 개선하기 위해서, 항상 0번 재료를 A에 포함시키면, 
(A,B)만 보게 되어 탐색량이 절반으로 줄어든게 된다.


4) 9999999999999 말고, float('inf')가 가독성이 좋다.



'''