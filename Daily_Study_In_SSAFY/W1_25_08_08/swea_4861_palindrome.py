import sys
sys.stdin = open('input_4861.txt', 'r')


def palindrome_test(lst):
    '''이 함수는
    입력된 리스트에 대해서
    회문인지 아닌지를 검사하여
    회문이면 True, 아니면 False를 반환합니다.
    '''
    for a in range(len(lst)//2) :
        if lst[a] != lst[-(a+1)]:
            return False
    return True

     
T = int(input())
for test_case in range(1, T + 1):
    N, M = list(map(int, input().split()))  # 리스트로 받아오는게 더 빠름.

    big_lst = [list(input()) for _ in range(N)]
         
    # 정식 방향에 대한 검사
    # found == True 이면 break하고 출력할 예정.
    found = False   
         
    for i in range(N):  # 각 행에 대해
        for k in range(N-M+1): # 각 M짜리 문자열에 대해
            test = big_lst[i][k:k+M]   # test는 요만큼 잘라온 대상이고,
            if palindrome_test(test) is True:     # 회문 테스트를 시행
                print(f'#{test_case} {"".join(test)}') 
                found = True
                break
             
        if found == True:
            break

    # 전체를 돌아도 찾지 못했다면
    # 세로 방향으로 회문 검사 시작.
    if found is False:
        transposed_big_lst = list(zip(*big_lst))         
        #N, M = M, N       
        for i in range(len(transposed_big_lst)):
            col = transposed_big_lst[i]
            for k in range(len(col) - M + 1):
                test = col[k:k+M]
                 
                if palindrome_test(test) is True:
                    print(f'#{test_case} {"".join(test)}') 
                    found = True
                    break
                 
            if found is True:
                break