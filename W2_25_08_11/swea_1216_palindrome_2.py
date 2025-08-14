import sys
sys.stdin = open('input_1216.txt', 'r')


def palindrome_test(lst, length):
    '''
    이 함수는 단일 lst를 입력 받았을 때
    길이가 length인 회문을 개수를 리턴하는 함수입니당
    '''
    found = False    # 회문 못 찾음으로 시작

    for idx in range(len(lst) - length + 1):
        test_arr = lst[idx:idx + length]
        if test_arr == test_arr[::-1]:
            #print('test_area', test_arr)
            #print('reversed_test_arr', test_arr[::-1])
            found = True

    return found



T = 10

for test_case in range(1, T+1):
    tc = int(input())

    big_arr = [list(input()) for _ in range(100)]
    transposed_big_arr = list(map(list, zip(*big_arr)))

    found = False
    for k in range(100, 0, -1):
        if found is True:
            break
        else:
            for rdx in range(100):
                if palindrome_test(big_arr[rdx], k) is True:
                    #print('안녕', k)
                    result = k
                    found = True
                    break

                elif palindrome_test(transposed_big_arr[rdx], k) is True:
                    #print('여기얌', k)
                    result = k
                    found = True
                    break

    print(f"#{tc} {result}")
