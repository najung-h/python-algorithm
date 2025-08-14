# 5432. 쇠막대기 자르기

import sys
sys.stdin = open('input_5432.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    my_str = input()
    
    old_lst = []
        # [0, 5, 7, 11, 14, 19]
        # [1, 6, 8, 12, 15, 20]

    new_lst = []
        # [4, 10, 18]
        # [9, 13, 21]

    laser_lst = []

    for idx, i in enumerate(my_str):
        if i == '(' and my_str[idx+1] == ')':
            old_lst.append(idx) # 레이저와 연관된 애들
            old_lst.append(idx+1)
            laser_lst.append(idx)
            laser_lst.append(idx+1)

    #print(old_lst)
    trying = 0
    stick = 0

    while len(new_lst) + len(old_lst) < len(my_str) and trying<1000:
        trying += 1
        old_lst.extend(new_lst)
        new_lst = []

        try: 
            for idx, i in enumerate(old_lst):   ###############짝수번째 인덱스만
                if idx%2==0 and i != 0 and my_str[i-1] == '(' and i-1 not in old_lst:
                    new_lst.append(i-1)
                    #print(i-1, end=' + ')
                    for jdx, j in enumerate(my_str):
                        if jdx > i and j == ')' and jdx not in old_lst:
                            new_lst.append(jdx)
                            stick += 1
                            #print(jdx, end=' + ')
                            break

            
            
            '''
            for i in new_lst:
                if i != 0 and my_str[i-1] == '(':
                    new_lst.append(i-1)
                    for jdx, j in enumerate(my_str):
                        if jdx > i and j == ')' and jdx not in old_lst and jdx not in first_laser_end_lst:
                            second_laser_end_lst.append(jdx)
                            break'''

        
            #print('old')
            #print(old_lst)
            #print('new')
            #print(new_lst)

            #stick += len(new_lst//2)

        except:
            #print('error')
            pass
        
        #print(laser_lst)
        for idx in range(len(new_lst)//2):
            for j in range(new_lst[idx*2], new_lst[idx*2+1]):
                #print(j, end='   ')
                
                if j in laser_lst:
                    stick += 0.5
            
    print(f"#{test_case} {int(stick)}")



    '''test_case 1의 경우
        old
        [0, 1, 5, 6, 7, 8, 11, 12, 14, 15, 19, 20]
        new
        [4, 9, 10, 13, 18, 21]
        old
        [0, 1, 5, 6, 7, 8, 11, 12, 14, 15, 19, 20, 4, 9, 10, 13, 18, 21]
        new
        [3, 16]
        old
        [0, 1, 5, 6, 7, 8, 11, 12, 14, 15, 19, 20, 4, 9, 10, 13, 18, 21, 3, 16]
        new
        [2, 17]
        '''

        #laser_lst =  [0, 1, 5, 6, 7, 8, 11, 12, 14, 15, 19, 20]


        ### 시간 복잡도 커짐

        ## 이게 중첩돼서 O(n²)에 가까워집니다.
        ## 케이스에 따라 n=100,000이면 절대 시간 안 나올 수도 있어요.