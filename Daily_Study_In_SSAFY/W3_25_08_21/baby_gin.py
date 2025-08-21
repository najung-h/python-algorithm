# 완전탐색으로 구현한다
# 숫자들을 모두 6P3을 이용해서 배열한 다음에,
# 만약 6P3가 run / triplet이라면,
# 나머지 애들이 run / triplet인지도 확인한 다음
# 만약에 baby gin이라면 True값을 return한다.

import sys
sys.stdin = open('input_babygin.txt', 'r')


from itertools import permutations

def is_run(arr):
    arr = sorted(arr)
    #if arr in {[0,1,2], [1,2,3], [2,3,4], [3,4,5], [4,5,6], [5,6,7], [6,7,8], [7,8,9]}:
    return arr[0] +2 == arr[1] + 1 and  arr[1] + 1 == arr[2]


def is_triplet(arr):
    return len(set(arr)) == 1



T = int(input())

for tc in range(1, T+1):
    arr = list(map(int, input()))

    
    for perm in list(permutations(arr, 6)):
        left, right = perm[:3], perm[3:]

        if is_run(left) and is_run(perm[3:]) \
            or ( is_run(left) == True ) and (is_triplet(perm[3:]) == True) \
            or (is_triplet(left) == True ) and (is_triplet(perm[3:]) == True) \
            or (is_triplet(left) == True ) and ( is_run(perm[3:]) == True) :
            
            print(f'#{tc} YES')
                
            found = True
            break
        
    if not found:
        print(f'#{tc} No')   