import sys
sys.stdin = open('input_11315.txt', 'r')

def is_there_omok_lets_find(lst):
    cnt = 0
    for col in lst:
        if col == '.':
            if cnt >= 5:
                return True
            cnt = 0
            break
        else: # 돌이라면
            cnt += 1

    if cnt == 5:
        return True
    return False


T = int(input())
    

for test_case in range(1, T+1):
    N = int(input())
    big_arr = [list(input()) for _ in range(N)]
    # [['.', '.', '.', '.', 'o'], ['.', '.', '.', 'o', '.'], ['.', '.', 'o', '.', '.'], ['.', 'o', '.', '.', '.'], ['o', '.', '.', '.', '.']]
    found = False

    cnt = 0
    for row in big_arr:
        # 행방향 순회
        if is_there_omok_lets_find(row) is True:
            found = True
            break

    transposed_big_arr = list(map(list, zip(*big_arr)))

    for row in transposed_big_arr:
        # 열 방향 순회
        if is_there_omok_lets_find(row) is True:
            found = True
            break

    left_diagonal = []
    right_diagonal = []

    for k in range(5):
        if found is True:
            break

        for n in range(N-4):
            # \ 대각선
            left_diagonal.append(big_arr[k+n][k])
            right_diagonal.append(big_arr[n+k][4-k])

        if len(left_diagonal) == 5:
            if(is_there_omok_lets_find(left_diagonal)) is True:
                found = True
                break
        
        if len(right_diagonal) == 5:
            if(is_there_omok_lets_find(right_diagonal)) is True:
                found = True
                break
        
    if found is True:
        print(f"#{test_case} YES")
    else:
        print(f"#{test_case} NO")

    


