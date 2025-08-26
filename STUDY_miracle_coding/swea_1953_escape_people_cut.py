import sys
sys.stdin = open('input_1953.txt' , 'r')


'''# 터널 종류에 따라 델타 탐색이 가능한 dr, dc 리스트를 바꾸자

# 이후, for time in range(1, n+1):
if 못 가 :
    break
else:



# dr, dc 탐색함수를 구현해서 재귀적으로 탐색을 진행한다.

# went_point가 아니고, 델타 범위라면 이동하면서, went_point에 추가
'''

# 터널 종류에 따라 델타 탐색이 가능한 dr, dc 리스트를 바꾸자
def turnel_delta_lst(turnel):
    if turnel ==1:
        dr = [+1, -1, 0, 0] # 상하 좌우
        dc = [0, 0, -1, +1] 
        
    elif turnel == 2 :
        dr = [+1, -1] # 상하 좌우
        dc = [0, 0] 

    elif turnel == 3 :
        dr = [0, 0] # 상하 좌우
        dc = [-1, +1] 
        
    elif turnel == 4 :
        dr = [+1,  0] # 상하 좌우
        dc = [0, +1] 
        
    elif turnel == 5 :
        dr = [ -1, 0] # 상하 좌우
        dc = [ 0,  +1] 

    elif turnel == 6:
        dr = [-1, 0] # 상하 좌우
        dc = [0, -1] 
    
    elif turnel == 7:
        dr = [+1,  0] # 상하 좌우
        dc = [0, -1]     
    
    return (dr, dc) 


# 이후, for time in range(1, L+1):

def find_(M, N, C, R, L, dr, dc, went_set):
    rdx = R
    cdx = C

    
    
    for time in range(1, L+1):
        
        for d in range(len(dr)):
            r = rdx + dr[d]
            c = cdx + dc[d]
            
            
            if (r,c) not in went_set :
                rdx, cdx = r, c
                went_set.add((r,c))
                find_(M, N, c, r, L-time, *turnel_delta_lst(big_arr[r][c]), went_set)
            else:
                continue
        
    return len(went_set)



# dr, dc 탐색함수를 구현해서 재귀적으로 탐색을 진행한다.

# went_point가 아니고, 델타 범위라면 이동하면서, went_point에 추가


T = int(input())
for tc in range(1, T+1):
    N, M, R, C, L = list(map(int, input().split()))
    big_arr = [list(map(int, input().split()))  for _ in range(N)] 
    
    '''print(f'터널은 {N} * {M}의 크기이고, \
          \n 멘홀 뚜껑이 위치한 장소의 위치는 ({R}, {C})이며, \
          \n탈출 후 소요된 시간은 {L}이다.')'''
    
    #print(big_arr)
    '''숫자 0은 터널이 없는 장소, 수자 1-7은 해당 위치의 터널 구조물 타입'''
    
    dr, dc = turnel_delta_lst(big_arr[R][C])
    went_set = set((R,C))
    print(find_(M, N, C, R, L, dr, dc, went_set))