import sys
sys.stdin = open('input_2005.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    big_arr = []
    #[[0], [0, 0], [0, 0, 0], [0, 0, 0, 0]]

    for k in range(N):
        big_arr.append([0] * (k+1)) 
    
    #print(big_arr)
    big_arr[0][0] =1 #처음값 1로 지정
  
    
    for rdx in range(1, N):  # N줄만큼  # 젤 윗 칸 생략
        len_col = len(big_arr[rdx])
        for cdx in range(len_col):   #rdx번째 행의 길이만큼
            # 열의 길이
            #print('좌표', rdx, cdx)
            #print('좌표에 있는 값_전', big_arr[rdx][cdx])
            
            if 0<= cdx-1 < len_col - 1:
                left_up = big_arr[rdx-1][cdx-1]
            else:
                left_up = 0
        
            if 0<= cdx < len_col - 1:
                right_up = big_arr[rdx-1][cdx]
            else:
                right_up = 0

            big_arr[rdx][cdx] += (left_up + right_up)
            #print('좌표에 있는 값_후', big_arr[rdx][cdx])

    '''print(f"#{test_case}")
    for row in big_arr:
        print(" ".join(map(str, row)))'''

    print(f"#{test_case}\n" + "\n".join(" ".join(map(str, row)) for row in big_arr))





