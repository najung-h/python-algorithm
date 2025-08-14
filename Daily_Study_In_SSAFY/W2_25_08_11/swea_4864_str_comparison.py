import sys
sys.stdin = open('input_4864.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    
    str1 = input()
    str2 = input()

    lenn = len(str1)
    
    existence = 0

    for jdx in range(len(str2)-lenn +1):
        if str2[jdx:jdx+lenn] == str1:
                existence = 1
                break
    '''
    for jdx in range(len(str2)):
        for k in range(lenn):
            if str2[jdx+k] != str1[k]:
                break
        else:
            existence = 1'''

    print(f'#{test_case} {existence}')
