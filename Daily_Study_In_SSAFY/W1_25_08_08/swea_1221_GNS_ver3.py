import sys
sys.stdin = open('input_1221.txt', 'r')

T = int(input())

# 딕셔너리는 순서가 보장되지 않으므로
# 차례대로 출력하기 위하여
# num_lst 제작
num_lst = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

for test_case in range(1, T+1):
		# count 를 진행할 딕셔너리입니당.
		# 매번 초기화 필요
    alien_count_dic = {"ZRO":0, "ONE":0, "TWO":0, "THR":0, "FOR":0, "FIV":0, "SIX":0, "SVN":0, "EGT":0, "NIN":0}

    tc, length = input().split()
    alien_lst = list(input().split())

		# count해서 value 값 늘리기
    for i in alien_lst:
        alien_count_dic[i] += 1
    #{'ZRO': 700, 'ONE': 717, 'TWO': 721, 'THR': 737, 'FOR': 683, 'FIV': 742, 'SIX': 680, 'SVN': 661, 'EGT': 732, 'NIN': 713}
    
    # 이제 value 값 만큼  key값을 출력
    print(f"#{test_case} ")
    for num in num_lst:
        num_cnt = alien_count_dic.get(num)  # 700
        print((num+' ') * num_cnt, end = '')