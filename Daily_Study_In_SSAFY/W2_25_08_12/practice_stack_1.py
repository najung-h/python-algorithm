stack = []


def push(ele):
    stack.append(ele)
    return stack

def pop():
    idx = len(stack)-1 # 마지막 원소
    if idx < 0:
        print('overflow')
        return 'overflow'
    stack.pop()
    return stack
    

push(2)
push(3)
push(4)
        # print(stack)
        # [2, 3, 4]

pop()
        # print(stack)   # [2, 3]
pop()
        # print(stack)   # [2]
pop()
        # print(stack)   # []
pop()
        # print(stack)    # overflow  #[]