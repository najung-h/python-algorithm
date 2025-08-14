T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
 
amount = 0
 
for test_case in range(1, T + 1):
    big_list = []# 칠할 모든 색상들이 모여있는 가장 큰 리스트
 
    area_num = int(input())
    for i in range(area_num):
        big_list.append(list(map(int, input().split())))  #len(big_list) = num = 첫번째 입력값
     
    #print(big_list)
     
     
    # 빅 리스트의 원소 각각(한 줄)에 대해서 색상 영역에 대한 정보를 옮겨담자.
    color_1 = []
    color_2 = []
         
    for n in big_list:
        # input 한 줄 한 방에 처리하는 반복문
         
        # 각각의 컬리스트에다가 치워야하는 모든 칸에 대한 정보를 옮겨담은 예정
        start_x = n[0]
        start_y = n[1]
        end_x = n[2]
        end_y = n[3]
        color = int(n[4])
         
        #print(start_x, start_y, end_x, end_y, color)
         
        # 빨간색이면 ?
        if color == 1:
            for x in range(start_x, end_x+1):
                for y in range(start_y, end_y +1):
                    color_1.append((x,y))
                     
         
 
        # 파란색이면?       
        if color == 2:
            for x in range(start_x, end_x+1):
                for y in range(start_y, end_y +1):
                    color_2.append((x,y))
                     
        #print(color_1)
        # [(2, 2), (2, 3), (2, 4), (3, 2), (3, 3), (3, 4), (4, 2), (4, 3), (4, 4)] 
    
    #####3
    # 완성된 color_1 과 color_2 비교하자
    amount = 0
     
    for i in color_1:
        if i in color_2:
            amount += 1
         
    print(f'#{test_case} {amount}')