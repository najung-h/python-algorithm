import sys
sys.stdin = open('input_1979.txt', 'r')

T = int(input())
result = 0

def find_one_for_each_row(row):
    find_one = 0
    cnt = 0             # 각 행마다, 연속한 1의 개수를 찾겠습니다.
    row.append(0)   # 마지막에 0으로 넣어서, find_one의 개수 정확하게

    for col in row:
        if col == 1:    # 1이라면, 
            cnt += 1    # cnt 늘리기
        else:
            if cnt != 0:
                if cnt == K:
                    #print(f'찾았다! {K}만큼의 단어가 들어갈 수 있어요!')
                    find_one += 1
            cnt = 0

        # 추가로 넣어둔 0 버리겠습니다.
    row.pop()

    return find_one


for test_case in range(1, T+1):
    N,K = list(map(int,input().split()))
    big_arr = [list(map(int,input().split())) for _ in range(N)]
    result = 0

    # 결국,,, 연속한 1의 개수 찾아서,, 그 결과가 K개인거 세는 게임

    #print(big_arr)

    
    for row in big_arr:
        result += find_one_for_each_row(row)
        
    
    # 열 방향으로도 찾을게요
    transposed_big_arr = list(map(list, zip(*big_arr)))
    #print(transposed_big_arr)
    for row in transposed_big_arr:
        result += find_one_for_each_row(row)



    print(f"#{test_case} {result}")