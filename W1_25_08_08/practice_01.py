import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for test_case in range(1, T+1):

    str = input()

    print(f"#{test_case} {str[::-1]}")