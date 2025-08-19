import sys
sys.stdin = open('input_1220.txt', 'r')

'''
빨간색은 아래로 가고
파란색은 위로 가는데
성공하면 교착 상태가 아닌거고

그 외에 방해꾼들이 있다면, 
즉, 빨간색이면 아래로 가야하는데, 아래 파랭이가 있어서 교착 상태
    파란색이면 위로 가야하는데, 내 위에 빨강이가 있어. 이런 경우
요러면 교착 상태

그러면, 전체 자석의 개수에서 - 성공한 애들의 개수를  빼주면
되겠는데
윗줄부터 파란색인데 내 위에 머가 없다면 성공시키는 코드랑
아랫줄부터 시작해서 빨간색인데 내 아래에 뭐가 없다면 성공시키는 코드
<- 함수로 두 번 쓰기

'''


T = 10

for test_case in range(1, T+1):
    N = int(input())  # 100

    big_arr = [list(map(int, input().split())) for _ in range(100)]
    #print(big_arr)
    # 1 == N극 == 빨강이
    # 2 == S극 == 파랭이
    impossible_up_col = []   # 위쪽으로 못 나가는 열
    impossible_down_col = []
    go_out_num = 0  # 탈출한 애들의 수


    total_magnet = 0

    # 1. 위에 방향으로 못 나가는 리스트 만들면서, 그 리스트에 없으면 탈출시켜주기
    for rdx in range(100):
        for cdx in range(100):
            if big_arr[rdx][cdx] == 1: # 빨강이라면
                impossible_up_col.append(cdx)
                total_magnet += 1
                
            elif big_arr[rdx][cdx] == 2: # 파랑이라면
                if cdx not in impossible_up_col:
                    big_arr[rdx][cdx] = 0 # 탈출
                    go_out_num += 1
                    total_magnet += 1

    # 열 방향으로 순환하려면 시간 복잡도가 줄어들 것 같앗는데
    # 어차피 전체 자석이 몇 갠지 세어야 해서...        
    '''for cdx in range(100):
        for rdx in range(100):
            if big_arr[rdx][cdx] == 1:
                impossible_up_col.append(cdx)
                break
    
            elif big_arr[rdx][cdx] == 2:
                if cdx not in impossible_up_col:
                    big_arr[rdx][cdx] = 0
                    go_out_num += 1'''


    


    # 2. 아래 방향으로 못 나가는 리스트 만들면서, 그 리스트에 없으면 탈출시켜주기
    # 단, 아래줄부터 수행
    for rdx in range(99,-1, -1):
        for cdx in range(100):
            if big_arr[rdx][cdx] == 2: # 파랑이라면
                impossible_down_col.append(cdx)

            elif big_arr[rdx][cdx] == 1:# 빨강이라면
                if cdx not in impossible_down_col:
                    big_arr[rdx][cdx] = 0 # 탈출
                    go_out_num += 1

    print(total_magnet)
    print(go_out_num)
    print(f'#{test_case} {total_magnet - go_out_num}')
