big_arr = [list(map(int, input().split())) for _ in range(9)]

# transpose 어떻게 하더라 망했다
'''
for r in range(9):
    for c in range(9):
        # 빈 칸이면 
        if big_arr[r][c] == 0: 
            '''
            
# 일차원으로 접근하자.
# 같은 열이면 mod9일때 같은 값일거고
# 같은 행이면 정수나눗셈 결과가 같을거임.


# 일차원으로는 어떻게 받지 ?? 큰일났네

arr = []
for row in big_arr:
    for col in row:
        arr.append(col)
    
# print(arr)

number_set = {1, 2, 3, 4, 5, 6, 7, 8, 9}


# 박스 찾기 함수
def find_box(index):
    # 행 / 열 단위로 분류
    row_index = index // 9
    col_index = index % 9
    
    # 3 * 3으로 분류해서 
    # 박스의 좌상단 값 추출
    r0 = (row_index // 3) * 3  # 0인지 3인지 6인지 결정 # 나머지 값 제거
    c0 = (col_index // 3) * 3  # 0 인지 3인지 6인지
    
    box_set = set()
    for r in range(r0, r0 + 3):
        for c in range(c0, c0+3):
            now_index = r * 9 + c  # 일차원 리스트에서의 인덱스값 반환
            box_set.add(now_index)
    
    return box_set


# 종료조건
is_not_finished = True

while is_not_finished:
    # 종료조건 초기화 : 0있는지 확인
    is_not_finished = False
    
    for index, number in enumerate(arr):
        # 빈 칸이라면
        if number == 0:
            # is_not_finished = True # 시간 초과
            row_index = index // 9
            col_index = index % 9
            # print(f'{row_index+1}행 {col_index+1}열 확인하고 있어요')
            same_row = set([9*row_index + k for k in range(9)])
            same_col = set([9*k + col_index for k in range(9)])
            # 아니 클났네. 가로 세로가 아니라 박스도 있었네.
            same_box = find_box(index)
            
            non_candidate_set_index = same_box.union(same_row.union(same_col))
            non_candidate_set = {arr[i] for i in non_candidate_set_index}
            
            candidate_set = number_set - non_candidate_set
            # print(f'나온 숫자: {non_candidate_set}')
            # print(f'남은 후보: {candidate_set}')
            
            if len(candidate_set) == 1:
                arr[index] = list(candidate_set)[0]
                # is_not_finished = True # 틀렸습니다.
                # print(f'{row_index+1}행 {col_index+1}열을 {arr[index]}로 채웠어요')
                
                
# 2차원 복귀
result = []
for k in range(9):
    result.append(arr[k * 9 : (k+1) * 9])
    
for row in result:
    print(' '.join(map(str, row)))


''' 

찍어보는 접근이 필요한 것 같은데
그거 어떻게 구현할지 모르겠어요. 
bfs 인가 이게

'''