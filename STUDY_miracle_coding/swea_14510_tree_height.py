import sys
sys.stdin = open('input_14510.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    tree_height_lst = list(map(int, input().split()))
    
    # 나무 높이 리스트를 물 주기 리스트로 변환하겠습니다.
    watering_lst = [max(tree_height_lst) - tree for tree in tree_height_lst]
    #print('물을 총 얼마나 줘야하는거야?', sum(watering_lst))
    # ------------- 1. ----------
    # 홀수 나무와 짝수나무 개수를 계산해보자
    even_tree_cnt, odd_tree_cnt = 0,0

    for tree in watering_lst:
        if tree % 2 == 1: #홀수트리
            odd_tree_cnt += 1
            if tree != 1:
                even_tree_cnt += (tree-1) // 2
        else:
            even_tree_cnt += (tree) // 2

    #print('짝수 나무 : ', even_tree_cnt, '   홀수 나무 : ', odd_tree_cnt)

    # -------------- 2. ----------
    '''짝수 > 홀수라면, 
    많은 개수만큼 홀수 날에도 물주기를 고려해봐야한다.
    day = 홀수날 * 2 + (짝수 - 홀수-1) * 3 +1
    
    반대로, 홀수 > 짝수라면
    day = 짝수날 * 2 해주고, (홀수-짝수) * 2 해주어야 한다.

    '''
    
    if even_tree_cnt == odd_tree_cnt:
        day = 2 * even_tree_cnt

    elif even_tree_cnt > odd_tree_cnt:
        day = odd_tree_cnt * 2 + (even_tree_cnt-1-odd_tree_cnt) * 3 + 1

    else: # 홀수 > 짝수
        day = even_tree_cnt * 2 + (odd_tree_cnt - even_tree_cnt) * 2
    '''while max(tree_height_lst) - min(tree_height_lst) > 0 :
        

        pass'''
    
    print(f'#{tc} {day}')