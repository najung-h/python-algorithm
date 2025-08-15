import sys
sys.stdin = open('input_11315.txt', 'r')


# 오목의 여부를 오른쪽, 아래쪽, 대각선 오른쪽 아래, 대각선 왼쪽 아래로만 확인하면 된다. 
dr = [0, +1, +1, +1]
dc = [+1, 0, +1, -1]


def find_omok(now_point):
    rdx, cdx = now_point
    for d in range(4):  # 각 방향에 대해서
        for k in range(1, 5):  # 5번 o가 나오는지 검사한다.
            r = rdx + dr[d] * k
            c = cdx + dc[d] * k
            
            if 0<=r<N and 0<=c<N and big_arr[r][c] == 'o':
                pass
            else:
                break
        
        else:  # break되는 일이 없었다면
            return True
    return False





T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    big_arr = [list(input()) for _ in range(N)]
    # [['.', '.', '.', '.', 'o'], ['.', '.', '.', 'o', '.'], ['.', '.', 'o', '.', '.'], ['.', 'o', '.', '.', '.'], ['o', '.', '.', '.', '.']]

    found = False


    for rdx in range(N):
        if found is True:
            break
        for cdx in range(N):
        
            if big_arr[rdx][cdx] == 'o' :
                now_point = (rdx,cdx)
                if find_omok(now_point) is True:
                    found = True
                    break
    
    print(f'#{test_case} ', end='')
    if found is True:
        print('YES')
    
    else: 
        print('NO')
    
                        
                