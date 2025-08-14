T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    
    test = list(input())
    #print(test)
     
    parentheses_lst = []  # 괄호 리스트
         
    for t in range(len(test)):
        if test[t] in ['(', '{', ')', '}']:  
            parentheses_lst.append(test[t])

    # 괄호 너 짝수개니?
    parentheses_str = ''.join(parentheses_lst)
    lenn = len(parentheses_str)
     
    if lenn % 2 != 0:
        #print('짝이 안 맞아요!')
        print(f"#{test_case} 0")
        continue
     
    poped_str = ''
    trying = 0
     
    while trying < lenn:
        parentheses_str = parentheses_str.replace('()', '')
        parentheses_str = parentheses_str.replace('{}', '')
        parentheses_str = parentheses_str.replace('()', '')
        parentheses_str = parentheses_str.replace('{}', '')

        trying += 1
         
             
    if len(parentheses_str) != 0:
        print(f"#{test_case} 0")
     
    else:
        print(f"#{test_case} 1")