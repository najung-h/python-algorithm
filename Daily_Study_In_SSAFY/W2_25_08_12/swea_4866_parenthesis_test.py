import sys
sys.stdin = open('input_4866.txt', 'r')

stack = []

def parenthesis_test(input_str):
    stack = [] # 스택 초기화
    for s in input_str:
        if s =='(':
            stack.append(s)

        elif s =='{':
            stack.append(s)

        elif s == ')':
            if len(stack) < 1 or stack.pop() != '(':
                success = 0
                #print('case 1')
                break

        elif s == '}':
            if len(stack) < 1 or stack.pop() != '{':
                success = 0
                #print('case 2')
                break

    else:
        if len(stack) > 0:
            success = 0
            #print('case 3')
        else: 
            success = 1

    return success




def only_parenthesis(lst):
    result = ''
    for s in lst:
        if s in ['(', ')', '{', '}']:
            result += s
    return result  # str


    
T = int(input())

for test_case in range(1, T+1):
    stack = [] # 스택 초기화
    lst = list(input())   # 한 줄 받아오기


    only_parenthesis_str = only_parenthesis(lst)
    # ({}{}())  # str

    success = parenthesis_test(only_parenthesis_str)

    print(f'#{test_case} {success}')
