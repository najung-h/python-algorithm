import sys
sys.stdin = open('input_1215.txt', 'r')

T = 10

def palindrome_test(lst, length):
    '''
    이 함수는 단일 lst를 입력 받았을 때
    길이가 length인 회문을 개수를 리턴하는 함수입니당
    '''
    result = 0    # 회문 0개로 시작

    for idx in range(len(lst) - length + 1):
        test_arr = lst[idx:idx + length]
        if test_arr == test_arr[::-1]:
            #print('test_area', test_arr)
            #print('reversed_test_arr', test_arr[::-1])
            result += 1

    return result

#print(palindrome_test([1,2,3,4,5,6,5,4,3,2,1], 3))

for test_case in range(1, T+1):
    palindrome_length = int(input())
    big_arr = [list(input()) for _ in range(8)]

    # 각 행에서 대해서 검사 실시
    total_palindrome_count = 0

    for row in big_arr:
        total_palindrome_count += palindrome_test(row, palindrome_length)
    
    transposed_big_arr =list(map(list, zip(*big_arr)))
    #print(transposed_big_arr)

    for row in transposed_big_arr:
        total_palindrome_count += palindrome_test(row, palindrome_length)

    print(f"#{test_case} {total_palindrome_count}")
