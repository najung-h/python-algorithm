import sys
sys.stdin = open('input_1221.txt', 'r')

T = int(input())

# 딕셔너리를 이용해서 
# 딕셔너리 키 값에 대한 value를 가져온 다음에 변경
# 그 value 값을 기준으로 sorting 한 후
# 다시 key 값을 가져와서 출력할 생각입니다
alien_dic = {"ZRO":0, "ONE":1, "TWO":2, "THR":3, "FOR":4, "FIV":5, "SIX":6, "SVN":7, "EGT":8, "NIN":9}


for test_case in range(1, T+1):

    tc, length = input().split()
    alien_lst = list(input().split())

    print(f"#{test_case} ")
    print('ZRO ' * (alien_lst.count('ZRO')), end='')
    print('ONE ' * (alien_lst.count('ONE')), end='')
    print('TWO ' * (alien_lst.count('TWO')), end='')
    print('THR ' * (alien_lst.count('THR')), end='')
    print('FOR ' * (alien_lst.count('FOR')), end='')
    print('FIV ' * (alien_lst.count('FIV')), end='')
    print('SIX ' * (alien_lst.count('SIX')), end='')
    print('SVN ' * (alien_lst.count('SVN')), end='')
    print('EGT ' * (alien_lst.count('EGT')), end='')
    print('NIN ' * (alien_lst.count('NIN')))

    


    


    '''    for i in alien_lst[:15]:
        #alien_dic.get(i)
        
        i = alien_dic.get(i)'''







