b, a = map(int, input().split())
big_arr = [list(map(int, input().split())) for _ in range(b)]

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

# 어떤 숫자가 1일 때, 그 사방이 1이라면 안 녹음
# 어떤 숫자가 1인데 사방에 0이 하나라도 있으면 녹음


time = 0

while True:
    time += 1
    num_of_cheese = sum([sum(row) for row in big_arr])
    # if num_of_cheese == 0:
    #     break
    
    # 녹을 치즈 개수 초기화
    num_of_melting_cheese = 0
    
    # 치즈 녹는 위치 초기화 및 저장
    # 시간복잡도를 위해 즉각적으로 0으로 바꿀 건데, 
    # 남은 애들의 정보가 달라질 수 있어서 예외처리할 예정
    location_of_melting_cheese_set = set()
    
    # 전체 2차원 배열에 대해
    for r in range(b):
        for c in range(a):
            # 치즈라면
            if big_arr[r][c] == 1:
                # 주변 사방을 봤을 때 0이 하나라도 있으면 녹는다
                """## -> fail, 안쪽에 있는 공기는 의미 없다.
                ### 사전에  안쪽 공기는 2 로 처리하자. 
                #### 아니 근데 안쪽 공기인지 구분하려면 결국 bfs 해야함.
                ##### 시간복잡도가 에반데
                ###### 이거 그냥 녹이는 것도 bfs 일텐데
                ####### 어떻게 해야할지 모르겠네 큰일"""
                for d in range(4):
                    nr = r + dr[d]
                    nc = c + dc[d]
                    if nr < b and nr >=0 and nc < a and nc>=0 and big_arr[nr][nc] == 0 and (nr, nc) not in location_of_melting_cheese_set:
                        num_of_melting_cheese += 1
                        big_arr[r][c] = 0
                        location_of_melting_cheese_set.add((r, c))
                        # 탐색 멈춰
                        break
                
    num_of_cheese = sum([sum(row) for row in big_arr])
    if num_of_cheese == 0:
        final_answer = num_of_melting_cheese
        break #while문
  
  
print(time)      
print(final_answer)

