import sys
sys.stdin = open('input_4880.txt', 'r')


# 문제에서 말을 1번 2번 사람 이렇게 해서
# 인덱스 기준이 아니고, 자연어 기준인가 헷갈렸는데
# 인덱스 기준이 맞습니다.
# 그래서 큐가 써지네요


from collections import deque





big_arr = []
def making_tournament(arr):
    tournament_lst = []
    tournament_lst
    # 

    return making_tournament(tournament_lst)

def lets_do_gawe_bawe_bo(a,b):
    '''
    가위바위보의 승자를 리턴합니다.

    1==가위, 2==바위, 3==보
    비기는 경우, 앞에 사람이 이긴다
    1 > 3
    2 > 1
    3 > 2
    '''
    # 동점이면 앞 사람이 승자
    if a == b:
        return a
    
    # 그 외
    elif a == 1 and b == 3:
        return a
    elif a == 1 and b == 2:
        return b
    
    elif a == 2 and b == 1:
        return a
    elif a == 2 and b == 3:
        return b
    
    elif a == 3 and b == 1:
        return b
    elif a == 3 and b == 2:
        return a





T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    card_lst = list(map(int, input().split()))

    # 일단은 큐에다가 사람들을 다 넣겠습니다.
    people = deque()
    for i in range(1, N+1):
        people.append(i)
    
    # 앞에 두 명을 빼서 승자를 가리고, 승자는 가장 뒤에 다시 넣겠습니다.
    # 단, 홀수 개라면, 마지막 원소는 단순히 빼서 다시 뒤에 넣겠습니다. 
    
    while True:
        new_people = deque()

        if len(people) == 1:
            return people.popleft()
        a = people.popleft()
        b = people.popleft()

        new_people.append(lets_do_gawe_bawe_bo(a,b))
        
        



    '''# 패딩이 총 N //2 만큼 들어가게 된다
    while people.count('_') < N//2:
        if N / 2 == N//2 : 
            people.insert(N//2, '_')

        pass'''


    


    print('#{test_case} ')
