import sys
sys.stdin = open('input_1989.txt', 'r')

T = int(input())


def is_palindrome(str):
    '''이 함수는
    입력받은 str에 대해서
    회문 테스트 결과를
    TRUE 올 FALSE로 반환합니다.
    '''
    for idx in range(len(str)//2):
        if str[idx] != str[len(str)-idx-1]:
            return False
    return True

for test_case in range(1, T+1):
    str = input()
    if is_palindrome(str) is True:
        result = 1
    else: result = 0
    
    print(f'#{test_case} {result}')