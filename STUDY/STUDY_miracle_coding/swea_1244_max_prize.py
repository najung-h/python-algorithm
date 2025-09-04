import sys
sys.stdin = open('input_1244.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    num, C = input().split()
    num_lst = list(map(int, num))   # [1, 2, 3]
    N = len(num)
    C = int(C)

    for i in range(N-1):
        if C == 0:
            break

        now_nom_lst = num_lst[i:]
        max_num = max(now_nom_lst)

        # 현재 자리가 이미 최대값이면 패스
        if num_lst[i] == max_num:
            continue
        
        # 만약 max_num가 여러 개라면, 전략적으로 위치를 바꿔줄 필요가 있음.
        # 한 개인 경우
        if now_nom_lst.count(max_num) == 1:    
            max_num_idx = now_nom_lst.index(max_num)
            num_lst[i], num_lst[i+max_num_idx] = num_lst[i+max_num_idx], num_lst[i]
            C -= 1
        
        # 여러 개인 경우
            '''그러니까, 
            32888에서 
            82838을 만들고 
            88832를 만드는 경우에서 
            PRIORITY를 선택하겠다
            
            내 교환횟수가 2번이니까 [:2]까지 봤을 때
            3이 두 번째로 작잖아
                그럼 가장 뒤에 있는 -1번째 8이랑 교환하는게 아니라
                -2 번째 8이랑 교환하겠다
            '''
        
        else:
            #  네 핵심 아이디어: 남은 교환횟수 C 내 윈도우에서 priority 계산
            win_len = min(C, len(now_nom_lst))          # 예: C=2 -> [:2]
            window = now_nom_lst[:win_len]              # 현재 자리 포함 윈도우
            sorted_win = sorted(window)
            # 현재 값(=now_nom_lst[0])이 윈도우에서 몇 번째로 작은지 (0-based)
            priority = sorted_win.index(window[0])      # 중복 있으면 첫 위치(=작은 쪽) 사용
        

            max_num_idx_lst = []
            for idx in range(len(now_nom_lst)):
                if now_nom_lst[idx] == max_num:
                    max_num_idx_lst.append(idx)


            # 우선순위가 max 개수를 초과하면 맨 오른쪽으로 클램핑
            pick_from_right = min(priority, len(max_num_idx_lst) - 1)
            target = max_num_idx_lst[-1 - pick_from_right]

            # 스왑 및 C 감소
            if target != 0:
                num_lst[i], num_lst[i + target] = num_lst[i + target], num_lst[i]
                C -= 1


            if C == 0:
                break


    result = num_lst
    # 남은 교환 횟수 처리
    if N-1 < C: # 남는 교환횟수에 대해서는
        if (C-N+1) % 2 ==0 :
            result = num_lst
        
        else:
            if len(set(num_lst)) != len(num_lst):
                result = num_lst
            else:
                num_lst[-1], num_lst[-2] = num_lst[-2], num_lst[-1]
                result = num_lst

    result = list(map(str,result))
    result = ''.join(result)
    result = int(result)
    print(f'#{tc} {result}')