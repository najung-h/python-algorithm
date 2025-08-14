import sys
sys.stdin = open('input_parenthesis.txt', 'r')








def push(ele):
    stack.append(ele)
    return stack

def pop():
    idx = len(stack)-1 # 마지막 원소
    if idx < 0:  # 원소가 없는데 print를 시켰다는 의미
        #print('overflow')
        return 'overflow'
    stack.pop()
    return stack







T = int(input())

for test_case in range(1, T+1):
    print(f"#{test_case} ", end = '')

    stack = [] # 스택 초기화
    str = input()

    for s in str:
        if s =='(':
            push(s)
        elif s == ')':
            result = pop()
            #print('이곳', result)
            if result == 'overflow':
                print(') 가 많아')
                break
    else:
        if len(stack) > 0:
            print('( 가 많잖아')
        else: print('굿괄호')







    

