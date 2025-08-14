
'''start_parenthesis = ['(', '{', '[', '<']
end_parenthesis = [')', '}' , ']', '>']'''

'''parenthesis_dict = {'(' : ')', 
                    '{' : '}' , 
                    '[' : ']' , 
                    '<' : '>' }'''

import sys
sys.stdin = open('input_1218.txt', 'r')

parenthesis_dict ={')': '(', '}': '{', ']': '[', '>': '<'}




T = 10
for test_case in range(1, T+1):
    stack = []
    result = 1 # 성공

    N = int(input())
    parenthesis_lst = list(input())
    #print(list(parenthesis_dict.values()))

    for pdx in range(N):
        if parenthesis_lst[pdx] in list(parenthesis_dict.values()):
            stack.append(parenthesis_lst[pdx])
            #print('추가했어요', parenthesis_lst[pdx])
        else:
            if len(stack)<1:
                result = 0
                break

            output = stack.pop()
            #print('삭제할거에요', output)
            if parenthesis_dict.get(parenthesis_lst[pdx]) != output:
                result = 0
                break
    
    if result == 1 and len(stack) >0 :
        result = 0

    print(f'#{test_case} {result}')
    



