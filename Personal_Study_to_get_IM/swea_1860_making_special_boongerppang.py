import sys
sys.stdin = open('input_1860.txt', 'r')

# 진기의 특별한 붕어빵 만들기
'''(기각)스택으로 풀자.
    각 시간에 대해 
    빵 만들어졌으면 push
    빵 찾으러 왔으면 pop
    pop 못 하면 Impossible
    각 시간에 대해 푸니까 시간 복잡도가 클라나'''

'''(채택) 그러면, 모든 시간을 돌지 말고, set으로 만들고,
    set의 원소에 대해서만 돌자. 
    그리고 하나 더, 각 시간에 오는 사람들을 count해서 dic를 만들고
    그 딕셔너리를 기준으로 확인하자'''


T = int(input())
#T = 1

for test_case in range(1, T+1):
    N, M, K = list(map(int, input().split()))
    arrival_time_lst = list(map(int, input().split())) 
    #print(f'{N}명의 사람이 오는데요, {M}초의 시간을 들이면 {K}개의 붕어빵 만들 수 있어요!')
    #print(f'도착시간은 차례대로 {arrival_time}이에요!')
    # 0<= 도착시간 < 11,111

    result = 'Possible' # Impossible


    # 1. 도착 시간 내 중복값 제거 및 빨리 오는 사람부터 나열

    arrival_time_set = set(arrival_time_lst)
    # set은 순서를 보장해주지 않으므로, list로 다시 변환하면서
    # # [59, 60, 61] 빨리 오는 사람의 시간부터 나열
    real_arrival_time_lst = sorted(list(arrival_time_set))   


    # 2. 몇초에 몇 명 픽업오는지를 딕셔너리로 제작
    bread_pickup_time_dic = {}   # 몇몇 초 : 몇 명
    for time in real_arrival_time_lst:  
        bread_pickup_time_dic[time] = arrival_time_lst.count(time)
    #print(bread_pickup_time_dic)  # {59: 28, 60: 23, 61: 23}


    # 3. 빨리 오는 사람부터 차례대로 확인
    # 그 시간에 몇 명이 오는데 만들어진 붕어빵 보다 작지 않은지 확인
    maken_bread = 0
    previous_time = 0

    for time in real_arrival_time_lst:     # 빨리 오는 사람부터 확인
        maken_bread += (time // M - previous_time // M) * K  # 만들어져있는 붕어빵
        #print(f'{time}초에 만들어진 빵은 {maken_bread}개인데, {bread_pickup_time_dic.get(time)}명이 픽업왔어요!')
        people_num = bread_pickup_time_dic.get(time)
        if people_num > maken_bread: # 몇 명 오는지 < 만들어진 붕어빵
            result = 'Impossible'
            #print('불가능해요!')
            break
        else : #붕어빵 찾아간만큼 빼줍시다.
            #print('가능해요')
            maken_bread -= people_num
            previous_time = time

    

    print(f'#{test_case} {result}')
