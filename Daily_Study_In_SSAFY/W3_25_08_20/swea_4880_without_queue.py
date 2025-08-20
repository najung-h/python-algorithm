T = int(input())
 
def gawe_bawe_bo_winner(a_idx, b_idx, players):
    '''
    가위바위보의 승자를 리턴합니다.

    1==가위, 2==바위, 3==보
    비기는 경우, 앞에 사람이 이긴다
    1 > 3
    2 > 1
    3 > 2
    '''
    a_what = players[a_idx]  # a가 낸 것
    b_what = players[b_idx]  # b가 낸 것
     
    if a_what == b_what :
        return a_idx
    elif a_what == 1:  # 가위
        if b_what == 3 or b_what== 1:  # 보
            return a_idx
        else:  # 바위
            return b_idx
    elif a_what == 2:  # 바위
        if b_what == 1 or b_what==  2:  # 가위
            return a_idx
        else:  # 보
            return b_idx
    elif a_what == 3:  # 보
        if b_what == 2 or b_what== 3:  # 바위
            return a_idx
        else:  # 가위
            return b_idx
 



def tournament_winner(start, end, players):
    '''
    재귀함수로 구현
    '''
    if start == end:
        return start
     
    mid = (start + end) // 2
     
    winner1 = tournament_winner(start, mid, players)
    winner2 = tournament_winner(mid + 1, end, players)
     
    return gawe_bawe_bo_winner(winner1, winner2, players)
 






for test_case in range(1, T + 1):
    N = int(input())
    gawe_bawe_bo_lst = list(map(int, input().split()))
     
    
    winner_index = tournament_winner(0, N - 1, gawe_bawe_bo_lst)
    print(f'#{test_case} {winner_index + 1}')




